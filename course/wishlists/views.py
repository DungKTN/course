from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .services import (
    create_wishlist,
    get_wishlist_by_id,
    get_all_wishlists,
    update_wishlist,
    delete_wishlist,
    get_wishlists_by_user
)

class WishlistListView(APIView):
    def get(self, request):
        try:
            wishlists = get_all_wishlists()
            return Response(wishlists, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"errors": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        try:
            wishlist = create_wishlist(request.data)
            return Response(wishlist, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response({"errors": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, wishlist_id):
        try:
            wishlist = update_wishlist(wishlist_id, request.data)
            return Response(wishlist, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"errors": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, wishlist_id):
        try:
            result = delete_wishlist(wishlist_id)
            return Response(result, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"errors": str(e)}, status=status.HTTP_404_NOT_FOUND)

class WishlistDetailView(APIView):
    def get(self, request, wishlist_id):
        try:
            wishlist = get_wishlist_by_id(wishlist_id)
            return Response(wishlist, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"errors": str(e)}, status=status.HTTP_404_NOT_FOUND)

class UserWishlistView(APIView):
    def get(self, request, user_id):
        try:
            wishlists = get_wishlists_by_user(user_id)
            return Response(wishlists, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"errors": str(e)}, status=status.HTTP_404_NOT_FOUND)