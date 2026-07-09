import click
import os
from .operations import organize_files, rename_files

@click.group()
def cli():
    """File Organizer CLI - Organize and rename your files with ease."""
    pass

@cli.command()
@click.argument('directory', type=click.Path(exists=True, file_okay=False, dir_okay=True))
def organize(directory):
    """Organize files in the given directory by their extensions.
    
    Creates subfolders like 'Images', 'Documents', etc., and moves files into them.
    """
    click.echo(f"Organizing files in '{directory}'...")
    try:
        organize_files(directory)
    except Exception as e:
        click.secho(f"Error: {str(e)}", fg="red")

@cli.command()
@click.argument('directory', type=click.Path(exists=True, file_okay=False, dir_okay=True))
@click.argument('pattern')
@click.argument('replacement')
def rename(directory, pattern, replacement):
    """Bulk rename files by replacing a pattern with a replacement string.
    
    Replaces all occurrences of PATTERN with REPLACEMENT in the filenames
    within the specified DIRECTORY.
    """
    click.echo(f"Renaming files in '{directory}' (replacing '{pattern}' with '{replacement}')...")
    try:
        rename_files(directory, pattern, replacement)
    except Exception as e:
        click.secho(f"Error: {str(e)}", fg="red")

if __name__ == '__main__':
    cli()
