from django.db import transaction
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer

from users.models import GENDER_SELECTION, CustomUser

class CustomUserDetailsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = (
            'pk',
            'first_name',
            'middle_name',
            'last_name',
            'email',
            'phone_number',
            'date_joined',
        )
        read_only_fields = ('email', 'pk')
class CustomRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField(max_length = 240)
    middle_name = serializers.CharField(max_length = 240)
    last_name = serializers.CharField(max_length = 240)
    phone_number = serializers.CharField(max_length=30)
    date_joined = serializers.DateTimeField()
    

    # Define transaction.atomic to rollback the save operation in case of error
    @transaction.atomic
    def save(self, request):
        user = super().save(request)
        user.first_name = self.data.get('first_name')
        user.middle_name = self.data.get('middle_name')
        user.last_name = self.data.get('last_name')
        user.phone_number = self.data.get('phone_number')
        user.date_joined = self.data.get('date_joined')
       
        user.save()
        return user