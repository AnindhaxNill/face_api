from rest_framework import serializers
from .models import *


class AccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountsModel
        fields = "__all__"

class ImageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageModel
        fields = ['image','account_id','name']