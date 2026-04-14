from rich.console import Console
from rich.panel import Panel

console = Console()

#Entidade da classe
class Produto():
    #Atributos da classe
    def __init__(self, nome, preço='⛔ Preço não informado'):
        self.nome = nome
        self.preço = preço

    #Metodo da classe
    def etiqueta(self):
        console.print(
            Panel(
                f'[bold italic]Nome:[/] [bold italic yellow]{self.nome}[/]\n'
                f'{'-'*20}\n'
                f'[bold italic]Preço:[/] [bold italic green]R${self.preço}[/]',
                title='[bold italic]Etiqueta[/]'
                ),
                width=30
            )
        
#Criação do objeto 01
p1 = Produto('Arroz', 14.90)
p1.etiqueta()

#Criação do objeto 02
p2 = Produto('Perá')
p2.etiqueta()