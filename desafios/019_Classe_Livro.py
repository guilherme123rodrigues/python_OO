from rich.console import Console
from rich.panel import Panel

console = Console()

#Entidade da classe
class Livro():
    #Atributos da classe
    def __init__(self, autor, paginas):
        self.autor = autor
        self.paginas = paginas
        self.go = 1

    #Metodos da classe
    def passar_pagina(self, passa):
        console.print(f'Você acabou de abrir o livro [bold yellow italic]{self.autor}[/] que tem [bold green italic]{self.paginas}[/] página(s) no total. Você agora está na página {self.go}')
        cont = 0
        
        for c in range(self.go+1, (passa+self.go+1)):
            if c <= self.paginas:
                if c < (passa+self.go) and c < self.paginas:
                    console.print(f'[blue italic]Pág.{c}[/] =>',end=' ')
                else:
                    console.print(f'[blue italic]Pág.{c}[/]. Você acabou de avançar {cont+1} página(s)')
            else:
                console.print(f'\n❌[red italic]Chegamos ao fim do seu livro {self.autor}[/]❌')
                return
            cont += 1
        self.go += cont
        console.print()



        '''t = False
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
'''

#Criação do objeto da classe Livro
p1 = Livro('Thiago Nitro', 20)

p1.passar_pagina(5)
p1.passar_pagina(10)
