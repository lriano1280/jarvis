from fastapi import FastAPI

app = FastAPI()

@app.get("/hola")
def hola(nombre: str = "mundo"):
    return {"mensaje": f"hola {nombre}"}


@app.get("/salud")
def salud():
    return {"estado": "ok"}
