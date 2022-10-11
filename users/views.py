from django.shortcuts import render
from djoser.views import TokenCreateView

# Create your views here.
class CustomLoginView(TokenCreateView):
    def post(self, request, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if not serializer.is_valid():
            print(serializer.errors)
        
        return self._action(serializer)