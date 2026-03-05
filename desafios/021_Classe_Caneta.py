from rich.console import Console
from rich.panel import Panel

console = Console()

class Caneta():
    def __init__(self, cor):
        self.cor = cor
        self.tampa = True
        
    #Metodo da classe
    def destampar(self):
        self.tampa = False
    #Metodo da classe
    def escrever(self, msg):
        self.msg = msg
        #Se a tampa for diferente de True, execulta esse comando
        if not self.tampa:
            console.print(Panel(f'[bold italic {self.cor}]{self.msg}[/]'), width=len(self.msg)+4, justify='center')
        #Senão, execulta esse comando
        else:
            console.print(Panel(f'[bold]{self.msg}[/]'), width=len(self.msg)+4, justify='center')
            
#Criando objeto
p1 = Caneta('red')
#Chamando o metado da classe
p1.escrever('I Love You')
console.print('-'*30)

#Criando objeto
p2 = Caneta('yellow')
#Chamando o metodo da classe
p2.destampar()
p2.escrever( 'What is your name?')
