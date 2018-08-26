from .utils import run, die


def add_tag(tag, force=False):
    force_str = '-f' if force else ''

    run(f'git tag {force_str} {tag}', exit=True)
    run(f'git push origin {force_str} {tag}', exit=True)


def remove_tag(tag):
    r = run(f'git tag --delete {tag}', exit=False)
    if r.returncode != 0 and f"error: tag '{tag}' not found." not in r.stderr:
        die(r)

    r = run(f'git push --delete origin {tag}', exit=False)
    if r.returncode != 0 and f"error: unable to delete '{tag}': remote ref does not exist" not in r.stderr:
        die(r)
