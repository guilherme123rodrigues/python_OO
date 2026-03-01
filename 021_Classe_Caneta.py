from rich.console import Console
from rich.panel import Panel

console = Console()

class Caneta():
    def __init__(self, cor, msg):
        self.cor = cor
        self.msg= msg

    #Metodo da classe
    def tinta(self):
        match self.cor:
            case 'red':
                console.print(Panel(f'[bold italic red]{self.msg}[/]'),width=len(self.msg)+5)
            case 'yellow':
                console.print(Panel(f'[bold italic yellow]{self.msg}[/]'), width=len(self.msg)+5)
            case 'black':
                console.print(Panel(f'[bold italic black]{self.msg}[/]'), width=len(self.msg)+5)



#Criação do objeto
p1 = Caneta('yellow', 'I want go to with my family. I Love they.')
p1.tinta()
