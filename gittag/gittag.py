from .utils import run


def add_tag(tag, force=False):
    force_str = '-f' if force else ''

    run(f'git tag {force_str} {tag}', exit=True)
    run(f'git push origin {force_str} {tag}', exit=True)


def delete_tag(tag):
    r = run(f'git push --delete origin {tag}')
    print(r)
