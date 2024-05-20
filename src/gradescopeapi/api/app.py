from fastapi import FastAPI

from gradescopeapi.api.routes import auth, course

app = FastAPI()
app.include_router(auth.router)
app.include_router(course.router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
