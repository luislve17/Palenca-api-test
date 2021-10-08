from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .serializers import LoginSerializer

class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        # Validating request body structure with serializer
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_credentials = serializer.validated_data

        # Checking unique email
        if user_credentials.get('email') != 'pierre@palenca.com':
            response_obj = {
                'message': 'CREDENTIALS_INVALID',
                'details': 'Incorrect username or password'
                }
            response_code = status.HTTP_401_UNAUTHORIZED

        elif user_credentials.get('password') != 'MyPwdChingon123':
            response_obj = {
                'message': 'CREDENTIALS_INVALID',
                'details': 'Incorrect username or password'
                }
            response_code = status.HTTP_401_UNAUTHORIZED
        else:
            response_obj = {
                'message': 'SUCCESS',
                'access_token': 'cTV0aWFuQ2NqaURGRE82UmZXNVBpdTRxakx3V1F5'
            }
            response_code = status.HTTP_200_OK


        return Response(response_obj, status=response_code)

@api_view(['GET'])
def get_profile(request, token):
    if token != "cTV0aWFuQ2NqaURGRE82UmZXNVBpdTRxakx3V1F5":
        response_obj = {
            'message': 'CREDENTIALS_INVALID',
            'details': 'Incorrect token'
        }
        response_code = status.HTTP_401_UNAUTHORIZED

    else:
        response_obj = {
            "message": "SUCCESS",
            "platform": "uber",
            "profile": {"email": "pierre@palenca.com", "password": "****"}
        }
        response_code = status.HTTP_200_OK
 

    return Response(response_obj, status=response_code)