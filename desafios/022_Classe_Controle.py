from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel

console = Console()
layout = Layout()

layout.add_split(
    Layout(name='controle'),
    )

layout.split_row(Layout['controle'])

console.print(Panel(f'{layout}'))