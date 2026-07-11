def soma(a, b):
    return a + b
     

def sub(a, b):
    return a - b
    

def mult(a, b):
    return  a * b
    

def div(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero!"

def calculadora():
    while True:
        print("Escolha uma opção:")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. divisão")
        print("5. Sair")

        escolha =input("Digite o número da opção desejada: ")

        if escolha == '5':
            print("Saindo do programa...")
            break
        elif escolha in ['1', '2', '3', '4', '5']:
            num1 = float(input("Digite um número: "))
            num2 = float(input("Digite outro número: "))

            if escolha == '1':
                print(f"{num1} + {num2} = {soma(num1, num2)}")
            elif escolha == '2':
                print(f"{num1} - {num2} = {sub(num1, num2)}")
            elif escolha == '3':
                print(f"{num1} * {num2} = {mult(num1, num2)}")
            elif escolha == '4':
                print(f"{num1} / {num2} = {div(num1, num2)}")
        else:
            print("Escolha inválida. Por favor, selecione uma operação válida.")
            return calculadora()

calculadora()

