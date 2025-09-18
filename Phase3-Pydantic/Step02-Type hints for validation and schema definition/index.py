#🔹 Type hints for Validation
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    age: int

# ✅ Correct data
u1 = User(id=1, name="CodeQueen", age=22)
print(u1)

# ❌ Wrong data type (age should be int but given str)
try:
    u2 = User(id=2, name="Sumbal", age="twenty")
except Exception as e:
    print("Error:", e)


#🔹 Type hints for Schema Definition
from pydantic import BaseModel
from typing import List

class Product(BaseModel):
    id: int
    name: str
    price: float

class Order(BaseModel):
    order_id: int
    products: List[Product]  # List of Product objects
    total: float

# ✅ Correct schema
order = Order(
    order_id=101,
    products=[
        Product(id=1, name="Laptop", price=1500.50),
        Product(id=2, name="Mouse", price=20.99),
    ],
    total=1521.49
)
print(order)

# ❌ Wrong schema (price should be float, given as string)
try:
    bad_order = Order(
        order_id=102,
        products=[Product(id=3, name="Keyboard", price="cheap")],
        total=100.0
    )
except Exception as e:
    print("Error:", e)
