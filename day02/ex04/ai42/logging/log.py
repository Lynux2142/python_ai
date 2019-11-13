import time
from random import randint
import logging as prout
from getpass import getuser

prout.basicConfig(filename='machine.log', level=prout.INFO, format=f'({getuser()})Running: %(message)s')

class CoffeeMachine():
    water_level = 100
    def start_machine(self):
        begin_time = time.time()
        if self.water_level > 20:
            prout.info(f"{'Start Machine':<16} [ exec-time = {round((time.time() - begin_time) * 1000, 3):0<5} ms ]")
            return True
        else:
            prout.info(f"{'Start Machine':<16} [ exec-time = {round((time.time() - begin_time) * 1000, 3):0<5} ms ]")
            print("Please add water!")
            return False
    def boil_water(self):
        begin_time = time.time()
        prout.info(f"{'Boil Water':<16} [ exec-time = {round((time.time() - begin_time) * 1000, 3):0<5} ms ]")
        return "boiling..."
    def make_coffee(self):
        begin_time = time.time()
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")
            prout.info(f"{'Make Coffee':<16} [ exec-time = {round(time.time() - begin_time, 3):0<5} s  ]")
    def add_water(self, water_level):
        begin_time = time.time()
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")
        prout.info(f"{'Add Water':<16} [ exec-time = {round(time.time() - begin_time, 3):0<5} s  ]")

def main():
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)

if __name__ == "__main__":
    main()
