from django.contrib.auth.models import User
from django.http import JsonResponse
import json

def register(request):
    if request.method == "POST":
        data = json.loads(request.body)

        username = data.get("username")
        password = data.get("password")

        if User.objects.filter(username=username).exists():
            return JsonResponse({"error": "User already exists"}, status=400)

        user = User.objects.create_user(username=username, password=password)

        return JsonResponse({"message": "User created successfully"})