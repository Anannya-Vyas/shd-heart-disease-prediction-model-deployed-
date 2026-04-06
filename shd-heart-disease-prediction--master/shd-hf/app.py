from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from openai import OpenAI
import os

app = FastAPI()

# NVIDIA AI API Key
NVIDIA_API_KEY = os.environ.get("NVIDIA_API_KEY", "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")

# Initialize OpenAI client with NVIDIA endpoint
client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=NVIDIA_API_KEY
)

@app.post("/api/analyze")
async def analyze(request: Request):
    if not NVIDIA_API_KEY:
        return JSONResponse({"error": "API key not configured."}, status_code=500)

    body = await request.json()
    prompt = body.get("prompt", "")
    if not prompt:
        return JSONResponse({"error": "No prompt provided."}, status_code=400)

    try:
        # Call NVIDIA API using OpenAI client
        # Note: Gemma 2 doesn't support system role, so we incorporate it into the user message
        system_instruction = "You are a helpful Heart Health AI Assistant. Provide clear, supportive analysis based on user data.\n\n"
        
        completion = client.chat.completions.create(
            model="google/gemma-2-2b-it",
            messages=[
                {"role": "user", "content": system_instruction + prompt}
            ],
            temperature=0.2,
            top_p=0.7,
            max_tokens=1024
        )

        # Extract response text
        text = completion.choices[0].message.content
        return JSONResponse({"result": text})

    except Exception as e:
        error_str = str(e)
        print(f"Error: {error_str}")
        return JSONResponse({"error": f"Error: {error_str}"}, status_code=500)

# Serve the static files (HTML/CSS/JS) from the 'static' folder
# Make sure your index.html is inside a folder named 'static'
app.mount("/", StaticFiles(directory="static", html=True), name="static")