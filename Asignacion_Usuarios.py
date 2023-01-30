class Usuario:
    bank_name = "Primer Dojo Nacional"
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.balance_cuenta = 0
    def hacer_depósito(self, amount):   # toma un argumento que es el monto del depósito
        self.balance_cuenta += amount   # la cuenta del usuario específico aumenta en la cantidad del valor recibido
        print(f"La cuenta de '{self.name}' resive depósito. Monto: ${amount}.")
    def hacer_retiro(self, amount):
        self.balance_cuenta -= amount
        print(f"'{self.name}' retira ${amount} de su cuenta. Saldo actual: {self.balance_cuenta}")
    def mostrar_balance_usuario(self):
        print(f"Usuario: {self.name}, Balance: ${self.balance_cuenta}")
    def transferir_dinero(self, other_user, amount):
        self.balance_cuenta -= amount
        other_user.balance_cuenta += amount
        print(f"'{self.name}' tranfiere ${amount} a cuenta de '{other_user.name}'")

guido =  Usuario("Guido van Rossum", "guido@python.com")
monty = Usuario("Monty Python", "monty@python.com")
chiri = Usuario("Christian Vargas", "christianj.vrgs@gmail.com")
# guido.bank_name = "Dojo Credit Union"

Usuario.bank_name = "Banco del Dojo"
print(guido.bank_name) # salida: Banco del Dojo
print(monty.bank_name) # salida: Banco del Dojo

print(guido.name)
print(monty.name)

guido.mostrar_balance_usuario()
monty.mostrar_balance_usuario()
chiri.mostrar_balance_usuario()

print("-"*70)
# Haz que el primer usuario haga 3 depósitos y 1 giro, y luego muestra sus balances

guido.mostrar_balance_usuario()
guido.hacer_depósito(100)
guido.hacer_depósito(200)
guido.hacer_depósito(300)
guido.hacer_retiro(150)
guido.mostrar_balance_usuario()

print("-"*70)
# Haz que el segundo usuario haga 2 depósitos y 2 giros, y luego muestra sus balances

monty.mostrar_balance_usuario()
monty.hacer_depósito(500)
monty.hacer_depósito(150)
monty.hacer_retiro(100)
monty.hacer_retiro(200)
monty.mostrar_balance_usuario()

print("-"*70)
# Haz que el tercer usuario haga 1 depósito y 3 giros, y luego muestra sus balances

chiri.mostrar_balance_usuario()
chiri.hacer_depósito(2000)
chiri.hacer_retiro(200)
chiri.hacer_retiro(300)
chiri.hacer_retiro(500)
chiri.mostrar_balance_usuario()

print("-"*70)
# BONUS: Agrega un método transferir_dinero; haz que el primer usuario transfiera dinero al tercer usuario y luego imprime los balances de ambos usuarios

guido.mostrar_balance_usuario()
chiri.mostrar_balance_usuario()
guido.transferir_dinero(chiri, 100)
guido.mostrar_balance_usuario()
chiri.mostrar_balance_usuario()
