from django.http import HttpResponseForbidden

from .models import User


class proxyPortalMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get the value of the Authorization header
        token = request.headers.get("Proxy-Token", None)

        user = User.objects.filter(proxy_token=token)
        if not user.exists():
            return HttpResponseForbidden("Invalid token")

        # Token is valid, allow the request to proceed
        request.user = user.first()
        response = self.get_response(request)
        return response
