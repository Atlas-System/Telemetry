import dotenv
dotenv.load_dotenv()
import os
from fastapi import FastAPI, Request, HTTPException
import ssl
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware

app = FastAPI()

app.add_middleware(HTTPSRedirectMiddleware)

@app.middleware("http")
async def check_api_key(request: Request, call_next):
    api_key = request.headers.get("X-API-Key")
    if not api_key or api_key != os.getenv("API_KEY"):
        raise HTTPException(status_code=401, detail="Unauthorized")
    response = await call_next(request)
    return response
