from problems.housing import BaseHousingProblem


class NoWaterProblem(BaseHousingProblem):
    name = 'Нет воды'


class WaterQualityProblem(BaseHousingProblem):
    name = 'Качество воды'


class NoHotWaterProblem(BaseHousingProblem):
    name = 'Нет горячей воды'


class WaterPressureProblem(BaseHousingProblem):
    name = 'Слабый напор'
