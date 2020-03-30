from rest_framework import serializers

from profiles_api import models


class HelloSerializer(serializers.Serializer):
    """ Serializes a name field for testing our apiview """
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """ Serializes a user profile object """

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,  # Can use only to create object or update but not to Retrieve
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """ Create and return new user """
        user = models.UserProfile.objects.create_user(
            email = validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password']
        )
        return user
