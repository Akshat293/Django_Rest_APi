from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.conf import settings
user=get_user_model()

class UserProductInlineSerializer(serializers.Serializer):
   url=serializers.HyperlinkedIdentityField(view_name='product-detail',lookup_field='pk',read_only=True)
   title=serializers.CharField(read_only=True)


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(read_only=True)
    first_name = serializers.CharField(read_only=True)
    last_name = serializers.CharField(read_only=True)
    is_staff = serializers.BooleanField(read_only=True)
    is_active = serializers.BooleanField(read_only=True)
    is_superuser = serializers.BooleanField(read_only=True)
    last_login = serializers.DateTimeField(read_only=True)
    date_joined = serializers.DateTimeField(read_only=True)
    # other_products = serializers.SerializerMethodField(read_only=True)

    # def get_other_products(self,obj):
    #    request=self.context.get('request')
    #    if request is None :
    #        return None
    #    return UserProductInlineSerializer(obj.product_set.all()[:4],many=True,context={'request':request}).data

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = [
            'username',
            'id',
        ]