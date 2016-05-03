# This program express an integer in binary

def tobinary(number):
    binary = ""
    on = "1"
    off = "0"
    while number > 0:
        if number % 2 == 0:
            binary = off + binary
            number //= 2
        else:
            binary = on + binary
            number //= 2
    print(binary)

def main():
    number = int(input("Enter a integer: "))
    tobinary(number)
main()
