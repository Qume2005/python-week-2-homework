from enum import Enum
from math import cos, sin, sqrt

class Exercise1:
    def __init__(self) -> None:
        score_list = score_list = [51, 71, 76, 81, 46, 67, 58];
        total = Exercise1.total(score_list);
        average_score = Exercise1.average_score(score_list)
        pass_rate = Exercise1.pass_rate(score_list)
        print("分数总和:", total, "\n")
        print("平均分:", average_score, "\n")
        print("及格率:", pass_rate, "\n")
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
    def __init__(self) -> None:
        amount_of_dollar = Exercise2.exchange(10000, Exercise2.ExchangeRate.Dollar)
        amount_of_gbp = Exercise2.exchange(10000, Exercise2.ExchangeRate.GBP)
        amount_of_eur = Exercise2.exchange(10000, Exercise2.ExchangeRate.EUR)
        amount_of_aud = Exercise2.exchange(10000, Exercise2.ExchangeRate.AUD)
        print("换算美元:", amount_of_dollar, "\n")
        print("换算英镑:", amount_of_gbp, "\n")
        print("换算欧元:", amount_of_eur, "\n")
        print("换算澳元:", amount_of_aud, "\n")
    class ExchangeRate(Enum):
        Dollar = 7.00
        GBP = 8.55
        EUR = 7.78
        AUD = 4.24
    
    @staticmethod
    def exchange(amount: float, foreign_exchange: ExchangeRate):
        return round(amount / foreign_exchange.value, 2)

class Exercise3:
    def __init__(self) -> None:
        result = Exercise3.which_is_bigger()
        print("最大的是:", result)
    @staticmethod
    def which_is_bigger() -> str:
        return "COS(365)" if cos(365) >= sin(365)  else "SIN(365)"

class Exercise4:
    def __init__(self) -> None:
        (result1, result2) = Exercise4.solving_equations(-8, -2, 1)
        print("计算结果: ", "\n")
        print("x1:", result1, "\n")
        print("x2:", result2, "\n")
    @staticmethod
    def solving_equations(constant_term: float, linear_term: float, squared_term: float) -> tuple[float, float]:
        return (
            (-linear_term + sqrt(linear_term**2 - squared_term * constant_term * 4)) / (squared_term * 2), 
            (-linear_term - sqrt(linear_term**2 - squared_term * constant_term * 4)) / (squared_term * 2)
        )

class Exercise5:
    def __init__(self) -> None:
        tax = Exercise5.tax_payable(6000, 3500, 0.1, 105)
        print("应缴税额:", tax)
    @staticmethod
    def tax_payable(salary: float, tax_hreshold: float, tax_rate: float, quick_deduction: float) -> float:
        return (salary - tax_hreshold) * tax_rate - quick_deduction
    
    