# enter your code here to solve the housing assignment
# voer hier je code in om de huisvestingsvraag op te lossen
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
        self.__occupants = {}
    
    
    