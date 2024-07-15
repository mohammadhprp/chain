from abc import ABC, abstractmethod

from typing import Dict

class Serializable(ABC):
    """
    Abstract base class for objects that can be serialized to a dictionary.

    Requires subclasses to implement a `to_dict` method.
    """

    @abstractmethod
    def to_dict(self) -> Dict:
        """
        Convert the object to a dictionary representation.

        Returns:
            dict: A dictionary representation of the object.
        """
        pass
