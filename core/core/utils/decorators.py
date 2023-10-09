from typing import Any
from rest_framework import status
from rest_framework.response import Response

class AdminOnly(object):
    '''Check if user is Admin'''

    def __init__(self, original_method):
        self.original_method = original_method
    
    def __call__(self, request, *args: Any, **kwargs: Any) -> Any:
        if (request.user.is_authenticated) and (request.user.role == "TESTER"):
            return self.original_method(request, *args, **kwargs)
        else:
            return Response({
                "message": "Access Denied!"
            }, status=status.HTTP_403_FORBIDDEN)
