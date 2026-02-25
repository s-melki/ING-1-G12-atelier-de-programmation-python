"""
Main entry point of the application.
"""

from vehicules.voiture import Voiture
from vehicules.moto import Moto
from vehicules.camion import Camion


def main() -> None:
    """
    Create vehicle instances and display maintenance costs.
    """
    vehicules = [
        Voiture("BMW", "Serie 3", 2020),
        Moto("Harley-Davidson", "Sportster 1000", 1977),
        Camion("Mack Trucks", "MH UltraLiner", 1982),
    ]

    for vehicule in vehicules:
        print(
            f"{vehicule.get_info()} -> "
            f"{vehicule.cout_entretien_annuel()} €"
        )


if __name__ == "__main__":
    main()