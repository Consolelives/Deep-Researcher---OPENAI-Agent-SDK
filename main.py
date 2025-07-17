from dotenv import load_dotenv
from rich.console import Console
from rich.prompt import Prompt
import asyncio
from coordinator import ResearchCoordinator

load_dotenv(override=True)

console = Console()

async def main():
    console.print("[bold cyan]Deep Research Tool[/bold cyan] - Console Edition")
    console.print("This tool performs in-depth research on any topic using AI Agents")

    # Get the users query
    query= Prompt.ask("\n[bold]What would you like to research about?[/bold]")

    if not query.strip():
        console.print("[bold red]Erro:[/bold red] Please provide a valid query.")
        return
    
    research_coodinator = ResearchCoordinator(query)
    report = await research_coodinator.research()


if __name__ == "__main__":
    asyncio.run(main())