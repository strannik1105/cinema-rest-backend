from contextlib import asynccontextmanager
from threading import Thread

import uvicorn
import settings
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from router.api import api_router
from services.booking_service.booking_checker import check_bookings

booking_checker_thr = Thread(target=check_bookings, daemon=True)


@asynccontextmanager
async def lifespan(fastapi_app: FastAPI):
    booking_checker_thr.start()
    yield


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="../static"), name="static")

app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run(app=app, host=settings.HOST, port=settings.PORT)
