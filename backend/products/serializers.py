from rest_framework import serializers

from . import models


class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Picture
        fields = ('id', 'product', 'image')


class ConcisePictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Picture
        fields = ('id', 'image')

class ProductSerializer(serializers.ModelSerializer):
    images = ConcisePictureSerializer(many=True)

    class Meta:
        model = models.Product
        fields = ('id', 'name', 'price', 'description', 'stock_count', 'images')

    def create(self, validated_data):
        images_data = validated_data.pop('images')
        product = models.Product.objects.create(**validated_data)
        for image_data in images_data:
            models.Picture.objects.create(product=product, **image_data)
        return product


# from PIL import Image
#
# width = 400
# height = 300
#
# img  = Image.new( mode = "RGB", size = (width, height) )
#
# data = {
#     "name": "elo",
#     "price": 90,
#     "description": "nothing special",
#     "stock_count": 3,
#     "images": [
#         {"image": img}, {"image": img}
#     ]
# }