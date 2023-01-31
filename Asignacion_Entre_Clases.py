class CuentaBancaria:
    cuentas = []
    def __init__(self, tasa_interes=0.02, balance=0):
        self.tasa_interes = tasa_interes
        self.balance = balance
        CuentaBancaria.cuentas.append(self)
    def deposito(self, amount):
        self.balance += amount
        return self
    def retiro(self, amount):
        if (self.balance - amount) > 0:
            self.balance -= amount
            return self
        else:
            self.balance -= 5
            print("Fondos insuficientes: cobrando una tarifa de $5")
            return self
    def mostrar_info_cuenta(self):
        print(f"Balance: {self.balance}")
    def generar_interes(self):
        if self.balance > 0:
            self.balance = self.balance * (1 + self.tasa_interes)
            print (f"Interes generado del 2%. Balance actual: ${self.balance}")
            return self
        else: 
            print("Saldo insuficiente para generar interes positivo para su cuenta")
            return self
    @classmethod
    def instancias(cls):
        for i in cls.cuentas:
            i.mostrar_info_cuenta()


class Usuario:
    bank_name = "Primer Dojo Nacional"
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.cuenta = CuentaBancaria()
    def hacer_depósito(self, amount):
        self.cuenta.deposito(amount)
        print(f"La cuenta de '{self.name}' resive depósito. Monto: ${amount}. Saldo: {self.cuenta.balance}")
        return self
    def hacer_retiro(self, amount):
        self.cuenta.retiro(amount)
        print(f"'{self.name}' hace retiro por ${amount}.")
        return self
    def mostrar_balance_usuario(self):
        print(f"Usuario: {self.name}.")
        self.cuenta.mostrar_info_cuenta()
        return self
    def transferir_dinero(self, other_user, amount):
        self.cuenta.balance -= amount
        other_user.cuenta.balance += amount
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

CuentaBancaria.instancias()

print("-"*120)
print("-"*120)
print("-"*120)
print("-"*120)
print("-"*120)
print("-"*120)

class UsuarioPremium:
    bank_name = "Segundo Dojo Nacional"
    cuentasDoble = []
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.cuenta = CuentaBancariaDoble()
        UsuarioPremium.cuentasDoble.append(self)
    def hacer_depósito(self, cuenta_, amount):
        print(f"Cuenta de '{self.name}' resive depósito!.")
        self.cuenta.deposito(cuenta_, amount)
        return self
    def hacer_retiro(self, cuenta_, amount):
        print(f"Cuenta de '{self.name}' Retiro de dinero!.")
        self.cuenta.retiro(cuenta_, amount)
        return self
    def mostrar_balance_usuario(self):
        print(f"Usuario: {self.name}.  cuenta_1: {self.cuenta.cuenta_1}.  cuenta_2: {self.cuenta.cuenta_2}")
        return self
    def transferir_dinero(self, other_user, amount):
        self.cuenta.balance -= amount
        other_user.cuenta.balance += amount
        print(f"'{self.name}' tranfiere ${amount} a cuenta de '{other_user.name}'")
        return self

class CuentaBancariaDoble:
    def __init__(self, tasa_interes=0.03, cuenta_1=0, cuenta_2=0):
        self.tasa_interes = tasa_interes
        self.cuenta_1 = cuenta_1
        self.cuenta_2 = cuenta_2
    def deposito(self, cuenta_, amount):
            if cuenta_ == "cuenta_1":
                self.cuenta_1 += amount
                print(f"Cuenta: cuenta_1.  Monto: ${amount}.  Saldo: ${self.cuenta_1}")
                print("")
                return self
            elif cuenta_ == "cuenta_2":
                self.cuenta_2 += amount
                print(f"Cuenta: cuenta_2.  Monto: ${amount}.  Saldo: ${self.cuenta_2}")
                print("")
                return self
            else:
                print("Error al ingresar datos de cuenta")
                print("")
                return self
    def retiro(self,cuenta_, amount):
        if cuenta_ == "cuenta_1":
            if (self.cuenta_1 - amount) > 0:
                self.cuenta_1 -= amount
                print(f"Cuenta: cuenta_1.  Monto: ${amount}.  Saldo: ${self.cuenta_1}")
                print("")
                return self
            else:
                print(f"Saldo insuficiente!  Saldo solicitado: ${amount}.  Saldo: ${self.cuenta_1}")
                print("")
                return self
        elif cuenta_ == "cuenta_2":
            if (self.cuenta_2 - amount) > 0:
                self.cuenta_2 -= amount
                print(f"Cuenta: cuenta_2.  Monto: ${amount}.  Saldo: ${self.cuenta_2}")
                print("")
                return self
            else:
                print(f"Saldo insuficiente!  Saldo solicitado: ${amount}.  Saldo: ${self.cuenta_2}")
                print("")
                return self
        else:
            print("Error al ingresar datos")
            print("")
            return self
    def generar_interes(self, cuenta_):
        if cuenta_ == "cuenta_1":
            if self.cuenta_1 > 0:
                self.cuenta_1 = self.cuenta_1 * (1 + self.tasa_interes)
                print (f"Interes generado del 3%. Balance actual de cuenta_1: ${self.cuenta_1}")
                return self
            else:
                print("Saldo insuficiente para generar interes")
                return self
        elif cuenta_ == "cuenta_2":
            if self.cuenta_2 > 0:
                self.cuenta_2 = self.cuenta_2 * (1 + self.tasa_interes)
                print (f"Interes generado del 3%. Balance actual de cuenta_2: ${self.cuenta_2}")
                return self
            else:
                print("Saldo insuficiente para generar interes")
                return self
        else: 
            print("Error al ingresar datos")
            return self
    @classmethod
    def instancias(cls):
        print("Clientes con cuentas dobles:")
        for i in UsuarioPremium.cuentasDoble:
            i.mostrar_balance_usuario()
        print("")



vale = UsuarioPremium("Valeria Castro", "vacc_90@gmail.com")
felipe = UsuarioPremium("Felipe Vargas", "f.vargas@gmail.com")

vale.hacer_depósito("cuenta_1", 100).hacer_depósito("cuenta_1", 150).hacer_depósito("cuenta_2", 200).hacer_retiro("cuenta_1", 50).hacer_retiro("cuenta_2", 50).hacer_retiro("cuenta_1", 260)
felipe.hacer_depósito("cuenta_1", 300)

print("-"*120)
CuentaBancariaDoble.instancias()