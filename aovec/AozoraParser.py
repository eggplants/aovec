import codecs
import glob
import os
from typing import List, Optional, Tuple

from bs4 import BeautifulSoup as bs


class AozoraParser():
    __pwd__ = os.getcwd()
    AOZORA_BASE = os.path.join(__pwd__, 'aozorabunko')
    AOZORA_CARDS = os.path.join(AOZORA_BASE, 'cards')
    AOZORA_FILES = os.path.join(AOZORA_CARDS, '{}', 'files')

    def __init__(self, savedirname: str = 'novels') -> None:
        self.SAVEDIR = os.path.join(self.__pwd__, savedirname)
        os.makedirs(self.SAVEDIR, exist_ok=True)
        self.__check_aozora_dir()

    @classmethod
    def __check_aozora_dir(cls) -> None:
        if not cls.check_exist(cls.AOZORA_CARDS):
            raise FileNotFoundError(cls.AOZORA_CARDS)

    @classmethod
    def parse(cls) -> None:
        cards = [cls.get_novels(c) for c in cls.get_cards()]
        for novels in cards:
            for novel in novels:
                res = cls.__parse_novel(novel)
                if res:
                    sd = os.path.join(cls.SAVEDIR, res[0])
                    sf = os.path.join(sd, res[1])
                    os.makedirs(sd, exist_ok=True)
                    cls.__save_text(sf, res[2])

    @classmethod
    def __parse_novel(cls, novel: str) -> Optional[Tuple[str, str, str]]:
        print(novel)
        f = codecs.open(novel, 'r', encoding='utf-8')
        source = bs(f.read(), 'html.parser')
        cls.__decompose(source)

        novel_title = source.find('h1', class_='title')
        novel_author = source.find('h2', class_='author')
        novel_content = source.find('div', class_='main_text')
        f1 = novel_author is not None
        f2 = novel_author.string is not None
        if f1 and f2:
            return (novel_author.string, novel_title.string,
                    novel_content.text)
        else:
            return None

    @staticmethod
    def __save_text(path: str, text: str) -> None:
        print(text, file=open(path, 'w'))

    @staticmethod
    def __decompose(bs_: bs) -> None:
        try:
            for rt in bs_('rt'):
                rt.decompose()
            for rp in bs_('rp'):
                rp.decompose()
        except AttributeError as err:
            print(err)

    @staticmethod
    def check_exist(path: str) -> bool:
        return os.path.exists(path)

    @classmethod
    def get_cards(cls) -> List[str]:
        return [c for c in os.listdir(cls.AOZORA_CARDS)
                if c.isdecimal()]

    @classmethod
    def get_novels(cls, card: str) -> List[str]:
        f = cls.AOZORA_FILES.format(card)
        return glob.glob(os.path.join(f, '*.html'))


if __name__ == '__main__':
    AozoraParser().parse()
