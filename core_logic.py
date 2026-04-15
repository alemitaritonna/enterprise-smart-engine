import math

def calculate_compound_interest(principal, rate, time):
    """
    Calcula el interés compuesto según estándares bancarios.
    """
    amount = principal * (pow((1 + rate / 100), time))
    return amount

def validate_credit_score(score):
    """
    Valida la elegibilidad del cliente basado en su scoring crediticio.
    """
    if score > 700:
        return "APROBADO"
    elif score < 700:
        return "RECHAZADO"
    return "PENDIENTE"
