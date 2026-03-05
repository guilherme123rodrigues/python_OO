from rich.console import Console
from rich.panel import Panel
from time import sleep

console = Console()

#Entidade da classe
class Gamer():
    def __init__(self, nome, nick, *favoritos):
        #Entidades d classe
        self.nome = nome
        self.nick = nick
        self.favoritos = favoritos


    #Metodo da classe
    def ficha(self):
        #Pega a lista e junta em uma string só, uma embaixo da outra
        jogos = '\n'.join(self.favoritos)
        console.print(
            Panel(
                f'\n[bold italic yellow]Nome do jogador:[/] {self.nome}\n\n'
                f'[bold italic yellow]Jogos favoritos:[/]\n{jogos}\n'
                , title=f'{self.nick}'
                , width=50
                )
                    )
            

#Criação do objeto
p1 =  Gamer('Guilherme', 'Matador_de_aluguel', 'Free Fire', 'Bomba Pet', 'GTA 5')
p1.ficha()
