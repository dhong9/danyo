from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from PIL import Image
import numpy as np
import io

@csrf_exempt
def img_to_excel(request):
    if request.method == "POST" and request.FILES.get("image"):
        try:
            # Read the uploaded image
            image_file = request.FILES["image"]
            image = Image.open(image_file)

            # Ensure the image is in RGB mode
            if image.mode != "RGB":
                image = image.convert("RGB")
            
            # Convery image to a NumPy array
            rgb_array = np.array(image) # Shape: (rows, columns, 3)

            # Convert NumPy array to a Python list for JSON serialization
            rgb_list = rgb_array.tolist()

            # Return the RGB array
            return JsonResponse({"rgb_values": rgb_list})
        
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    
    return JsonResponse({"error": "Invalid request. Please POST an image."}, status=400) 