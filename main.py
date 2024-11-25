from fastapi import FastAPI
import uvicorn
from app.api.v1.endpoints.login import router as api_router
from app.api.v1.endpoints.registration import router as reg_api_router

app = FastAPI()

app.include_router(api_router, prefix="/api/v1")
app.include_router(reg_api_router, prefix="/api/v1")

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)