import json
from django.shortcuts import render
from django.http import JsonResponse
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.models import Product
from products.serializers import ProductSerializer
# Create your views here.
# @api_view(['GET'])
# def api_home(request):
#     instance=Product.objects.all().order_by("?").first()
#     data={}
#     if instance:
#         data=ProductSerializer(instance).data
#     return Response(data)

@api_view(['POST'])
def api_home(request):
    senpai=ProductSerializer(data=request.data)
    if senpai.is_valid(raise_exception=True):    # Additional feature to validate the json form
        #data=senpai.save() # If we dont have the instance to the model then 
        # It will not get the get_discount function
        return Response(senpai.data)


   #*
   # body=response.body  byte type string
   #  data={}
   #  try:    If body dosnt have the json data
   #   data=json.loads(body) . Convert byte type string into json format
   #  except:
   #   pass
   #  We need to convert the Http response to serializable 
   #   data['header']=dict(request.header)
   #   data['content_type]=request.content_type
   #   print(request.GET)
   # 
   #  *#


   #*
   # model_data=Product.objects.all().order_by("?").first()
   # data={} manually making a dictionary to pass to the json response
   # if model_data:
   #    data=model_to_dict(model_data,fieds[''])
   # return JsonResponse(data)
   # *#

