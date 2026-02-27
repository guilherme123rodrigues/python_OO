from rich.console import Console
from rich.panel import Panel

console = Console()

#Classe orientado objeto
class Funcionario():
    #Atributo da classe
    def __init__(self, nome, setor, cargo, salario=0):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
        self.salario = salario

    #Metodo da classe
    def apresentar_se(self):
        console.print(
                    Panel(
                            f'[bold italic]Nome:[/] [bold italic green]{self.nome}[/]\n'
                            f'[bold italic]Trabalha na área:[/] [bold italic yellow]{self.setor}[/]\n'
                            f'[bold italic]Cargo:[/] [bold italic yellow]{self.cargo}[/]\n'
                            f'[bold italic]Salário atual:[/][bold italic green]R${self.salario:,.2f}[/]',
                            title='[bold italic]Dados do funcionario[/]'
                            )
                      , width=50
                      )


#Criação do objeto 01
f1 = Funcionario('Guilherme', 'TI', 'Desenvolvedor de Sistemas', 7_900.00)
f1.apresentar_se()

#Criação do objeto 02
f2 = Funcionario('Karen', 'Administração','Marketing', 4_500.00)
f2.apresentar_se()


