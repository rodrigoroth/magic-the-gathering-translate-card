from fastapi import FastAPI
from routers import api_router


app = FastAPI()

if __name__ == "__main__":
    import uvicorn
    app.include_router(api_router)
    uvicorn.run(app, host="0.0.0.0", port=8000)
