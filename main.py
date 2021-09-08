import random

caps1 = chr(random.randint(65,90))
caps2 = chr(random.randint(65,90))

lower1 = chr(random.randint(97,122))
lower2 = chr(random.randint(97,122))

number = str(random.randint(10,99))
symbol = chr(random.randint(33,47))

password = (caps1 + caps2 + symbol + lower1 + lower2 + number + symbol)
print(password)