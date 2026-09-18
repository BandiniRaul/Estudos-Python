from datetime import datetime
agendamentos: list[Agendamento] = []

def data_valida(data_informada):
    return data_informada >= datetime.now().date()

class Agendamento:
    def __init__(self, data, nome_evento):
        self.data = data
        self.nome_evento = nome_evento

    def reagendar_data (self, nova_data):
        self.data = nova_data

    def __str__ (self):
        return f"{self.nome_evento} ({self.data.strftime ('%d-%m-%Y')})"

while True:
    print("\n1. Realizar agendamento")
    print("2. Visualizar todos os agendamentos")
    print("3. Reagendar")
    print("4. Cancelar agendamento")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
            data_informada = input("Digite a data (DD-MM-AAAA): ")
            data = datetime.strptime(data_informada, "%d-%m-%Y").date()
            if not data_valida(data):
                print("Data inválida")
                nome_evento = input("Digite o nome do evento: ")
                continue
            agendamento = Agendamento(data, nome_evento)
            agendamentos.append(agendamento)
            print("Evento agendado!")

        case "2":
            for agendamento in agendamentos:
                print(agendamento)

        case "3":
            nome_evento = input("Digite o nome do evento: ")
            nome_encontrado = [a for a in agendamentos if a.nome_evento == nome_evento]
            if not nome_encontrado:
                print("Evento não encontrado")
                continue
            nova_data_informada = (input("Evento encontrado, digite a nova data: "))
            nova_data = datetime.strptime(nova_data_informada, "%d-%m-%Y").date()
            if not data_valida(nova_data):
                print("Data inválida")
                continue
            agendamento.reagendar_data(nova_data)

        case "4":
            nome_evento = input("Digite o nome do evento que deseja cancelar: ")
            agendamento_encontrado = [a for a in agendamentos if a.nome_evento == nome_evento]
            if not agendamento_encontrado:
                print("Evento não encontrado")
                continue
            agendamento_a_remover = agendamento_encontrado[0]
            agendamentos.remove(agendamento_a_remover)
            print("Evento removido!")

        case "5":
            break

        case _:
            print("\033[31mOpção inválida.\033[0m")