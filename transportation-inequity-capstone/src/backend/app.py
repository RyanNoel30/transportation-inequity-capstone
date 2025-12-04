from fastapi import FastAPI
from .app import router as app_router

app = FastAPI(title="Transportation Inequity API")

# include the modular router
app.include_router(app_router)

@app.get("/health")
def health():
    return {"status": "ok"}
