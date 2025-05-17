from rest_framework import  generics,mixins, permissions
# from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from django.http import Http404
from django.shortcuts import get_object_or_404

from api.mixins import (
            UserQuerySetMixin,
            StaffEditorPermissionMixin
                        )

from .models import Product
from api.permissions import IsStaffEditorPermission
from .serializers import ProductSerializer


# get method is used to retrieve data from the server
# post method is used to send data to the server
class ProductListCreateAPIView(
    UserQuerySetMixin,
    StaffEditorPermissionMixin,
    generics.ListCreateAPIView):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # Authentication is in setting.py /REST_FRAMEWORK
    # authentication_classes = [
    #     authentication.SessionAuthentication,
    #     # authentication.TokenAuthentication
    #     TokenAuthentication,
    #     ]

    # permission_classes = [permissions.DjangoModelPermissions]
    permission_classes = [permissions.IsAdminUser,IsStaffEditorPermission]

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        # print(serializer.validated_data)

        # email = serializer.validated_data.get('email')
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title

        serializer.save(user=self.request.user, content=content)
        # send a Django signal


    # def get_queryset(self,*args,**kwargs):
    #     qs=super().get_queryset(*args,**kwargs)
    #     request = self.request

    #     # print(request.user)
    #     user = request.user
    #     if not user.is_authenticated:
    #         return Product.objects.none()
    #     return qs.filter(user=request.user)
    
product_list_create_view = ProductListCreateAPIView.as_view()

class ProductDetailAPIView(
    UserQuerySetMixin,
    StaffEditorPermissionMixin,
    generics.RetrieveAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [permissions.IsAdminUser,IsStaffEditorPermission]

product_detail_view = ProductDetailAPIView.as_view()

class ProductUpdateAPIView(
    UserQuerySetMixin,
    StaffEditorPermissionMixin,
    generics.UpdateAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_filed = 'pk'
    # permission_classes = [permissions.IsAdminUser,IsStaffEditorPermission]

    def perform_update(self, serializer):
        print(serializer.validated_data)
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title
            instance.save()

product_update_view = ProductUpdateAPIView.as_view()

class ProductDestroyAPIView(
    UserQuerySetMixin,
    StaffEditorPermissionMixin,
    generics.DestroyAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_filed = 'pk'
    # permission_classes = [permissions.IsAdminUser,IsStaffEditorPermission]

    def perform_destroy(self, instance):
        # instance.user = self.request.user
        # instance.save()
        # instance.delete()
        super().perform_destroy(instance)

product_destroy_view = ProductDestroyAPIView.as_view()


# class ProductListAPIView(generics.ListAPIView):
#     '''
# #     Not gonna use this method
# #     ''' 
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

# product_list_view = ProductListAPIView.as_view()

class ProductMixinView(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    permission_classes = [permissions.IsAdminUser,IsStaffEditorPermission]

    def get(self, request, *args, **kwargs): #HTTP -> get
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = "this is a single view doing cool stuff"
        serializer.save(content=content)

product_mixin_view = ProductMixinView.as_view()

@api_view(['GET', 'POST'])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method  

    if method == "GET":
        if pk is not None:
            # detail view
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data
            return Response(data)
        # list view
        queryset = Product.objects.all() 
        data = ProductSerializer(queryset, many=True).data
        return Response(data)

    if method == "POST":
        # create an item
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)
        return Response({"invalid": "not good data"}, status=400)