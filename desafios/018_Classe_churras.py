from rich.console import Console
from rich.panel import Panel

#Posso usar os recursos que tem o biblioteca "rich"
console = Console()

#Entidade da classe
class Churras():
    '''
    
    Essa classe serve para calcular o total de carne que deverá compra, e calcula o total a ser gasto por pessoa.

    Sintax:

    Variavel = Churras(titulo, quantidade de pessoa)
    
    '''
    def __init__(self, titulo, quantidade):
        #Atirbutos da instância
        self.titulo = titulo
        self.quantidade = quantidade

    #Metodo da classe
    def calculo(self):
        kg = 400
        preço = 82.40
        t_carne = self.quantidade * kg

        #Fiz uma condição, se a quantidade de pessoa for == 1 pego o resto de t_carne % 1000 que vai ser 500
        #Senão, faço a divissão normal.
        k_p = str(t_carne % 1000) + 'g' if 1 <= self.quantidade <= 2 else str(t_carne / 1000) + ' kg'
        tot_pagar = (t_carne * preço) / 1000

        console.print(Panel(f'Quantidade de pessoa:\t{self.quantidade}\n'
                            f'Quantidade de carne:\t{k_p}\n' 
                            f'Total a ser pago:\tR${tot_pagar:.2f}\n'
                            f'Cada um vai pagar: \tR${tot_pagar/self.quantidade:.2f}'
                            , title=f'[bold italic yellow]{self.titulo}[/]'
                            , width=50
                            )
                    )


#Criação do objeto
p1 = Churras('Churras dos amigos', 15)
p1.calculo()

#Criação do objeto
p1 = Churras('Festa fim de ano', 35)
p1.calculo()
