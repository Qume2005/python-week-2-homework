from lib import *

def exercise1():
    score_list = score_list = [51, 71, 76, 81, 46, 67, 58];
    total = Exercise1.total(score_list);
    average_score = Exercise1.average_score(score_list)
    pass_rate = Exercise1.pass_rate(score_list)
    print("分数总和:", total, "\n")
    print("平均分:", average_score, "\n")
    print("及格率:", pass_rate, "\n")

def exercise2():
    amount_of_dollar = Exercise2.exchange(10000, Exercise2.ExchangeRate.Dollar)
    amount_of_gbp = Exercise2.exchange(10000, Exercise2.ExchangeRate.GBP)
    amount_of_eur = Exercise2.exchange(10000, Exercise2.ExchangeRate.EUR)
    amount_of_aud = Exercise2.exchange(10000, Exercise2.ExchangeRate.AUD)
    print("换算美元:", amount_of_dollar, "\n")
    print("换算英镑:", amount_of_gbp, "\n")
    print("换算欧元:", amount_of_eur, "\n")
    print("换算澳元:", amount_of_aud, "\n")

def exercise3():
    result = Exercise3.which_is_bigger()
    print("最大的是:", result)

def exercise4():
    (result1, result2) = Exercise4.solving_equations(-8, -2, 1)
    print("计算结果: ", "\n")
    print("x1:", result1, "\n")
    print("x2:", result2, "\n")

def exercise5():
    tax = Exercise5.tax_payable(6000, 3500, 0.1, 105)
    print("应缴税额:", tax)