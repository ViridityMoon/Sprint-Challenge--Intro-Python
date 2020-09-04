# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# Base class
class Vehicle(self):
    pass

# GroundVehicle and FlightVehicle are both direct subclasses of 
# the base class
class GroundVehicle(Vehicle, self):
    pass
class FlightVehicle(Vehicle, self):
    pass

# Car and Motorcycle are both direct subclasses of GroundVehicle
class Car(GroundVehicle, self):
    pass
class Motorcycle(GroundVehicle, self):
    pass

# Starship and Airplane are both direct subclasses of
# FlightVehicle
class Starship(FlightVehicle, self):
    pass
class Airplane(FlightVehicle, self):
    pass