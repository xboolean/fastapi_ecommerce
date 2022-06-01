from abc import ABC, abstractmethod

class BaseRepository(ABC):
    def __init__(self, session):
        self.session = session

    @abstractmethod
    def add(self):
        raise NotImplementedError()

    @abstractmethod
    def get(self):
        raise NotImplementedError()

    @abstractmethod
    def list(self, obj):
        raise NotImplementedError()