#  Q9. Create a Bus child class that inherits from the Vehicle class. The default fare charge of any vehicle should be seating_capacity * 100. If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge. So total fare for bus instance should become the final_amount = total fare + 10% of the total fare. Demonstrate this example using Bus and Vehicle classes and using the concept of method overriding.

class Vehicle:
    def __init__(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def fare(self):
        return self.seating_capacity * 100

class Bus(Vehicle):
    def fare(self):
        # Calculate the base fare using the parent class method
        base_fare = super().fare()
        # Add 10% maintenance charge
        total_fare = base_fare + (0.10 * base_fare)
        return total_fare

# Example usage
# Create an instance of Vehicle
vehicle = Vehicle(50)
print(f"Vehicle fare: {vehicle.fare()}")  # Output: Vehicle fare: 5000

# Create an instance of Bus
bus = Bus(50)
print(f"Bus fare: {bus.fare()}")  # Output: Bus fare: 5500
