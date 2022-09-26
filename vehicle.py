class Vehicle():
    """The Vehicle class represents the vehicle which will be used to ship/deliver an
    order. It will be of two types: 1. Bike and 2. Truck. The bike has only 10 unit of capacity. The
    truck has only 100 unit of capacity. suggested attributes : (id , vehicle_no , capacity ,
    current_position , current_status[Free,busy,Not_working] )
    """

def __init__(self, vehicle_no, capacity, current_position, current_status):
    self.vehicle_no = vehicle_no
    self.capacity = capacity
    self.current_position = current_position
    self.current_status = current_status

def get_vehicle_no(self):
    """User has to register himself / herself to use this system."""
    return self.vehicle_no

def set_vehicle_no(self, vehicle_no):
    """User has to register himself / herself to use this system."""
    self.vehicle_no = vehicle_no

def get_capacity(self):
    """User has to register himself / herself to use this system."""
    return self.capacity

def set_capacity(self, capacity):
    """User has to register himself / herself to use this system."""
    self.capacity = capacity

def get_current_position(self):
    """User has to register himself / herself to use this system."""
    return self.current_position

def set_current_position(self, current_position):
    """User has to register himself / herself to use this system."""
    self.current_position = current_position

def get_current_status(self):
    """User has to register himself / herself to use this system."""
    return self.current_status

def set_current_status(self, current_status):
    """User has to register himself / herself to use this system."""
    self.current_status = current_status


class Bike(Vehicle):
    """bike has capacity of 10"""
    def __init__(self, vehicle_no):
        super().__init__(vehicle_no, 10, 0, "FREE")


class Truck(Vehicle):
    """truck has capacity of 100"""
    def __init__(self, vehicle_no):
        super().__init__(vehicle_no, 100, 0, "Not_working")
