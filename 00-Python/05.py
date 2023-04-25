import sys

if len(sys.argv) != 4:
    print("[!] Fehler")
    sys.exit(1)

_, func, num1, num2 = sys.argv

try:
    num1 = int(num1)
    num2 = int(num2)
    if func == "add":
        print(num1 + num2)
    elif func == "sub":
        print(num1 - num2)
    elif func == "mul":
        print(num1 * num2)
    else:
        raise Exception("Unbekannte Funktion")

except Exception as e:
    print("[!] Fehler: " + str(e))
    sys.exit(1)
