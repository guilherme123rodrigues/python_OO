from rich.console import Console
from rich.panel import Panel
from time import sleep

console = Console()

#Entidade da classe
class Livro():
    #Atributos da classe
    def __init__(self, autor, paginas):
        self.autor = autor
        self.paginas = paginas
        self.p_atual = 1

        console.print(f'[bold blue italic]:open_book: Você acabou de abrir o livro [bold yellow italic]{self.autor}[/] que tem [bold green italic]{self.paginas}[/] [bold blue italic]página(s) no total. Você agora está na página[blu/] [bold red italic]{self.p_atual}[/]')

    #Metodos da classe
    def passar_pagina(self, passa=1):
        cont = 0
        for pg in range(0, passa, 1):
            if not self.verificar():
                self.p_atual += 1
                console.print(f'Pág.{self.p_atual} :arrow_forward:', end = ' ')
                sleep(0.2)
                cont += 1
        console.print(f'[bold blue italic]Você avançou {cont} página(s) e agora está na página[/] [bold red italic]{self.p_atual}[/]')
        if self.verificar():
            console.print(f'[bold green italic]:closed_book: Você chegou no final do livro[/] [bold yellow italic]{self.autor}[/]')
            return True
        else:
            return False
        
            
    def verificar(self) -> bool:
        return True if self.p_atual == self.paginas else False



l = str(input('Nome do livro: ')).strip().title()
p = int(input('Quantidade de páginas: '))
p1 = Livro(l, p)
#Criação do objeto da classe Livro
while True:
    resp = int(input('Quantas páginas deseja avançar? '))
    v = p1.passar_pagina(resp)
    if not v:
        print('-'*30)
    else:
        break
