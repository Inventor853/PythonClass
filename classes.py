class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)
    
flight = Flight(3)

passengers = ["Harry", "Hermione", "Ron", "Ginnie"]

for people in passengers:
    if flight.add_passenger(people):
        print("Success")
    else:
        print("No more seats")

print(flight.capacity)
print(flight.passengers)