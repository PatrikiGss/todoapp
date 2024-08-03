from rest_framework import status # type: ignore
from rest_framework.views import APIView# type: ignore
from rest_framework.response import Response# type: ignore
from rest_framework.permissions import IsAuthenticated# type: ignore
from django.contrib.auth import authenticate, login, logout# type: ignore
from django.contrib.auth.models import User# type: ignore
from django.contrib.auth.forms import PasswordChangeForm# type: ignore
from .models import UserProfile
from .serializers import UserSerializer, UserProfileSerializer

class AddUserAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(request.data.get('password'))
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class UserLogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)

class UserChangePasswordAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        form = PasswordChangeForm(user=request.user, data=request.data)
        if form.is_valid():
            form.save()
            request.session.save()
            return Response({'message': 'Password changed successfully'}, status=status.HTTP_200_OK)
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

class AddUserProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self):
        try:
            return UserProfile.objects.get(user=self.request.user)
        except UserProfile.DoesNotExist:
            return None

    def post(self, request):
        profile = self.get_object()
        serializer = UserProfileSerializer(data=request.data, instance=profile)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        profile = self.get_object()
        serializer = UserProfileSerializer(instance=profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListUserProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            profile = UserProfile.objects.get(user=request.user)
            serializer = UserProfileSerializer(profile)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except UserProfile.DoesNotExist:
            return Response({'error': 'User profile not found'}, status=status.HTTP_404_NOT_FOUND)

class ChangeUserProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, username):
        try:
            return UserProfile.objects.get(user__username=username)
        except UserProfile.DoesNotExist:
            return None

    def put(self, request, username):
        profile = self.get_object(username)
        serializer = UserProfileSerializer(instance=profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ChangeUserInformationAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, username):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            return None

    def put(self, request, username):
        user = self.get_object(username)
        serializer = UserSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
