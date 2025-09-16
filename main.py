from fastapi import FastAPI
import os
import platform

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Environment Checker dev API is running"}
@app.get("/env")
async def check_environment():
    return {
        "status": "ok",
        "environment": {
            "platform": platform.platform(),
            "python_version": platform.python_version(),
            "hostname": platform.node(),
            "env_vars": os.getenv('ENVIRONMENT')
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)