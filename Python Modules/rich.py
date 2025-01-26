from rich.console import Console
from rich.theme import Theme
from rich.traceback import install

install(show_locals=True) 

custom_theme = Theme({'error': 'bold red', 'warning': 'bold yellow'})

console = Console(theme=custom_theme)

def compare_numbers(a, b):
    console.log(log_locals=True)
    if a > b:
        console.print(f"{a} is greater than {b}", style="bold green")
    elif a < b:
        console.print(f"{a} is less than {b}", style="warning")
    else:
        console.print(f"{a} is equal to {b}")

compare_numbers(5, 10)
compare_numbers(10, 5)
compare_numbers(5, 5)

compare_numbers(5, "Ecem")

from rich.console import Console
from rich.table import Table
from rich.progress import Progress
from rich.traceback import install
from rich.logging import RichHandler
import logging
import time

# Install rich traceback for better error visualization
install(show_locals=True) 

# Create a console instance
console = Console()

# 1. Pretty-print dictionaries with colors and styling
console.print("[bold cyan]Pretty-Printing a Dictionary:[/bold cyan]")
data = {
    "name": "Alice",
    "age": 30,
    "languages": ["Python", "JavaScript", "C++"]
}
console.print(data, style="bold green")

# 2. Custom-styled text
console.print("\n[bold magenta]Hello, [italic cyan]Rich![/italic cyan][/bold magenta]")

# 3. Creating a table
console.print("\n[bold cyan]Table Example:[/bold cyan]")
table = Table(title="Programming Languages")
table.add_column("Language", justify="left", style="bold yellow")
table.add_column("Type", justify="center", style="bold green")
table.add_row("Python", "Dynamic")
table.add_row("C++", "Static")
table.add_row("JavaScript", "Dynamic")
console.print(table)

# 4. Progress bar example
console.print("\n[bold cyan]Progress Bar Example:[/bold cyan]")
with Progress() as progress:
    task = progress.add_task("[cyan]Downloading...", total=100)
    for i in range(100):
        time.sleep(0.05)  # Simulate work
        progress.update(task, advance=1)

# 5. Logging example
console.print("\n[bold cyan]Logging Example:[/bold cyan]")
logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    handlers=[RichHandler()]
)
logger = logging.getLogger("rich")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")

# 6. Rich traceback example
console.print("\n[bold cyan]Traceback Example:[/bold cyan]")
try:
    1 / 0  # This will raise an error
except ZeroDivisionError:
    console.print_exception()

# 7. Styled live output (using Console and Status)
console.print("\n[bold cyan]Live Status Example:[/bold cyan]")
from rich.status import Status

with console.status("[bold green]Working on something...[/bold green]") as status:
    for i in range(3):
        time.sleep(1)  # Simulate work
    console.print("[bold blue]Task completed![/bold blue]")

# 8. Markdown rendering
console.print("\n[bold cyan]Markdown Rendering Example:[/bold cyan]")
from rich.markdown import Markdown

markdown_text = """
# Hello, Rich!
This is a **Rich Markdown** example.
- Supports **bold** and *italic*.
- Render lists, tables, and more!
"""
console.print(Markdown(markdown_text))

# 9. Syntax highlighting
console.print("\n[bold cyan]Syntax Highlighting Example:[/bold cyan]")
from rich.syntax import Syntax

code = """def hello_rich():
    print("Hello, Rich!")
hello_rich()
"""
syntax = Syntax(code, "python", theme="monokai", line_numbers=True)
console.print(syntax)
