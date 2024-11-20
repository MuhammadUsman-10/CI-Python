from fastapi import FastAPI
from menu_data import menu
app = FastAPI()
@app.get("/")
def read_root():
    return{"Hello" : "World"};

@app.get("/menu")
def get_menu():
    return{
        "data": menu
}

@app.get("/menu/{dish_id}")
def get_dish(dish_id:int):
    for dish in menu:
        if dish["id"]==dish_id:
            return{
                "data": dish
        }

@app.post("/menu")
def create_dish(dish: dict):
    dish_count=len(menu)
    new_dish= {
        "id":dish_count + 1,
        "name":dish["name"],
        "price":dish["price"],
        "category":dish["category"]
    }
    menu.append(new_dish)
    return{ "data": dish}

@app.delete("/menu/{dish_id}")
def delete_dish(dish_id: int):
    for dish in menu:
        if dish["id"] == dish_id:
            menu.remove(dish)
            return {"message": f"Dish with id {dish_id} has been deleted"}
    return {"error": "Dish not found"}

@app.put("/menu/{dish_id}")
def update_dish(dish_id: int, updated_dish: dict):
    for dish in menu:
        if dish["id"] == dish_id:
            dish["price"] = updated_dish.get("price", dish["price"])
            return {"data": dish}
    return {"error": "Dish not found"}
