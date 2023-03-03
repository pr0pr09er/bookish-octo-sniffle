from rest_framework import status
from rest_framework.response import Response
from .models import Cart
from .serializers import CartSerializer
from rest_framework.decorators import api_view


# Я так понял что надо просто получать описание,
# если неправильно понял, напишите в комментарии,
# попробую связать с продуктом, чтобы сразу создавать описание для продукта.
# Классы я понимаю, просто не хочу на них писать.

@api_view(['GET'])
def api_overview(request):
    api_urls = {
        "List view": "api/v1/get_reviews/",
        "Detail view": "api/v1/get_review/<int:pk>/",
        "Create view": "api/v1/create_review/",
        "Update view": "api/v1/update_review/<int:pk>/",
        "Delete view": "api/v1/delete_review/<int:pk>/"
    }
    return Response(api_urls)


@api_view(['GET'])
def get_product_reviews(request):
    queryset = Cart.objects.all()
    serializer = CartSerializer(
        queryset,
        many=True
    )

    return Response(
        serializer.data,
        status=status.HTTP_200_OK
    )


@api_view(['GET'])
def get_product_review(request, pk):
    try:
        queryset = Cart.objects.get(id=pk)
    except Cart.ObjectDoesNotExist:
        return Response(
            {"error": f"Object {pk} does not exist"},
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = CartSerializer(
        queryset
    )

    return Response(
        serializer.data,
        status=status.HTTP_200_OK
    )


@api_view(['POST'])
def create_product_review(request):
    serializer = CartSerializer(
        data=request.data
    )
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response(
        serializer.data,
        status=status.HTTP_201_CREATED
    )


@api_view(['PUT', 'PATCH'])
def update_product_review(request, pk):
    try:
        instance = Cart.objects.get(id=pk)
    except Cart.DoesNotExist:
        return Response(
            {"error": f"Object {pk} does not exist"},
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = CartSerializer(
        data=request.data,
        instance=instance
    )
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response(
        serializer.data,
        status=status.HTTP_200_OK
    )


@api_view(['DELETE'])
def delete_product_review(request, pk):
    try:
        queryset = Cart.objects.get(id=pk)
    except Cart.DoesNotExist:
        return Response(
            {"error": f"Object {pk} does not exist"},
            status=status.HTTP_404_NOT_FOUND
        )

    queryset.delete()

    return Response(
        {"review": f"Object {pk} deleted"},
        status=status.HTTP_200_OK
    )
