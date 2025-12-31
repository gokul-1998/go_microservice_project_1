import os,requests

def token(request):
    if not "Authorization" in request.headers:
        return None,("Missing credentials",401)
    tokne=request.headers["Authorization"]
    if not token:
        return None,("Missing credentials",401)
    response=requests.post(f"http://{os.getenv('AUTH_SVC_ADDRESS')}/validate",headers={"Authorization":token})

    if response.status_code ==200:
        return response.txt,None
    else:
        return None,(response.txt,response.status_code)