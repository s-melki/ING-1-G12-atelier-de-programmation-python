"""
Module defining the Moto class.
"""

from vehicules.Vehicule import Vehicule


class Moto(Vehicule):
    """
    Represents a motorcycle.
    """

    def cout_entretien_annuel(self) -> float:
        """
        Maintenance cost formula for a motorcycle.
        """
        age = self._annee - 2000
        return 300 + (10 * age)