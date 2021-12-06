#!/usr/bin/env python3

class Lantern:
    def __init__(self, timer = 8):
        self.timer = timer

    def tick(self):
        self.timer -= 1
        if self.timer < 0:
            self.timer = 6
            return[self, Lantern()]
        else:
            return [self]

    def __repr__(self):
        return str(self.timer)

if __name__ == '__main__':
    f = Lantern()
    for i in range(24):
        print(f)
        f.tick()
