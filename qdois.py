num = input('Digite um número: ')


decimal = float(num)
inteiro = int(float(num))

print(f'O número digitado foi {num} e é do tipo\n', type(decimal) if decimal != int(decimal) else type(int(num)))



