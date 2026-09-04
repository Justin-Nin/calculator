name = "Fustin"
print("Hi, my name is " + name + " and I am gay")

text = "fart"
number = 67
decimal = 6.7

print(number)
print(decimal)
print(text)

has_fart = True
print(has_fart)

number = 67
print(10 + (number))
print(int(number))

age: int = 15
Name: str = "Alvino"

print("Name:" + Name + " Age:" + str(age))
print(f"Name:{Name} Age:{age}")

def add (a: float, b: float) -> float:
    print(f'Adding {a} + {b}')
    return a + b

print(add(67, 67))
print(add(6.7, 6.7))

def greet(name: str, greeting: str = "Yo") -> None:
    print(f"{greeting}, {name}!")

greet(input("What is your name? "))

def func(a: int, b: int) -> int:
    print(f' adding a={a} and b={b}')
    return a + b

print(func(5, 10))

def func():
    print("Hello, Fart.")

func()
func()


names: list[str] = ["Alvino", "Justin", "Kaito", "Marv"]

for name in names:
    print(f'Yo whats up, {name}')