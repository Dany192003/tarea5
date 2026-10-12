from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"mensaje": "API corriendo en EC2", "curso": "MIA"}

@app.get("/saludo/{nombre}")
def saludo(nombre: str):
    return {"saludo": f"Hola {nombre}"}