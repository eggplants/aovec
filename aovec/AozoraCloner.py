import os
import subprocess
import sys
from shutil import which
from typing import Optional


class GitIsNotInstalled(Exception):
    pass


class AozoraCloner():
    url = 'https://github.com/aozorabunko/aozorabunko'

    def __init__(self) -> None:
        pass

    @classmethod
    def get_url(cls) -> str:
        return cls.url

    @classmethod
    def set_url(cls, url: str) -> None:
        cls.url = url

    @classmethod
    def clone(cls) -> Optional[int]:
        if not which('git'):
            raise GitIsNotInstalled
        else:
            p = subprocess.Popen('git clone --depth 1 ' + cls.url, shell=True)
            p.wait()
            return p.poll()


if __name__ == '__main__':
    REPO = os.path.join(os.getcwd(), 'aozorabunko')

    if os.path.isdir(REPO) and os.path.isdir(os.path.join(REPO, '.git')):
        print('aozorabunko already exists!', file=sys.stderr)
        exit(0)
    else:
        AozoraCloner().clone()
