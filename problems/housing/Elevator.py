from problems.BaseProblem import BaseProblem
from problems.housing import BaseHousingProblem


class ElevatorStuck(BaseHousingProblem):
    name = 'Застревает лифт'


class ElevatorOutOfOrder(BaseHousingProblem):
    name = 'Не работает лифт'
