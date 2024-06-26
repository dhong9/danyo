# Django
from django.contrib.auth import authenticate, get_user_model

# Djoser
from djoser.conf import settings
from djoser.serializers import TokenCreateSerializer

# Rest Framework
from rest_framework import serializers

# Custom models
from portfolio.accounts.models import Profile

User = get_user_model()

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class CustomTokenCreateSerializer(TokenCreateSerializer):

    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        user = self.user
        return {
            'id': user.id,
            'username': user.username,
            'email': user.email
        }

    def validate(self, attrs):
        password = attrs.get("password")
        params = {settings.LOGIN_FIELD: attrs.get(settings.LOGIN_FIELD)}
        self.user = authenticate(
            request=self.context.get("request"), **params, password=password
        )
        if not self.user:
            self.user = User.objects.filter(**params).first()
            if self.user and not self.user.check_password(password):
                self.fail("invalid_credentials")
        # We changed only below line
        if self.user: # and self.user.is_active: 
            return attrs
        self.fail("invalid_credentials")