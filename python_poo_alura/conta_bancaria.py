class ContaBancaria:

    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @property
    def ativo(self):
        return self._ativo

    def ativar_conta(self):
        self._ativo = True


conta3 = ContaBancaria("Carlos", 200)
print(f"Antes de ativar: Conta ativa? {conta3._ativo}")
conta3.ativar_conta()
print(f"Depois de ativar: Conta ativa? {conta3._ativo}")

conta4 = ContaBancaria("Fernanda", 1500)
print(f"Titular da conta 4: {conta4.titular}")


class ClienteBanco:

    def __init__(self, nome, idade, email, conta, saldo):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.conta = conta
        self.saldo = saldo

    @classmethod
    def criar_conta(cls, titular, saldo_inicial):
        conta = ContaBancaria(titular, saldo_inicial)
        return conta

cliente1 = ClienteBanco("Raul", 20, "raul@lapaza.com", 1, 999999)
cliente2 = ClienteBanco("João", 21, "joão@lapaza.com", 2, 10)
cliente3 = ClienteBanco("Mazini", 22, "mazini@lapaza.com", 3, 11)

conta_cliente1 = ClienteBanco.criar_conta("Ana", 2000)
print(f"Conta de {conta_cliente1.titular} criada com saldo inicial de R${conta_cliente1.saldo}")