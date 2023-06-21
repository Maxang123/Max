import math
class rectangularCoordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def get_coordinates(self):
        return (self.x, self.y)
    
    def is_on_x_axis(self):
        return self.y == 0
    
    def is_on_y_axis(self):
        return self.x == 0
    
    def get_quadrant(self):
        if self.x > 0 and self.y > 0:
            return 1
        elif self.x < 0 and self.y > 0:
            return 2
        elif self.x < 0 and self.y < 0:
            return 3
        elif self.x > 0 and self.y < 0:
            return 4
        else:
            return None
    
    def distance_from_x_axis(self):
        return abs(self.y)
    
    def distance_from_y_axis(self):
        return abs(self.x)
    
    def distance_from_origin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5
    
    def midpoint_between_points(self, a, b):
        midpoint_x = (self.x + a) / 2
        midpoint_y = (self.y + b) / 2
        return (midpoint_x, midpoint_y)
    
    def distance_to_point(self, a, b):
        distance = ((a - self.x) ** 2 + (b - self.y) ** 2) ** 0.5
        return distance
    
    def angle_with_x_axis(self):
        import math
        angle = math.degrees(math.atan2(self.y, self.x))
        return angle
