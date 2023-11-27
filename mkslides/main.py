import os
import click

from .config import load_config, initialize_configuration_file, DefaultPaths
from .deck import Deck
from .utils import save_to_file


def create_sample_cover_slide(filename: str) -> None:
    """Creates sample slide for configuration initialization."""
    sample_slide_content = """
    # MkSlides

    Free your slides! Markdown based, version controlled, configurable slide decks. MkDocs for slides.
    """
    save_to_file(filename, sample_slide_content)
    return


def initialize_slides_dir(dirname: str) -> None:
    """Initializes a new slides directory, including sample cover slide."""
    os.mkdir(dirname)
    create_sample_cover_slide(os.path.join(dirname, "cover.md"))
    return


@click.group()
def mkslides():
    pass


@mkslides.command("init", help="Initialize a new mkslides configuration file.")
def init():
    click.echo(
        click.style("Initializing _mkslides_ artifacts", fg="green", underline=True)
    )
    if os.path.exists(DefaultPaths.CONFIG_FILENAME):
        raise FileExistsError(
            click.style(
                f"Mkslides configuration file '{DefaultPaths.CONFIG_FILENAME}' already exists. Either delete existing file first or add a new deck section to existing file.",
                fg="red",
            )
        )
    else:
        initialize_configuration_file()
        click.echo(
            click.style(
                f"- Added new configuration file '{DefaultPaths.CONFIG_FILENAME}'...",
                fg="green",
            )
        )
    # add slides dir if it doesn't yet exist
    if not os.path.exists(DefaultPaths.SLIDE_DIR):
        initialize_slides_dir(DefaultPaths.SLIDE_DIR)
        click.echo(click.style("- Added new `slides` directory...", fg="green"))
    else:
        click.echo(
            click.style(
                f"- Found existing '{DefaultPaths.SLIDE_DIR}' directory...", fg="yellow"
            )
        )
    click.echo("--> You are ready to begin writing slides!")


# TODO: argument/option to specify output marp file
@mkslides.command("build", help="Build slide-deck from mkslides configuration file.")
def build():
    config = load_config(DefaultPaths.CONFIG_FILENAME)
    # create directory for output deck if does not exist
    if not os.path.exists(config.output_dir):
        os.mkdir(config.output_dir)
        click.echo(
            click.style(
                f"Created directory '{config.output_dir}' to store output slide decks...",
                fg="yellow",
            )
        )
    # check for existing slide deck if configs.overwrite is False
    if config.overwrite is False and os.path.exists(config.name):
        raise ValueError(
            f"Slide deck with name '{config.name}' already exists and configs.overwrite set to 'False'."
        )

    deck = Deck(config)
    deck.build()

    click.echo(f"created '{config.name}' from {len(config.slides):,} slides.")


if __name__ == "__main__":
    mkslides()
