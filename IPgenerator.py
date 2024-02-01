
import random

def generate_IP():
    return ".".join(str(random.randint(0, 255)) for _ in range(4))

print(generate_IP())







