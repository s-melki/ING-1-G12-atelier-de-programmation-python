# Vehicle Management System

## Description

This project demonstrates Object-Oriented Programming (OOP) principles in Python:

- Abstraction
- Encapsulation
- Inheritance
- Polymorphism

The system models different types of vehicles and calculates their annual maintenance cost.

---

## Project Structure

vehicule_project/
│
├── main.py
├── README.md
└── vehicules/
    ├── Vehicule.py
    ├── voiture.py
    ├── moto.py
    └── camion.py

---

## OOP Concepts Used

### 1. Abstraction
The `Vehicule` class is abstract and defines the method:
- `cout_entretien_annuel()`

### 2. Encapsulation
- Private attributes: `__marque`, `__modele`
- Protected attribute: `_annee`

### 3. Inheritance
- `Voiture`, `Moto`, and `Camion` inherit from `Vehicule`.

### 4. Polymorphism
Each subclass implements its own version of:
- `cout_entretien_annuel()`

---

## How to Run

```bash
python main.py