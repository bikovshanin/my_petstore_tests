import random
import string


def generate_random_string(length=10):
    """Генерация случайной строки указанной длины."""
    return ''.join(
        random.choices(string.ascii_letters + string.digits, k=length))
