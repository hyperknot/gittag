# -*- coding: utf-8 -*-

import sys

import click
import semantic_version

if sys.version_info[0] < 3 or sys.version_info[1] < 5:
    sys.exit('gittag requires Python 3.5+')

from .gittag import (
    add_tag,
    delete_local_tag,
    delete_remote_tags,
    get_semver_tags,
    sync_local_to_remote,
    sync_remote_to_local,
)  # noqa


@click.group()
def main():
    """Console script for gittag."""
    return 0


@main.command()
@click.argument('tag')
@click.option('--force', '-f', default=False, is_flag=True, help='Override existing tag.')
def add(tag, force):
    """Add a git tag to current revision. Moves tag if already present. Local + remote."""

    add_tag(tag, force)


@main.command()
@click.argument('tag')
def remove(tag):
    """Remove a git tag. Local + remote."""

    delete_local_tag(tag)
    delete_remote_tags([tag])


@main.command()
@click.option(
    '--local-to-remote', '--l2r', default=False, is_flag=True, help='Sync local to remote.'
)
def sync(local_to_remote):
    """Syncs git tags. Remote to local."""

    if local_to_remote:
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
    if sys.version_info[0] < 3 or sys.version_info[1] < 5:
        raise Exception("Must be using Python 3.5+")

    sys.exit(main())
