from rest_framework import serializers
from .models import Users

class UserSerializer(serializers.ModelSerializer):

    full_info = serializers.SerializerMethodField(read_only=True)

   
    class Meta:
        model = Users
        fields = ['id', 'name', 'email', 'password', 'age', 'full_info']
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': True,} 
        }
    def get_full_info(self, obj):
        return f"{obj.name} {obj.email}"
    
    def validate(self, data):
        if data ['user'].toLower() == data['email'].split('@')[0].lower():
            raise serializers.ValidationError("Username cannot be the same as email prefix.")
        return data
    
    def validate_age(self, value):
        if value < 10:
            raise serializers.ValidationError("Age must be at least 10.")
        return value
    
    def create(self, validated_data):
        return Users.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        for attr , value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
    