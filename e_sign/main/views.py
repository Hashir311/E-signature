from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import base64
from io import BytesIO
from django.http import JsonResponse
from django.shortcuts import render
from django.core.files.base import ContentFile
from PIL import Image
import json
from .models import Drawing


@login_required(login_url="accounts:login")
def dashboard(request):
    return render(request, "main/dashboard.html")


@login_required(login_url="accounts:login")
def canvas(request):
    return render(request, "main/canvas.html")


@login_required(login_url="accounts:login")
def save(request):
    if request.method == "POST":
        data = json.loads(request.body)
        image_data = data.get("image")
        file_name = data.get("file_name")
        print("file recieved")

        if image_data:
            print("image data received")
            format, imgstr = image_data.split(";base64,")
            img_data = base64.b64decode(imgstr)
            image = Image.open(BytesIO(img_data))
            image_name = f"{file_name}.png"
            image_path = f"drawings/{image_name}"
            drawing_file = ContentFile(img_data, name=image_name)
            drawing = Drawing(user=request.user, name=file_name, image=drawing_file)
            drawing.save()
            print("image saved")
            return JsonResponse(
                {"message": "Image saved successfully!", "drawing_id": drawing.id}
            )

        return JsonResponse({"message": "No image data received."}, status=400)

    return JsonResponse({"message": "Invalid request method."}, status=400)


@login_required(login_url="accounts:login")
def view_saved(request):
    drawings = Drawing.objects.filter(user=request.user)
    return render(request, "main/view_saved.html", {"drawings": drawings})
