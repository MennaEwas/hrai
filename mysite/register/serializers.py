from rest_framework import serializers
# from register.models import LoginModel
from .models import User

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, max_length = 200)
    password = serializers.CharField(required=True, write_only = True)


    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validate_data):
        return User.objects.create(**validate_data)

    def update(self, instance, validate_data):
        instance.usernamr = validate_data.get('username', instance.username)
        instance.password1 = validate_data.get('password', instance.password1)


        instance.save()
        return instance

