from django.shortcuts import render
from django.http import HttpResponse


def print_hello(request):
    return HttpResponse("Hello, nFactorial school!")


def sum_numbers(request, first: int, second: int):
    result = first + second
    return HttpResponse(f"{first} + {second} = {result}")


def upper_text(request, text: str):
    return HttpResponse(text.upper())


def check_palindrome(request, word: str):
    result = (word == word[::-1])
    return HttpResponse(f"Текст {word} является палиндромом: {result}")


def calculator(request, first: int, operation: str, second:int):
    result = 0.0
    res_operation = ''
    if operation.lower() == 'add':
        result = first + second
        res_operation = '+'
    elif operation.lower() == 'sub':
        result = first - second
        res_operation = '-'
    elif operation.lower() == 'mult':
        if first != 0 and second != 0:
            result = first * second
            res_operation = '*'
        else:
            return HttpResponse("Значение не должен быть равен на 0!")
    elif operation.lower() == 'div':
        if first != 0 and second != 0:
            result = first / second
            res_operation = '/'
        else:
            return HttpResponse("Значение не должен быть равен на 0!")

    return HttpResponse(f"{first}{res_operation}{second} = {result}")
