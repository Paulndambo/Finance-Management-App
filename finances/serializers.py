from rest_framework import serializers
from finances.models import Expenditure

class ExpenditureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expenditure
        fields = '__all__'