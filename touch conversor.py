def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_para_kelvin(celsius):
    return celsius + 273.15

def kelvin_para_celsius(kelvin):
    return kelvin - 273.15

def menu():
    print("Conversor de Temperatura")
    print("1. Celsius para Fahrenheit")
    print("2. Fahrenheit para Celsius")
    print("3. Celsius para Kelvin")
    print("4. Kelvin para Celsius")
    print("5. Sair")

while True:
    menu()
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        celsius = float(input("Digite a temperatura em Celsius: "))
        print(f"{celsius}°C é igual a {celsius_para_fahrenheit(celsius):.2f}°F")
    elif escolha == "2":
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        print(f"{fahrenheit}°F é igual a {fahrenheit_para_celsius(fahrenheit):.2f}°C")
    elif escolha == "3":
        celsius = float(input("Digite a temperatura em Celsius: "))
        print(f"{celsius}°C é igual a {celsius_para_kelvin(celsius):.2f}K")
    elif escolha == "4":
        kelvin = float(input("Digite a temperatura em Kelvin: "))
        print(f"{kelvin}K é igual a {kelvin_para_celsius(kelvin):.2f}°C")
    elif escolha == "5":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")