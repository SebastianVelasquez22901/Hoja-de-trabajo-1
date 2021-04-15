peso = int (input("Ingrese su peso: "))


altura = float (input("Ingrese su altura: "))

IMC = peso / (altura*altura)
MinumeroIMC = round(IMC, 2)
print("---------------------------------")
print("Su indice de masa es de: ", MinumeroIMC )
print("---------------------------------")
 