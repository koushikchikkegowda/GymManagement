from rest_framework import status, exceptions
from django.http import HttpResponse
from rest_framework.authentication import get_authorization_header, BaseAuthentication
from django.contrib.auth.models import User
import jwt
import json
from rest_framework.response import Response
from rest_framework import HTTP_HEADER_ENCODING, exceptions

class UserTokenAuthentication(BaseAuthentication):
    model = None

    def get_model(self):
        return User

    def authenticate(self, request):
        auth = get_authorization_header(request).split()
        print(auth)
        if not auth or auth[0].lower() != b'token':
            return None

        if len(auth) == 1:
            msg = 'Invalid token header. No credentials provided.'
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = 'Invalid token header'
            raise exceptions.AuthenticationFailed(msg)

        try:
            token = auth[1]
            if token == "null":
                msg = 'Null token not allowed'
                raise exceptions.AuthenticationFailed(msg)
        except UnicodeError:
            msg = 'Invalid token header. Token string should not contain invalid characters.'
            raise exceptions.AuthenticationFailed(msg)


        return self.authenticate_credentials(token)

    def authenticate_credentials(self, token):
        model = self.get_model()

        try:
            payload = jwt.decode(token, "SECRET")
            username = payload['username']
            id = payload['id']
        except:
            raise exceptions.AuthenticationFailed('Token has expired')

        msg = {'Error': "Token mismatch", 'status': "401"}
        try:

            user = User.objects.get(
                username=username,
                id=id,

            )

            if not user:
                raise exceptions.AuthenticationFailed(msg)

        except jwt.ExpiredSignature or jwt.DecodeError or jwt.InvalidTokenError:
            return Response({'Error': "Token is invalid"}, status="403")
        except Customer.DoesNotExist:
            return Response({'Error': "Internal server error"}, status="200")
        except Exception as e:
            return Response({'Error': "Token is invalid"}, status="403")

        return (user, token)

    def authenticate_header(self, request):
        return 'Token'