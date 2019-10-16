import time
from random import randint
import logging

logging.basicConfig(filename='machine.log', filemode='w')
logger = logging.getLogger("(bleveque)")
logging.root.setLevel(logging.NOTSET)

def log(func):
    """This decorator prints the execution time for the decorated function."""
    def timed(*args, **kwargs):
        ts = time.time()
        result = func(*args, **kwargs)
        te = time.time()
        exectime = te - ts
        if (exectime < 1):
            exectime = str(round(exectime * 100, 3)) +" ms"
        else:
            exectime = str(round(exectime, 3)) + " s"
        logger.info("Running: "+ func.__name__ + "      [ exec-time = " + exectime + " ]")
        return result
        
    return timed


class CoffeeMachine():
    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False
    
    @log
    def boil_water(self):
        return "boiling..."
    
    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level

if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    
    machine.make_coffee()
    machine.add_water(70)