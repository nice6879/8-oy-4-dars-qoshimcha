from rest_framework import serializers
from Goods.models import Category , Product,Banner,ProductImg, Cart,CartProduct,Order,ProductEnter,WishList, Info


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        modeel=Category
        fields='__all__'

class ProductSerializer(serializers.ModelSerializer):
    prodoct=CategorySerializer(many=True,read_only=True)
    class Meta:
        model=Product
        fields='__all__'




class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Banner
        fields='__all__'

class ProductImgSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductImg
        fields='__all__'
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cart
        fields='__all__'



class CartProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=CartProduct
        fields='__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields='__all__'


class ProductEnterSerializer(serializers.Serializer):
    class Meta:
        model=ProductEnter
        fields='__all__'

class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model=WishList
        fields='__all__'

class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Info
        fields='__all__'





