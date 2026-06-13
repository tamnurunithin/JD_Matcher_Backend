import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.matcher_routes import router as matcher_router

app = FastAPI(title="Resume JD Matcher API")

frontend_url = os.getenv("FRONTEND_URL", "http://localhost:3000")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        frontend_url,
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(matcher_router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Resume JD Matcher backend is running"}