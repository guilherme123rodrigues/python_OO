from rich.console import Console
from rich.panel import Panel

#Posso usar os recursos que tem o biblioteca "rich"
console = Console()

#criação da classe
class Churras():
    '''
    
    Essa classe serve para calcular o total de carne que deverá commpra, e calcular o total a ser gasto por peesso

    Sintax:

    Variavel = Churras(quantidade = valor obrigatiorio)
    
    '''
    def __init__(self, quantidade):
        #Atirbutos da classe
        self.quantidade = quantidade

    #Metodo da classe
    def calculo(self):
        kg = 500
        preço = 82.40
        t_carne = self.quantidade * kg

        #Fiz um condição, se a quantidade de pessoa for == 1 pego o resto de t_carne / 1000 que vai ser 500
        #senão, faço a divissão normal.
        k_p = str(t_carne % 1000) + 'g' if self.quantidade == 1 else str(t_carne / 1000) + ' kg'
        tot_pagar = (t_carne * preço) / 1000

        console.print(Panel(f'Quantidade de pessoa:\t{self.quantidade}\n'
                            f'Kilo de carne:\t\t{k_p}\n' 
                            f'Total a ser pago:\tR${tot_pagar:.2f}'
                            , title='[bold italic yellow]Churras[/]'
                            , width=50
                            )
                    )


#Criação do objeto
p1 = Churras(0)
p1.calculo()
