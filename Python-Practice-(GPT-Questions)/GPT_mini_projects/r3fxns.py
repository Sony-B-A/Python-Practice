# 🌟 MINI PROJECT 1 — Temperature Converter (Functions Only)
def c2f(temp):
    f = (temp * (9/5)) + 32
    print(f"{temp}°C converted to farenheit is: {f}°F")

def f2c(temp):
    return (temp - 32) * (5/9)
    pass

while True:
    print("1.Celsius to Farenheit\n2.Farenheit to Celsius\n0.Exit")
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            temp = float (input("Enter Temperature in celsius: "))
            c2f(temp)
        case 2:
            temp = float (input("Enter Temperature in farenheit: "))
            print(f"{temp}°F converted to celsius is: {f2c(temp)}°C")
        case 0:
            print("Exiting, bye baay")
            break
        case _:print("Invalid choice!!")


