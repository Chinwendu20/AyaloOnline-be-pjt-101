from rest_framework import serializers
from .models import  MyUser
from .models import ModelLeesee

class UserSerializer(serializers.Serializer):
		choicess=[('Leeser', 'Leeser'), ('Leesee', 'Leessee')]
		username=serializers.CharField()
		email=serializers.EmailField()
		password=serializers.CharField()
		AccountType=serializers.ChoiceField(choices=choicess, allow_blank=False)
			


class CompleteProfileSerializer(serializers.Serializer):

		First_name=serializers.CharField()
		Last_name=serializers.CharField()
		gender_choices=[('Female', 'Female'), ('Male', 'Male')]
		Gender=serializers.ChoiceField(choices=gender_choices, allow_blank=False)
		Phone_number = serializers.CharField()

		


class LeeseeSerializer(serializers.ModelSerializer):
	class Meta:
		model=ModelLeesee
		exclude=['Leesee']