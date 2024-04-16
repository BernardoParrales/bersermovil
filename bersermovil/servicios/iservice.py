from abc import ABC, abstractmethod

class IService(ABC):
    
    @abstractmethod
    def create(self):
        pass
    
    @abstractmethod
    def read(self):
        pass
    
    @abstractmethod
    def read_all(self):
        pass
    
    @abstractmethod
    def update(self):
        pass
    
    @abstractmethod
    def delete(self):
        pass