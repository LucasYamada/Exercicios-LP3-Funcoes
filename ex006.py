def converteNota(nota):
    if nota >= 900:
        return 'A'
    elif nota >= 800:
        return 'B'
    elif nota >= 700:
        return 'C'
    elif nota >= 600:
        return 'D'
    return 'F'