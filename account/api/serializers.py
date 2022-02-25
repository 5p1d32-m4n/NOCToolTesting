from django.contrib.auth import authenticate
from rest_framework import serializers
from account.models import Accounts
from django.conf import settings


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        fields = '__all__'


class AccountLoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'}, trim_whitespace=False
    )

    def authenticate(self, **kwargs):
        return authenticate(self.context['request'], **kwargs)

    def _validate_username(self, username, password):
        user = None
        if username and password:
            user = self.authenticate(username=username, password=password)
        else:
            msg = _('Must include "username" and "password".')
            raise exceptions.ValidationError(msg)

        return user

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        user = None
        if 'allauth' in settings.INSTALLED_APPS:
            from allauth.account import app_settings
            # Authentication through email
            if app_settings.AUTHENTICATION_METHOD == app_settings.AuthenticationMethod.USERNAME:
                user = self._validate_username(username, password)

        # Did we get back an inactive user?
        if user:
            if not user.is_active:
                msg = _('User account is disabled.')
                raise exceptions.ValidationError(msg)
        else:
            msg = _('Unable to log in with provided credentials.')
            raise exceptions.ValidationError(msg)

        # If required, is the email verified?
        if 'dj_rest_auth.registration' in settings.INSTALLED_APPS:
            from allauth.account import app_settings
            if app_settings.EMAIL_VERIFICATION == app_settings.EmailVerificationMethod.MANDATORY:
                try:
                    email_address = user.emailaddress_set.get(email=user.email)
                except:
                    raise serializers.ValidationError(
                        _('E-mail is not registered.'))
                else:
                    if not email_address.verified:
                        raise serializers.ValidationError(
                            _('E-mail is not verified.'))

        attrs['user'] = user
        return attrs
