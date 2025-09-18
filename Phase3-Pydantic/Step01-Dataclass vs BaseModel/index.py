# Base Model
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    age: int

# ✅ Correct input
u1 = User(id=1, name="CodeQueen", age=22)
print(u1)

# ❌ Wrong type (age as string instead of int)
try:
    u2 = User(id=2, name="Sumbal", age="twenty")
except Exception as e:
    print("Error:", e)


#Dataclass 
from pydantic.dataclasses import dataclass

@dataclass
class Product:
    id: int
    name: str
    price: float

# ✅ Correct input
p1 = Product(1, "Laptop", 1500.50)
print(p1)

# ❌ Wrong type (price as string instead of float)
try:
    p2 = Product(2, "Mouse", "cheap")
except Exception as e:
    print("Error:", e)



# @Dataclass
from dataclasses import dataclass

@dataclass
class Student:
    id: int
    name: str
    marks: float

# ✅ Correct input (Python doesn't check types automatically)
s1 = Student(1, "CodeQueen", 88.5)
print(s1)

# ❌ Wrong type (marks as string instead of float)
s2 = Student(2, "Sumbal", "ninety")
print(s2)
