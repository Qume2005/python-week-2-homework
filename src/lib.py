from enum import Enum
from math import cos, sin, sqrt

class Exercise1:
    @staticmethod
    def total(score_list: list[int]) -> int:
        return sum(score_list)

    @staticmethod
    def average_score(score_list: list[int]) -> float:
        return round(float(Exercise1.total(score_list)) / len(score_list), 2)

    @staticmethod
    def pass_rate(score_list: list[int]) -> float:
        count = sum(1 for score in score_list if score > 60)
        return round(float(count) / len(score_list), 2)

class Exercise2:
    class ExchangeRate(Enum):
        Dollar = 7.00
        GBP = 8.55
        EUR = 7.78
        AUD = 4.24
    
    @staticmethod
    def exchange(amount: float, foreign_exchange: ExchangeRate):
        return round(amount / foreign_exchange.value, 2)

class Exercise3:
    @staticmethod
    def which_is_bigger() -> str:
        return "COS(365)" if cos(365) >= sin(365)  else "SIN(365)"

class Exercise4:
    @staticmethod
    def solving_equations(constant_term: float, linear_term: float, squared_term: float) -> tuple[float, float]:
        return (
            (-linear_term + sqrt(linear_term**2 - squared_term * constant_term * 4)) / (squared_term * 2), 
            (-linear_term - sqrt(linear_term**2 - squared_term * constant_term * 4)) / (squared_term * 2)
        )

class Exercise5:
    @staticmethod
    def tax_payable(salary: float, tax_hreshold: float, tax_rate: float, quick_deduction: float) -> float:
        return (salary - tax_hreshold) * tax_rate - quick_deduction
    
    