"""
Module defining the Camion class.
"""

from vehicules.vehicule import Vehicule


class Camion(Vehicule):
    """
    Represents a truck.
    """

    def cout_entretien_annuel(self) -> float:
        """
        Maintenance cost formula for a truck.
        """
        age = self._annee - 2000
        return 1000 + (50 * age)