from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def ref_root():
    a = 20
    b = 30
    return( a+ b)