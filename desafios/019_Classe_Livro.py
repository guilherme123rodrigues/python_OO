from rich.console import Console
from rich.panel import Panel

console = Console()

#Entidade da classe
class Livro():
    #Atributos da classe
    def __init__(self, autor, paginas):
        self.autor = autor
        self.paginas = paginas

    #Metodos da classe
    def passar_pagina(self):
        t = False
        p2 = 0 
        p3 = 0
        while True:
            while True:
                try:
                    p = int(input('Quantas páginas irá passar? '))
                except (TypeError, ValueError):
                    console.print('[bold red]Valor inválido![/]')
                else:
                    break
            if p < 0:
                console.print('Não aceito valor negativo, apenas valores inteiros. [bold red]Tente novamente![/]')
            else:
                p1 = p + p2
                for c in range(p3+1, p1+1):
                    if c <= self.paginas:
                        print(f'▶▶ Página {c}', end = ' ')
                        p2 += 1
                        if c == self.paginas:
                            console.print('')
                            console.print(Panel(f'[bold italic red]Você chegou na página final do livro[/] [bold italic green]"{self.autor}"[/]'), width=55)
                            t = True
                            break
                    else:
                        console.print('')
                        console.print(Panel(f'[bold italic red]Você já atingiu o limite de págia do livro[/] [bold italic green]"{self.autor}"[/]'), width=55)
                        t = True
                        break
                p3 += p
            if t == True:
                break
            print('\n')


#Criação do objeto da classe Livro
p1 = Livro('Thiago Nitro', 20)
p1.passar_pagina()
