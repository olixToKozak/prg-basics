from tv import TV  # Importujemy klasę TV z pliku tv.py

def main():
    # Tworzymy obiekt telewizora
    my_tv = TV()

    # Pokażemy status telewizora na początku
    print("Show TV status:")
    my_tv.show_status()  # Na początku TV powinien być wyłączony

    # Włączamy telewizor
    print("Turn TV on:")
    my_tv.turn_on()
    my_tv.show_status()  # Teraz TV powinien być włączony

    # Wyłączamy telewizor
    print("Turn TV off:")
    my_tv.turn_off()
    my_tv.show_status()  # Teraz TV powinien być znów wyłączony

if __name__ == "__main__":
    main()
