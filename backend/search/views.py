from django.db import models
from rest_framework.generics import ListAPIView
from products.models import Product
from rest_framework.response import Response
from products.serializers import ProductSerializer
from rest_framework import generics
from . import client
# Create your models here.
class SearchListView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        query = request.GET.get('q')
        print(query)
        if not query:
            return Response('', status=400)
        results = client.perform_search(query)
        return Response(results)

class SearchListOldView(ListAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    
    def get_queryset(self,*args,**kwargs):
        request=self.request
        print(request.GET)
        qs=super().get_queryset(*args,**kwargs)
        query=request.GET.get('q')
        user=None
        result=Product.objects.none()
        if query is not None:
            user=None
            if request.user.is_authenticated:
              user=request.user
            result=qs.search(query,user)
        return result
        