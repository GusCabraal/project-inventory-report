from abc import ABC, abstractmethod


class Importer(ABC):
    @abstractmethod
    def get_data(self):
        raise NotImplementedError

    @abstractmethod
    def import_data(self):
        raise NotImplementedError
