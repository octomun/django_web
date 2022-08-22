from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.authtoken.models import Token #토큰 모델
from rest_framework.validators import UniqueValidator # 이메일 중복 방지 검증 도구

class RegisterSerializer(serializers.ModelSerializer): # 회원가입 시리얼라이저
    email = serializers.EmailField(
        required = True,
        validators = [UniqueValidator(queryset=User.objects.all())],
    )
    password = serializers.CharField(
        write_only = True,
        required = True,
        validators = [validate_password], # 비밀번호 검증
    )
    password2 = serializers.CharField(
        write_only = True,
        required = True,
    )

    class Meta:
        model = User
        fields = ('username', 'password','password2','email')
    
    def validate(self, data):
        if data['password'] != data['password2']: # 비밀번호 일치 여부 확인
            raise serializers.ValidationError(
                {"password" : "Password fields didn't match"}
            )
        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            username = validated_data['username'],
            email = validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        token = Token.objects.create(user = user)
        return user