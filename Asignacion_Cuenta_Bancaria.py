class Usuario:
    bank_name = "Primer Dojo Nacional"
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.balance_cuenta = 0
    def hacer_depósito(self, amount):   # toma un argumento que es el monto del depósito
        self.balance_cuenta += amount   # la cuenta del usuario específico aumenta en la cantidad del valor recibido
        print(f"La cuenta de '{self.name}' resive depósito. Monto: ${amount}.")
        return self
    def hacer_retiro(self, amount):
        if (self.balance_cuenta > 0):
            self.balance_cuenta -= amount
            print(f"'{self.name}' retira ${amount} de su cuenta. Saldo actual: {self.balance_cuenta}")
            return self
        else: 
            print("Saldo isuficiente para realizar este retiro")
            return self
    def mostrar_balance_usuario(self):
        print(f"Usuario: {self.name}, Balance: ${self.balance_cuenta}")
        return self
    def transferir_dinero(self, other_user, amount):
        self.balance_cuenta -= amount
        other_user.balance_cuenta += amount
        print(f"'{self.name}' tranfiere ${amount} a cuenta de '{other_user.name}'")
        return self

guido =  Usuario("Guido van Rossum", "guido@python.com")
monty = Usuario("Monty Python", "monty@python.com")
chiri = Usuario("Christian Vargas", "christianj.vrgs@gmail.com")
Usuario.bank_name = "Banco del Dojo"

print("-"*70)
# Haz que el primer usuario haga 3 depósitos y 1 giro, y luego muestra sus balances

guido.hacer_depósito(100).hacer_depósito(200).hacer_depósito(300).hacer_retiro(150).mostrar_balance_usuario()

print("-"*70)
# Haz que el segundo usuario haga 2 depósitos y 2 giros, y luego muestra sus balances

monty.mostrar_balance_usuario().hacer_depósito(500).hacer_depósito(150).hacer_retiro(100).hacer_retiro(200).mostrar_balance_usuario()

print("-"*70)
# Haz que el tercer usuario haga 1 depósito y 3 giros, y luego muestra sus balances

chiri.mostrar_balance_usuario().hacer_depósito(2000).hacer_retiro(200).hacer_retiro(300).hacer_retiro(500).mostrar_balance_usuario()

print("-"*70)
# BONUS: Agrega un método transferir_dinero; haz que el primer usuario transfiera dinero al tercer usuario y luego imprime los balances de ambos usuarios

guido.mostrar_balance_usuario()
chiri.mostrar_balance_usuario()
guido.transferir_dinero(chiri, 100).mostrar_balance_usuario()
chiri.mostrar_balance_usuario()


class CuentaBancaria:
    cuentas = []
    def __init__(self):
        self.balance = 0
        self.tasa_interes = 0.01
        CuentaBancaria.cuentas.append(self)
    def deposito(self, amount):
        self.balance += amount
        print(f"La cuenta recibe depósito. Monto: ${amount}.")
        return self
    def retiro(self, amount):
        if (self.balance - amount) > 0:
            self.balance -= amount
            print(f"Retiro realizado por: ${amount}. Balance de cuenta: ${self.balance}")
            return self
        else:
            self.balance -= 5
            print("Fondos insuficientes: cobrando una tarifa de $5")
            return self
    def mostrar_info_cuenta(self):
        print(f"Balance: {self.balance}")
        return self
    def generar_interes(self):
        if self.balance > 0:
            self.balance = self.balance * (1 + self.tasa_interes)
            print (f"Interes generado del 1%. Balance actual: ${self.balance}")
            return self
        else: 
            print("Saldo insuficiente para generar interes positivo para su cuenta")
            return self


Cuenta1 = CuentaBancaria()
Cuenta2 = CuentaBancaria()

print("-"*120)
print("-"*120)
print("Cuenta1")
Cuenta1.deposito(50).deposito(100).deposito(150).retiro(100).generar_interes().mostrar_info_cuenta()
print("-"*70)
print("Cuenta2")
Cuenta2.deposito(500).deposito(1500).retiro(100).retiro(200).retiro(300).retiro(500).generar_interes().mostrar_info_cuenta()

print("-"*120)