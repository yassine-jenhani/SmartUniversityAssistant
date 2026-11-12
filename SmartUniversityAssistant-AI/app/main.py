from fastapi import FastAPI
from app.api.chat import router

app = FastAPI(
    title="SmartUniversityAssistant AI",
    description="AI services for SmartUniversityAssistant",
    version="1.0.0"
)

app.include_router(
    router,
    prefix="/api/ai",
    tags=["AI Chat"]
)


@app.get("/api/ai/health")
def health_check():
    return {
        "status": "healthy",
        "service": "SmartUniversityAssistant AI"
    }