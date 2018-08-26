# -*- coding: utf-8 -*-

import sys

import click

from .gittag import add_tag, get_remote_tags, delete_local_tag, delete_remote_tag, sync_tags_remote_to_local


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

    delete_local_tag(tag)
    delete_remote_tag(tag)


@main.command()
def sync():
    """Syncs git tags. Remote to local."""

    sync_tags_remote_to_local()


if __name__ == "__main__":
    sys.exit(main())
