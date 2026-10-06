from fastapi import FastAPI

app = FastAPI(
    title="BIT Notes LMS API",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "BIT Notes LMS API is running"
    }


@app.get("/api/health")
def health_check():
    return {
        "status": "ok"
    }