# -*- coding: utf-8 -*-

import sys

import click

from .gittag import add_tag, remove_tag


@click.group()
def main():
    """Console script for gittag."""
    return 0


@main.command()
@click.argument('tag')
def add(tag):
    """Add a git tag to current revision. Moves tag if already present. Local + remote."""

    add_tag(tag, force=True)


@main.command()
@click.argument('tag')
def remove(tag):
    """Remove a git tag. Local + remote."""

    remove_tag(tag)


if __name__ == "__main__":
    sys.exit(main())
