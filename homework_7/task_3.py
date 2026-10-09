"""
Создайте программу, имитирующую работу клиники. Создайте базовый
класс Doctor с методом treat(). От него создайте три дочерних класса:
Surgeon, Dentist и Therapist. В каждом дочернем классе
переопределите метод treat(), чтобы каждый врач выводил сообщение
о своём способе лечения.
"""
from abc import ABC, abstractmethod


class Doctor(ABC):
    @abstractmethod
    def treat(self):
        print("Я доктор")


class Surgeon(Doctor):
    def treat(self):
        print("Ложитесь на стол и считайте до 10")


class Dentist(Doctor):
    def treat(self):
        print("Я лечу зубы")


class Therapist(Doctor):
    def treat(self):
        print("Я врач ОБП и лучше не болейте")


surgeon = Surgeon()
surgeon.treat()

dentist = Dentist()
dentist.treat()

therapist = Therapist()
therapist.treat()
