import yaml
import random


def test(name):
    # test of stuff
    for i in range(10):
        print(f"Random Number: {random.randint(1, 10)}, Jello {name}")
        test = yaml.dump(name)
        print(test)


test("Name")
