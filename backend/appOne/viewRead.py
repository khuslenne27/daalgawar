from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from backend.settings import sendResponse, connectDB, disconnectDB


@csrf_exempt
def get_ideas(request):
    if request.method != 'GET':
        return JsonResponse(
            sendResponse("get_ideas", 1, {"error": "Method not allowed"}),
            status=405
        )

    conn = None
    cur = None

    try:
        conn = connectDB()
        cur = conn.cursor()

        cur.execute("SELECT * FROM ideas ORDER BY id ASC")
        rows = cur.fetchall()

        data = []
        for row in rows:
            idea = {
                "id": row[0],
                "title": row[1],
                "category": row[2],
                "description": row[3]
            }
            data.append(idea)

        return JsonResponse(sendResponse("get_ideas", 0, data), safe=False)

    except Exception as e:
        return JsonResponse(
            sendResponse("get_ideas", 1, {"error": str(e)}),
            status=500
        )

    finally:
        if cur:
            cur.close()
        if conn:
            disconnectDB(conn)