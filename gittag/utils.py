import subprocess
import sys


def run(command, exit=False):
    args = command.split()
    r = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

    if exit and (r.returncode != 0):
        die(r)

    return r


def die(r):
    command = ' '.join(r.args)
    print(f'Error running command:\n{command}\n\nOutput was:\n{r.stdout}\n\nError was:\n{r.stderr}')
    sys.exit(1)
