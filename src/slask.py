import yaml
import random


def test(name):
    for i in range(10):
        print(f"Jello {name}")
        yaml.dump(name)
        print(f"Random Number: {random.randint(1, 10)}")


test("Name")
