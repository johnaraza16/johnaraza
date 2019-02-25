from rest_framework import serializers
from malnutrition.models import AppUser,Food,Foodlog, Question
from django.contrib.auth.models import User


class DjangoAdminSerializer(serializers.ModelSerializer):
    """
        This serialize is the serializer for the django auth model
    """

    class Meta:
        model = User
        fields = ('username', 'password')

class UserSerializer(serializers.ModelSerializer):
    user = DjangoAdminSerializer()
    
    class Meta:
        model = AppUser
        fields = '__all__'

    def create(self, validated_data):
        print(validated_data)
        
        user = User.objects.create_user(
            username = validated_data['user']['username'],
            password = validated_data['user']['password']
        )

        instance =  AppUser.objects.create(
            user = user,
            firstname = validated_data['firstname'],
            lastname = validated_data['lastname'],
            birthdate = validated_data['birthdate'],
            gender = validated_data['gender'],
            weight = validated_data['weight'],
            height = validated_data['height'],
            physical_activity = validated_data['physical_activity']
        )

        return instance


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields ='__all__'

class FoodlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foodlog
        fields ='__all__'

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = '__all__'
