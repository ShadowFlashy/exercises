from abc import ABC, abstractmethod
import re

class Person:
    
    def __init__(self, id, name, is_a_student):
        self.id = id
        self.name = name
        self.is_a_student = is_a_student
    
    @staticmethod
    def is_valid_name(name):
        if(re.search(' ', name)):
            return True
        else:
            return False
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name (self, new_name):
        if not self.is_valid_name(new_name): raise ValueError
        
        self.__name = new_name

class Residence(ABC):
    def __init__(self, address, area, number_of_rooms):
        self.address = address
        self.area = area
        self.number_of_rooms = number_of_rooms
        self._occupants = {}  # Dictionary to store occupants using their ids as keys

    @property
    def number_of_occupants(self):
        return len(self._occupants)

    @property
    def maximum_occupants(self):
        return min(self.area // 20, self.number_of_rooms * 2)

    def register_resident(self, person):
        if person.id in self._occupants:
            return
        if self.number_of_occupants >= self.maximum_occupants:
            raise RuntimeError("Not enough space for another resident.")
        self._occupants[person.id] = person

    def unregister_resident(self, id):
        if id in self._occupants:
            del self._occupants[id]

    @property
    def resident_names(self):
        return [person.name for person in self._occupants.values()]

    @abstractmethod
    def calculate_value(self):
        pass

class Villa(Residence):
    def __init__(self, address, area, number_of_rooms, garage_capacity):
        super().__init__(address, area, number_of_rooms)
        self.garage_capacity = garage_capacity

    def calculate_value(self):
        return (25000 * self.number_of_rooms) + (2100 * self.area) + (10000 * self.garage_capacity)

class StudentKot(Residence):
    def __init__(self, address, area):
        super().__init__(address, area, number_of_rooms=1)

    def register_resident(self, person):
        if not person.is_student:
            raise RuntimeError("Only students can register in a StudentKot.")
        super().register_resident(person)

    def calculate_value(self):
        return 150000 + (750 * self.area)

# Example Person class for testing
class Person:
    def __init__(self, id, name, is_student=False):
        self.id = id
        self.name = name
        self.is_student = is_student

# Example usage
address = "123 Example St"
area = 100.0
number_of_rooms = 3
garage_capacity = 2

villa = Villa(address, area, number_of_rooms, garage_capacity)
print(villa.calculate_value())  # Should print the value of the villa

student_kot = StudentKot(address, area)
student = Person(1, "John Doe", True)
student_kot.register_resident(student)
print(student_kot.calculate_value())  # Should print the value of the student kot
print(student_kot.resident_names)  # Should print ["John Doe"]
