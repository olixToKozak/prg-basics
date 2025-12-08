# tv.py file
class TV:
    def __init__(self):
        # Początkowy stan telewizora jest wyłączony
        self.is_on = False

    def turn_on(self):
        # Włącza telewizor
        self.is_on = True

    def turn_off(self):
        # Wyłącza telewizor
        self.is_on = False

    def show_status(self):
        # Pokazuje status telewizora
        if self.is_on:
            print("TV is on")
        else:
            print("TV is off")
