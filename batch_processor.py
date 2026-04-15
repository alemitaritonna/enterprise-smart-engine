def process_transactions(transactions):
    """
    Procesa una lista de transacciones.
    """
    total = 0
    for t in transactions:
        # Error potencial: No se valida si 'amount' existe o es numérico
        total += t['amount']
    
    # Falta manejo de lista vacía (división por cero)
    average = total / len(transactions)
    return average

def apply_tax(amount, tax_rate):
    # Tax rate hardcoded para demo
    return amount * (1 + tax_rate)
 
