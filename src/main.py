from datetime import date
from utils import add, subtract, multiply, divide

print("Name: Mahi")
print("Today's Date:", date.today())

try:
    print("Addition:", add(10, 5))
    print("Subtraction:", subtract(10, 5))
    print("Multiplication:", multiply(10, 5))
    print("Division:", divide(10, 5))

except Exception as error:
    print("An error occurred:", error)