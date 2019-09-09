# bring in string and random
import string
import random

print(string.ascii_uppercase)
print(random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase))
names = set();
class Robot(object):
    def __init__(self):
        if self.name:
            self.reset(self)
        else:
            self.name = self.chooseName(self)
            self.names = set()
            if self.name in self.names:
                self.name = self.chooseName(self)
            else:
                self.names.add(self.name)
        
        print(self.name)

    def chooseName(self):
        letter1 = random.choice(string.ascii_uppercase)
        letter2 = random.choice(string.ascii_uppercase)
        number = str(random.randint(000, 999)
        return f"{letter1}{letter2}{number}"

    def reset(self):
        self.name = self.chooseName()
