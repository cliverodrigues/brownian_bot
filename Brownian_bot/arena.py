class Arena:
    def __init__(self, width=500, height=500):
        self.width = width
        self.height = height

    def in_bounds(self, x, y):
        return 0 <= x <= self.width and 0 <= y <= self.height
