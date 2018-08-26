from .utils import run


def add_tag(tag):
    run(f'git tag -f {tag}', exit=True)
    run(f'git push origin {tag}', exit=True)


def delete_tag(tag):
    r = run(f'git push --delete origin {tag}')
    print(r)
