class Vehicle:
    license_plate = None,
    speed = 0,
    color = None,
    vehicle_type = None,
    image = None,
    direction= None

    def __init__(self, speed, color,image,direction, vehicle_type=None, license_plate=None):
        self.color = color
        self.speed = speed
        self.vehicle_type = vehicle_type
        self.license_plate = license_plate
        self.image = image
        self.direction = direction
