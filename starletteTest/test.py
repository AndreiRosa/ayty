from starlette.applications import Starlette
from starlette.routing import Route
from starlette.responses import FileResponse
from starlette.responses import PlainTextResponse
from starlette.requests import Request
from starlette.responses import Response

app = Starlette(routes=routes)

async def homepage(request):
    return FileResponse("static/style.html")

async def createCall(request):
    return FileResponse("static/createCall.html")

async def createCallPost(request):
    print(request.body)
    return FileResponse("static/style.html")

async def updateCall(request):
    return FileResponse("static/updateCall.html")

async def createEvent(request):
    return FileResponse("static/createEvent.html")

async def createExtension(request):
    return FileResponse("static/createExtension.html")

async def updateExtension(request):
    return FileResponse("static/updateExtension.html")

async def deleteExtension(request):
    return FileResponse("static/deleteExtension.html")

async def specificExtension(request):
    return FileResponse("static/specificExtension.html")

async def allExtension(request):
    return PlainTextResponse('allExtension')

async def callTime(request):
    return FileResponse("static/callTime.html")

async def allCall(request):
    return PlainTextResponse('allCall')

async def extensionEvent(request):
    return FileResponse("static/extensionEvent.html")

routes = [
    Route("/", endpoint=homepage),
    Route("/createcall", endpoint=createCall, methods=['GET']),
    Route("/createcall", endpoint=createCallPost, methods=['POST']),
    Route('/updateCall', endpoint=updateCall),
    Route('/createEvent', endpoint=createEvent),
    Route('/createExtension', endpoint=createExtension),
    Route('/updateExtension', endpoint=updateExtension),
    Route('/deleteExtension', endpoint=deleteExtension),
    Route('/specificExtension', endpoint=specificExtension),
    Route('/allExtension', endpoint=allExtension),
    Route('/callTime', endpoint=callTime),
    Route('/allCall', endpoint=allCall),
    Route('/extensionEvent', endpoint=extensionEvent),
]

