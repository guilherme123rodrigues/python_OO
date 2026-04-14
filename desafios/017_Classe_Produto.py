from rich.console import Console
from rich.panel import Panel

console = Console()

#Entidade da classe
class Produto():
    #Atributos da classe
    def __init__(self, nome, preço):
        self.nome = nome
        self.preço = preço

    #Metodo da classe
    def etiqueta(self):
        conteudo = f"{self.nome:^25}"
        conteudo += f"{'-'*25}\n"
        precof = f"R${self.preço:,.2f}"
        conteudo += f"{precof:.^25}"
        console.print(Panel(f'{conteudo}', title='[bold italic]Etiqueta[/]'), width=30)
        
#Criação do objeto 01
p1 = Produto('PlayStaytion5', 5_122.90)
p1.etiqueta()

#Criação do objeto 02
p2 = Produto('Perá', 2_00)
p2.etiqueta()