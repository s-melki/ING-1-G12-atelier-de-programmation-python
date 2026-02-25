"""
Module defining the Voiture class.
"""

from vehicules.vehicule import Vehicule


class Voiture(Vehicule):
    """
    Represents a car.
    """

    def cout_entretien_annuel(self) -> float:
        """
        Maintenance cost formula for a car.
        """
        age = self._annee - 2000
        return 500 + (20 * age)