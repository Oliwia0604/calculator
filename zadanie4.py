import logging
logging.basicConfig(level=logging.INFO)

def calculator():
    x = float(input("Podaj skladnik 1:"))
    y = float(input("Podaj skladnik 2:"))
    operation = input("Podaj działanie posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:")
    
    if operation == "1":
       logging.info(f"Dodaje {x} i {y}")
    elif operation == "2":
       logging.info(f"Odejmuje {x} i {y}")
    elif operation == "3":
       logging.info(f"Mnoze {x} i {y}")
    elif operation == "4":
       logging.info(f"Dziele {x} i {y}")

    try:
       result = get_result(operation, x,y)
    except Exception as exc:
       logging.info(exc)
       return

    print(f"Wynik to {result:.2f}")

def get_result(operation, x,y):
    return {
       "1": x + y,
       "2": x - y,
       "3": x * y,
       "4": x / y,
    }.get(operation, "Operacja nie istnieje!")

   
calculator()













 