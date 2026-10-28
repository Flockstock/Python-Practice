from fastapi import FastAPI, HTTPException
from models import ItemPayload
app = FastAPI()
@app.get("/")
def root():
    grocery_list: dict[int, ItemPayload] = {}
    return{"message":"Hello World"}

#Routes to add an item
@app.post("/items/{item_name}/{quantity}")
def add_item(item_name: str,quantity: int) :
    if quantity <=0:
        raise HTTPException(status_code=400,detail="Quantity must be greater than 0.")
    # if item already exists, we'll just add the quantity.
    # get all item names
    item_ids = {item.item_name: item.item_id if item.item_id is not None else 0 for item in grocery_list.values()}
    if item_name in items_ids.keys():
