from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "hellow word"}


# Iniciar el servidor     
# uvicorn main:app --reload