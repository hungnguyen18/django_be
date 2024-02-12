from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Item
from .serializers import ItemSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

def response_format(code, message, data=None):
    return {'code': code, 'message': message, 'data': data}

@api_view(['GET'])
def get_all_items(request):
    try:
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(response_format(status.HTTP_200_OK, 'Success', serializer.data), status=status.HTTP_200_OK)
    except Exception as e:
        return Response(response_format(status.HTTP_500_INTERNAL_SERVER_ERROR, str(e)), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['PUT'])
def update_item(request, pk):
    try:
        item = Item.objects.get(pk=pk)
        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(response_format(status.HTTP_200_OK, 'Item updated successfully', serializer.data), status=status.HTTP_200_OK)
        return Response(response_format(status.HTTP_400_BAD_REQUEST, 'Invalid data'), status=status.HTTP_400_BAD_REQUEST)
    except Item.DoesNotExist:
        return Response(response_format(status.HTTP_404_NOT_FOUND, 'Item not found'), status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response(response_format(status.HTTP_500_INTERNAL_SERVER_ERROR, str(e)), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['DELETE'])
def delete_item(request, pk):
    try:
        item = Item.objects.get(pk=pk)
        item.delete()
        return Response(response_format(status.HTTP_204_NO_CONTENT, 'Item deleted successfully'), status=status.HTTP_204_NO_CONTENT)
    except Item.DoesNotExist:
        return Response(response_format(status.HTTP_404_NOT_FOUND, 'Item not found'), status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response(response_format(status.HTTP_500_INTERNAL_SERVER_ERROR, str(e)), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def create_item(request):
    try:
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(response_format(status.HTTP_201_CREATED, 'Item created successfully', serializer.data), status=status.HTTP_201_CREATED)
        return Response(response_format(status.HTTP_400_BAD_REQUEST, 'Invalid data'), status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(response_format(status.HTTP_500_INTERNAL_SERVER_ERROR, str(e)), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def hello_world(request):
    return JsonResponse(response_format(status.HTTP_200_OK, 'Hello, World!'))

def hello_world2(request):
    return JsonResponse(response_format(status.HTTP_200_OK, 'Hello, World! 2 :))'))
