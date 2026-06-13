from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.matcher_routes import router as matcher_router

app = FastAPI(title="Resume JD Matcher API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(matcher_router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Resume JD Matcher backend is running"}
