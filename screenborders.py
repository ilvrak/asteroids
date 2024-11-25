class ScreenBorders:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def check_bounds(self, position):
        if position.x < 0:
            position.x = self.width
        elif position.x > self.width:
            position.x = 0

        if position.y < 0:
            position.y = self.height
        elif position.y > self.height:
            position.y = 0

        return position
