from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from problems.court_officers.Fines import SickOfFinesProblem
from problems.housing import Elevator, Entrance, Water
from problems.housing import BaseHousingProblem
from problems.housing.Elevator import ElevatorStuck, ElevatorOutOfOrder
from problems.housing.Entrance import OutOfIllumination
from problems.housing.Water import NoHotWaterProblem, WaterQualityProblem, WaterPressureProblem, NoWaterProblem

mapping_cases = {
    ('застревает лифт', 'лифт', 'часто застревает лифт'): ElevatorStuck,
    ('не работает лифт', 'лифт', 'не работает'): ElevatorOutOfOrder,
    ('темно в подъезде', 'нет света в подъезде', 'нет света в подъезде', 'украли лампочку', 'темно в подьезде',
     'подьезде', 'подъезд', 'подьезд', 'парадная', 'парадной'): OutOfIllumination,
    ('штрафы', 'штраф'): SickOfFinesProblem,
    ('нет горячей воды', 'горячая вода', 'вода'): NoHotWaterProblem,
    ('слабый напор', 'напор', 'давление', 'вода'): WaterPressureProblem,
    ('нет воды', 'вода'): NoWaterProblem,
    ('качество воды', 'ржавчина', 'ржавая вода', 'грязная вода', 'грязь в воде', 'песок в воде',
     'ржавчина', 'вода'): WaterQualityProblem

}

MAPPING = {
    'ЖКХ': [ElevatorOutOfOrder,
            ElevatorStuck,
            OutOfIllumination,
            NoHotWaterProblem,
            NoWaterProblem,
            WaterPressureProblem,
            NoHotWaterProblem,
            WaterQualityProblem],
    'ФССП': [SickOfFinesProblem]
}

serialized_mapping = list()
for type in MAPPING:
    serialized_mapping.append(type)

all_subtypes = list()
for type_list in serialized_mapping:
    for type in MAPPING[type_list]:
        all_subtypes.append(type.name)
all_subtypes_regex = '|'.join(all_subtypes)


def process_search(text: str):
    kb_layout = ReplyKeyboardMarkup(one_time_keyboard=True)
    for mapping_case in mapping_cases:
        if text.lower() in mapping_case:
            name = mapping_cases[mapping_case].name
            kb_layout.add(KeyboardButton(name))
    return kb_layout
