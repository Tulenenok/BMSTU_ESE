from dataclasses import dataclass
from math import prod


@dataclass
class FormComplexity:
    low = 1
    middle = 2
    high = 3

@dataclass
class ReportComplexity:
    low = 2
    middle = 5
    high = 8

@dataclass
class ModuleComplexity:
    third_edition = 10


FACTORS = {
    'PREC': [6.20, 4.96, 3.72, 2.48, 1.24, 0],
    'FLEX': [5.07, 4.05, 3.04, 2.03, 1.01, 0],
    'RESL': [7.00, 5.65, 4.24, 2.83, 1.41, 0],
    'TEAM': [5.48, 4.38, 3.29, 2.19, 1.10, 0],
    'PMAT': [7.00, 6.24, 4.68, 1.12, 1.56, 0]
}

PROD = [4, 7, 13, 25, 50]

MULTIPLIERS = {
    'PERS': [1.62, 1.26, 1.00, 0.83, 0.63, 0.50],
    'RCPX': [0.60, 0.83, 1.00, 1.33, 1.91, 2.72],
    'RUSE': [0.95, 1.00, 1.07, 1.15, 1.24],
    'PDIF': [0.87, 1.00, 1.29, 1.81, 2.61],
    'PREX': [1.33, 1.22, 1.00, 0.87, 0.74, 0.62],
    'FCIL': [1.30, 1.10, 1.00, 0.87, 0.73, 0.62],
    'SCED': [1.43, 1.14, 1.00, 1.00, 1.00]
}


def get_factors(indexes: list):
    factors = []
    i = 0

    for key in FACTORS:
        factors.append(FACTORS[key][indexes[i]])
        i += 1

    return factors

def get_p(factors: list):
    return sum(factors) / 100 + 1.01

def get_time(work: float, p: float):
    power = 0.33 + 0.2 * (p - 1.01)
    return 3 * work ** power


def app_composition(salary: float, parameters: dict):
    nop = get_nop(parameters['FORMS'],
                  parameters['REPORTS'],
                  parameters['MODULES'],
                  parameters['RUSE'])
    
    factors = get_factors(parameters['FACTORS'])
    p = get_p(factors)
    
    work = nop / PROD[parameters['PROD']]
    time = get_time(work, p)
    budget = salary * work

    return {'P': p,
            'WORK': round(work, 2), 
            'TIME': round(time, 2), 
            'BUDGET': round(budget, 2)}

def get_nop(forms: list, reports: list, modules: int, ruse: float):
    object_points = (  forms[0] * FormComplexity.low
                     + forms[1] * FormComplexity.middle
                     + forms[2] * FormComplexity.high

                     + reports[0] * ReportComplexity.low
                     + reports[1] * ReportComplexity.middle
                     + reports[2] * ReportComplexity.high

                     + modules * ModuleComplexity.third_edition)

    return object_points * (100 - ruse) / 100


def early_architecture(salary: float, parameters: dict):
    multipliers = get_multipliers(parameters['MULTIPLIERS'])
    earch = prod(multipliers)

    factors = get_factors(parameters['FACTORS'])
    p = get_p(factors)

    work = 2.45 * earch * parameters['LOC'] / 1000 ** p
    time = get_time(work, p)
    budget = salary * work

    return {'P': p,
            'WORK': round(work, 2), 
            'TIME': round(time, 2), 
            'BUDGET': round(budget, 2)}

def get_multipliers(indexes: list):
    multipliers = []
    i = 0

    for key in MULTIPLIERS:
        multipliers.append(MULTIPLIERS[key][indexes[i]])
        i += 1

    return multipliers
