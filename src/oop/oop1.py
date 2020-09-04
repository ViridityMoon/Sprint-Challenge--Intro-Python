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
class Vehicle():
    pass

# GroundVehicle and FlightVehicle are both direct subclasses of 
# the base class
class GroundVehicle(Vehicle):
    pass
class FlightVehicle(Vehicle):
    pass

# Car and Motorcycle are both direct subclasses of GroundVehicle
class Car(GroundVehicle):
    pass
class Motorcycle(GroundVehicle):
    pass

# Starship and Airplane are both direct subclasses of
# FlightVehicle
class Starship(FlightVehicle):
    pass
class Airplane(FlightVehicle):
    pass