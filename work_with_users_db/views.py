import django.shortcuts
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from work_with_users_db.models import User_db, Castomer
from work_with_users_db.serializers import User_serializer, CastomerSerializer


class UsersView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            user = get_object_or_404(User_db.objects.all(), pk=pk)
            serializer = User_serializer(user)
            return Response({'users': serializer.data})

        user = User_db.objects.values()
        serializer_class = User_serializer(user, many=True)
        return Response({'users': serializer_class.data})

    def post(self, request):
        user = request.data.get('user')
        serializer = User_serializer(data=user)
        if serializer.is_valid(raise_exception=True):
            user_saved = serializer.save()
        return Response({'success': f"User {user_saved.name} saved"})

    def put(self, request, pk):
        saved_user = get_object_or_404(User_db.objects.all(), pk=pk)
        data = request.data.get('user')
        serializer = User_serializer(instance=saved_user, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            user_saved = serializer.save()
        return Response({'success': f"User {user_saved.name} updated"})

    def delete(self, request, pk):
        delete_user = get_object_or_404(User_db.objects.all(), pk=pk)
        delete_user.delete()
        return Response({'success': f"User {pk} deleted"}, status=204)


class CastomerView(APIView):
    def get(self, request):
        cast = Castomer.objects.values()
        serializer = CastomerSerializer(cast, many=True)
        return Response({'castomer': serializer.data})

    def post(self, request):
        cast = request.data.get('castomer')
        serializer = CastomerSerializer(data=cast)
        if serializer.is_valid(raise_exception=True):
            castomer_saved = serializer.save()
        return Response({'success': f"Castomer {castomer_saved.name} saved"})
