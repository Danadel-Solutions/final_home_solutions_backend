from api.permissions import IsAuthor
from api.serializers import PropertySerializer
from .models import Property
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.response import Response


@api_view(["GET"])
@permission_classes(
    [
        permissions.AllowAny,
    ]
)
def get_properties(request):
    properties = Property.objects.all()
    serializer = PropertySerializer(properties, many=True)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([permissions.AllowAny])
def get_property(request, pk):
    property = Property.objects.get(id=pk)
    serializer = PropertySerializer(property, many=False)
    return Response(serializer.data)


@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def create_property(request):
    user = request.user
    data = request.data
    property = Property.objects.create(
        first_title= 'This is the title',
        second_title= 'This is a short description',
        description= 'This is a long description',
        price= 0,
        type= 'rent',
        purpose='forSale',
        location= 'Lagos',
        address= 'Sangotedo, Lagos',
        bedroom_count=1,
        toilet_count= 2,
        bathroom_count=3,
        seller = user
    )
    serializer = PropertySerializer(property, many=False)
    return Response(serializer.data)


@api_view(["PUT"])
@permission_classes([IsAuthor])
def update_property(request, pk):
    data = request.data
    property = Property.objects.get(id=pk)

    property.first_title = data["first_title"]
    property.second_title = data["second_title"]
    property.description = data["description"]
    property.price = data["price"]
    property.type = data["type"]
    property.purpose = data["purpose"]
    property.location = data["location"]
    property.address = data["address"]
    property.bedroom_count = data["bedroom_count"]
    property.bathroom_count = data["bathroom_count"]
    property.toilet_count = data["toilet_count"]

    property.save()

    serializer = PropertySerializer(Property, many=False)
    return Response(serializer.data)


@api_view(["POST"])
def uploadImage(request):
    data = request.data

    property_id = data["property_id"]
    property = Property.objects.get(id=property_id)

    property.cover_photo = request.FILES.get("image")
    property.save()

    return Response("Image was uploaded")


@api_view(["GET"])
@permission_classes([permissions.AllowAny])
def get_user_properties(request, pk):
    user = pk
    properties = Property.objects.filter(seller_id=user)
    serializer = PropertySerializer(properties, many=True)
    return Response(serializer.data)
