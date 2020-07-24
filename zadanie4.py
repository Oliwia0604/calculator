import logging
logging.basicConfig(level=logging.INFO)

def calculator(x, y, z, result):
    x = int(input("Podaj skladnik 1:"))
    y = int(input("Podaj skladnik 2:"))
    z = input("Podaj działanie posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:")
    operators = {"1": x+y, "2": x-y, "3": x*y, "4": x/y}
    if operators == "1":
       print(operators["Dodaje"])
    elif operators == "2":
       print(operators["Odejmuje"])
    elif operators == "3":
       print(operators["Mnoże"])
    elif operators == "4":
       print(operators["Dziele"])
       logging.info(calculator)
       logging.info(f"Dodaje {x} i {y}")
       logging.info(f"Odejmuje {x} i {y}") 
       logging.info(f"Mnoże {x} i {y}")
       logging.info(f"Dziele {x} i {y}")
       print(f"Wynik to:" 'Dodaje: {x} + {y} = {}.format(add_result')
       print(f"Wynik to:" 'Odejmuje: {x} - {y} = {}.format(add_result')
       print(f"Wynik to:" 'Mnoże: {x} * {y} = {}.format(add_result')
       print(f"Wynik to:" 'Dziele: {x} / {y} = {}.format(add_result')


#print(f'Wynik to:  ')









 