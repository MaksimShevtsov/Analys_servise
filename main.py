from fastapi import FastAPI
from db.base import database
from fastapi.staticfiles import StaticFiles

from endpionts import users, auth, jobs, home
import uvicorn

app = FastAPI(title="Analys platform")

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(home.router, prefix="/home", tags=['home'])
app.include_router(users.router, prefix="/sign_up", tags=['users'])
app.include_router(auth.router, prefix="/login", tags=["auth"])
app.include_router(jobs.router, prefix="/jobs", tags=["jobs"])


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, host="0.0.0.0", reload=True)
