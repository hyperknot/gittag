# -*- coding: utf-8 -*-

import sys
import click


@click.group()
def main(args=None):
    """Console script for gittag."""
    return 0


@main.command()
def add():
    """Add a git tag to current revision. Moves tag if already present. Local + remote."""



if __name__ == "__main__":
    sys.exit(main())
