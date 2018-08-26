from .utils import die, lstrip, rstrip, run


def add_tag(tag, force=False):
    force_str = '-f' if force else ''

    run(f'git tag {force_str} {tag}', exit=True)
    run(f'git push origin {force_str} {tag}', exit=True)


def delete_local_tag(tag):
    r = run(f'git tag --delete {tag}')
    if r.returncode != 0 and f"error: tag '{tag}' not found." not in r.stderr:
        die(r)


def delete_local_tags(tags):
    tags_str = ' '.join(tags)
    run(f'git tag --delete {tags_str}', exit=True)


def delete_remote_tag(tag):
    r = run(f'git push --delete origin {tag}')
    if r.returncode != 0 and f"error: unable to delete '{tag}': remote ref does not exist" not in r.stderr:
        die(r)


def get_local_tags():
    r = run('git show-ref --tags --dereference', exit=False)

    tags = dict()

    for l in r.stdout.splitlines():
        commit, tag = l.split()
        tag = lstrip(tag, 'refs/tags/')
        tag = rstrip(tag, '^{}')

        tags[tag] = commit

    return tags


def get_remote_tags():
    r = run('git ls-remote --tags', exit=True)

    tags = dict()

    for l in r.stdout.splitlines():
        commit, tag = l.split()
        tag = lstrip(tag, 'refs/tags/')
        tag = rstrip(tag, '^{}')

        tags[tag] = commit

    return tags


def sync_remote_to_local():
    local_tags = get_local_tags()

    delete_local_tags(local_tags.keys())

    run('git fetch --tags', exit=True)


def sync_local_to_remote():
    remote_tags = get_remote_tags()
    local_tags = get_local_tags()

    for remote_tag, remote_commit in remote_tags.items():
        if remote_tag in local_tags:
            # tags with wrong commit
            if remote_commit != local_tags[remote_tag]:
                delete_remote_tag(remote_tag)

        # leftover tags
        else:
            delete_remote_tag(remote_tag)

    run('git push --tags origin', exit=True)
