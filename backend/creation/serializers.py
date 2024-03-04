from rest_framework import serializers
from .models import*

class UserRegisterserializers(serializers.ModelSerializer):
    class Meta:
        model = UserRegister
        fields = '__all__'

class LoanSerialiser(serializers.ModelSerializer):
     class Meta:
        model = Loan
        fields = '__all__'