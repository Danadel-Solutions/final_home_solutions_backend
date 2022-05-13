from rest_framework import serializers
from .models import PhotoBook, Property

class PropertySerializer(serializers.ModelSerializer):
    seller_id = serializers.ReadOnlyField(source = 'seller.id')
    seller_name = serializers.ReadOnlyField(source = 'seller.username')
    cover_photo = serializers.ImageField()
    seller_date_joined = serializers.ReadOnlyField(source = 'seller.date_joined')
    photos = serializers.SerializerMethodField()
    seller_phone_number = serializers.ReadOnlyField(source = 'seller.phone')

    class Meta:
        model = Property
        fields = ['id', 'first_title', 'second_title', 'description', 'seller', 'seller_id', 'seller_name', 'cover_photo', 'price', 'type','location', 'added', 'seller_date_joined', 'photos', 'toilet_count', 'bathroom_count', 'bedroom_count', 'seller_phone_number',]
    def get_photos(self, obj):
            # photos = obj.photos.all()
        # This work better for me, because Books objects doesn´t have 
        # the attribute photos, but PhotoBooks, contain the ```book_id```
        photos = PhotoBook.objects.filter(book=obj.id)
        return [photo.image.url for photo in photos] 