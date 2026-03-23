from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from backend.settings import sendResponse, connectDB, disconnectDB

@csrf_exempt
def check_service(request):
    if request.method != 'POST':
        return JsonResponse(sendResponse("check_service", 1, {"error": "Method not allowed"}), status=405)

    try:
        return JsonResponse(sendResponse("check_service", 0, []))
    except Exception as e:
        return JsonResponse(sendResponse("check_service", 1, {"error": str(e)}), status=500)