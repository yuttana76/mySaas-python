from api.serializers import ProductInlineSerializer, UserPublicSerializer
from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Product
from . import validators


class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(source='user',read_only=True)
    # related_products = ProductInlineSerializer(source="user.product_set.all",read_only=True,many=True)
    # my_user_data = serializers.SerializerMethodField(read_only=True)
    my_discount = serializers.SerializerMethodField(read_only=True)
    url = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    hy_url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk',
        lookup_url_kwarg='pk',
        read_only=True,
    )
    title = serializers.CharField(validators=[validators.unique_product_title,validators.validate_title_no_hello])
    name = serializers.CharField(source='title', read_only=True)

    class Meta:
        model = Product
        fields = [
            
            # 'related_products',
            # 'my_user_data',
            'pk',
            'title',
            'name',
            'content',
            'price',
            'sale_price',
            'my_discount',
            'hy_url',
            'edit_url',
            'url',
            'owner',
        ]

    # def get_my_user_data(self, obj):
    #     return {
    #         "username": obj.user.username
    #     }

    # def validate_title(self, value):
    #     request = self.context.get('request')
    #     if request is None:
    #         return value
    #     user = request.user
    #     qs = Product.objects.filter(user=user, title__iexact=value)        
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} is already been used.")
    #     return value
    
    # def create(self, validated_data):
    #     # return Product.objects.create(**validated_data)
    #     # email = validated_data.pop('email', None)
    #     obj =  super().create(validated_data)
    #     return obj
    
    # def update(self, instance, validated_data):
    #     email = validated_data.pop('email', None)
    #     return super().update(instance, validated_data)
    
    def get_edit_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-edit", kwargs={"pk": obj.pk}, request=request)
    
    def get_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-detail", kwargs={"pk": obj.pk}, request=request)

    def get_my_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        
        if not isinstance(obj, Product):
            return None
        
        return obj.get_discount()