L = 0


class LED:
    def __init__(self, x1, y1, x2, y2):
        self.S1 = [x1, y1]
        self.S2 = [x2, y2]
        self.position = [x1, y2, L-x2]


class screen:
    # assuming screen is "dist" away from the x-y plane
    def __init__(self, dist):
        self.dist = dist

    def calcAimPoint(self, LED1, LED2):
        LED1.position = 
