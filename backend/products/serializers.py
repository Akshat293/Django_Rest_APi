from rest_framework import serializers
from .models import Product
from rest_framework.reverse import reverse
from .validators import validate_title,unique_product_title
from api.serializers import UserSerializer,UserModelSerializer
from django.conf import settings
user=settings.AUTH_USER_MODEL
class ProductSerializer(serializers.ModelSerializer):
    owner=UserSerializer(source='user', read_only=True)
    usermod= UserModelSerializer(source='user', read_only=True)
    my_discount=serializers.SerializerMethodField(read_only=True)
    edit_url=serializers.SerializerMethodField(read_only=True)
    url=serializers.HyperlinkedIdentityField(view_name= 'product-detail',lookup_field='pk')
    title = serializers.CharField(validators=[validate_title,unique_product_title])
    # email=serializers.EmailField(write_only=True)
    class Meta:
        model = Product
        fields = [
            'owner',
            'usermod',
            'url',
            'edit_url',
            'pk',
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount'
        ]
     # How to validate the fields
    # def validate_title(self,value):
    #     request=self.context.get('request')
    #     user=request.user
    #     qs=Product.objects.filter(user=user,title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} is already a product name")
    #     return value
        # we can change the name here
    
    def get_edit_url(self,obj):
        request=self.context.get('request')
        if request is None :
            return None
        return reverse('product-update',kwargs={'pk':obj.pk},request=request) # diff from the django reverse
    # def create(self, validated_data):
    #     email=validated_data.pop('email')
    #     print(email)
    #     obj=super().create(validated_data)
    #     return obj
 
    
    def get_my_discount(self,obj):
        if not hasattr(obj,'id'):
            return None
        if not isinstance(obj,Product):
            return None
        return obj.get_discount()

  
# isinstance() --> It is used to check the object type
# hasattr() --> chech if the specified object has the specified attribute

# Serializables can injest data and clean it and can verify the data

       