from rest_framework.generics import RetrieveAPIView, GenericAPIView,  ListAPIView, CreateAPIView, ListCreateAPIView, UpdateAPIView, DestroyAPIView
# Create your views here.
from .models import Product
from .serializers import ProductSerializer
from django.http import Http404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from api.mixins import IsStaffEditormixins,UserQuerySetmixin


class ProductDetailAPIView(RetrieveAPIView):
    queryset = Product.objects.all().order_by('-id')
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class ProductUpdateAPIView(UpdateAPIView, IsStaffEditormixins):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        # If I want to add some additional changes while updating
        content = "Update hua ha bhai"
        instance = serializer.save(content=content)


class ProductDeleteAPIView(DestroyAPIView, IsStaffEditormixins):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)


class ProductListCreateAPIView(ListCreateAPIView, IsStaffEditormixins,UserQuerySetmixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        # If we want to manupulate the data recived from post request
        content = serializer.validated_data.get('title')
        serializer.save(user=self.request.user ,content=content)
    
    def get_queryset(self):
        request=self.request
        print(request.user)
        qs=super().get_queryset()
        return qs.filter(user=request.user)
       #filtered the queryset based on the user


# Lets define a function thart will store all the three features
@api_view(['GET', 'POST'])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method
    if method == 'GET':
        # in get case there will be two cases
        # get a single object detail
        if pk is not None:
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj).data
            return Response(data)
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data
        return Response(data)
        # get all the objects
    if method == 'POST':
        senpai = ProductSerializer(data=request.data)
        if senpai.is_valid(raise_exception=True):
            title = senpai._validated_data.get('title')
            content = senpai.validated_data.get('content') or None
            if content is None:
                content = title
            senpai.save(content=content)
            # Additional feature to validate the json form
        # data=senpai.save() # If we dont have the instance to the model then
        # It will not get the get_discount function
            return Response(senpai.data)


# Creating a mixin class
class ProductMixnView(UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin, ListModelMixin, CreateAPIView, CreateModelMixin,
                      GenericAPIView, IsStaffEditormixins):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):  # Http->get
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)







     