"""
Module defining the abstract base class Vehicule.
"""

from abc import ABC, abstractmethod


class Vehicule(ABC):
    """
    Abstract base class representing a generic vehicle.
    """

    def __init__(self, marque: str, modele: str, annee: int) -> None:
        """
        Initialize a vehicle.

        :param marque: Brand of the vehicle
        :param modele: Model of the vehicle
        :param annee: Manufacturing year
        """
        self.__marque = marque
        self.__modele = modele
        self._annee = annee  # Protected: accessible in subclasses

    @abstractmethod
    def cout_entretien_annuel(self) -> float:
        """
        Calculate the annual maintenance cost.
        Must be implemented by subclasses.
        """
        pass

    def get_info(self) -> str:
        """
        Return formatted vehicle information.
        """
        return f"{self.__marque} {self.__modele} ({self._annee})"