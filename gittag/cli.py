# -*- coding: utf-8 -*-

import sys

import click
import semantic_version

from .gittag import add_tag, delete_local_tag, delete_remote_tag, get_semver_tags, sync_local_to_remote, sync_remote_to_local


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
@click.option('--local-to-remote', '--l2r', default=False, is_flag=True, help='Sync local to remote.')
def sync(l2r):
    """Syncs git tags. Remote to local."""

    if l2r:
        sync_local_to_remote()
    else:
        sync_remote_to_local()


@main.command()
@click.option('--prefix', '-p', help='Prefix for semver, like api_ for api_1.2.3')
def bump(prefix):
    """Bump a semver tag."""

    tags = get_semver_tags(source='remote', prefix=prefix)
    if tags:
        latest_tag = tags[-1]
    else:
        latest_tag = semantic_version.Version('0.1.0')

    print(latest_tag)



if __name__ == "__main__":
    sys.exit(main())
