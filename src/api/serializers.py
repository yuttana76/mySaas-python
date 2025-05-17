from rest_framework import serializers

class ProductInlineSerializer(serializers.Serializer):
    hy_url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk',
        lookup_url_kwarg='pk',
        read_only=True,
    )
    title = serializers.CharField(read_only=True)

class UserPublicSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    username = serializers.CharField(read_only=True)
    email = serializers.EmailField(read_only=True)
    other_products = serializers.SerializerMethodField(read_only=True)
    # first_name = serializers.CharField(read_only=True)
    # last_name = serializers.CharField(read_only=True)
    # full_name = serializers.SerializerMethodField(read_only=True)

    # def get_full_name(self, obj):
    #     return f"{obj.first_name} {obj.last_name}" if obj.first_name and obj.last_name else None

    def get_other_products(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        user = obj
        my_products = user.product_set.all()[:2]
        return ProductInlineSerializer(my_products, many=True, context=self.context).data