from rest_framework.serializers import ModelSerializer
from .models import Item
from .models import User

class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
