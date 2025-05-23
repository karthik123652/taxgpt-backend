from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from apps.chat.route import router as chat_router
from constants import SERVER_URL, PORT, ENV

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

app = FastAPI(lifespan=lifespan)


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/test')
async def test_endpoint():
    """Endpoint for basic API health check"""
    return {
        "status": "success",
        "message": "API is working!",
        "endpoints": {
            "chat_advice": "/chat/advice (POST)",
            "root": "/ (GET)"
        }
    }

@app.get('/')
async def root():
    return {"message": "Server is running"}

app.include_router(chat_router, prefix="/chat", tags=["calculate"])


if __name__ == "__main__":
    uvicorn.run("main:app", host=SERVER_URL, port=int(PORT), reload=(ENV == "dev"))