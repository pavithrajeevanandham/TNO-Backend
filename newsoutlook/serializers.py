from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['is_active'] = user.is_active
        token['phone_number'] = user.phone_number


        return token

    def validate(self, attrs):
        data = super().validate(attrs)

        # Add additional user details to the response
        data['user'] = {
            'username': self.user.username,
            'email': self.user.email,
            'firstName': self.user.first_name,
            'lastName': self.user.last_name,
            'isActive': self.user.is_active,
            'phoneNumber': self.user.phone_number,
        }

        return data
