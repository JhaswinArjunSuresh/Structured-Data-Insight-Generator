from fastapi import FastAPI, UploadFile, File
from .profiler import profile_csv
from .insight_generator import generate_insights

app = FastAPI()

@app.post("/profile")
async def profile(file: UploadFile = File(...)):
    contents = await file.read()
    profile_data = profile_csv(contents)
    return {"profile": profile_data}

@app.post("/insights")
async def insights(file: UploadFile = File(...)):
    contents = await file.read()
    profile_data = profile_csv(contents)
    insights_text = generate_insights(profile_data)
    return {
        "profile": profile_data,
        "insights": insights_text
    }

@app.get("/health")
def health_check():
    return {"status": "ok"}

