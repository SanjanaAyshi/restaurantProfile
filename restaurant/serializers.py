from rest_framework import serializers
from .models import Food, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tag
        fields = ['id', 'name', 'slug']

class FoodSerializer(serializers.ModelSerializer):
    tags=TagSerializer(many=True,read_only=True)
    image_url=serializers.SerializerMethodField()
    class Meta:
        model=Food
        fields=[
            'id',          
            'title',
            'description',
            'price',
            'is_special',
            'tags',        # nested tags
            'image',
            'image_url',   # full URL for front-end
            'created_at',
        ]
        read_Only_fields=['id','created_at','image_url']
    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        return None
        