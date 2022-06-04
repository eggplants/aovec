from __future__ import annotations

import codecs
import glob
import os
import sys

import bs4


class AozoraParser:
    __pwd__ = os.getcwd()
    AOZORA_BASE = os.path.join(__pwd__, "aozorabunko")
    AOZORA_CARDS = os.path.join(AOZORA_BASE, "cards")
    AOZORA_FILES = os.path.join(AOZORA_CARDS, "{}", "files")

    def __init__(self, savedirname: str = "novels") -> None:
        self.SAVEDIR = os.path.join(self.__pwd__, savedirname)
        os.makedirs(self.SAVEDIR, exist_ok=True)
        self.__check_aozora_dir()

    @classmethod
    def __check_aozora_dir(cls) -> None:
        if not cls.check_exist(cls.AOZORA_CARDS):
            raise FileNotFoundError(cls.AOZORA_CARDS)

    def parse(self) -> None:
        cards = [self.get_novels(c) for c in self.get_cards()]
        c_len = len(sum(cards, []))
        idx = 0
        for novels in cards:
            for novel in novels:
                res = self.__parse_novel(novel)
                # print(res[0:2] if res is not None else '')
                idx += 1
                print("{}/{}".format(idx, c_len), end="\r", file=sys.stderr)
                if res:
                    sd = os.path.join(self.SAVEDIR, res[0])
                    sf = os.path.join(sd, res[1])
                    os.makedirs(sd, exist_ok=True)
                    self.__save_text(sf, res[2])

    @classmethod
    def __parse_novel(cls, novel: str) -> tuple[str, str, str] | None:
        # print(novel)
        f = codecs.open(novel, "r", "shiftjis", "ignore")
        source = bs4.BeautifulSoup(f.read(), "html.parser")
        cls.__decompose(source)

        novel_title = source.find("h1", class_="title")
        novel_author = source.find("h2", class_="author")
        novel_content = source.find("div", class_="main_text")

        if (
            isinstance(novel_author, bs4.element.Tag)
            and isinstance(novel_author.string, str)
            and isinstance(novel_title, bs4.element.Tag)
            and isinstance(novel_title.string, str)
            and isinstance(novel_content, bs4.element.Tag)
            and isinstance(novel_content.text, str)
        ):
            return (
                cls.__shrink(novel_author.string),
                novel_title.string,
                novel_content.text,
            )
        else:
            return None

    @staticmethod
    def __shrink(t: str, length: int = 100) -> str:
        t = t.replace("　", "_")
        if len(t) > 100:
            return t[0:100] + "…"
        else:
            return t

    @staticmethod
    def __save_text(path: str, text: str) -> None:
        print(text, file=open(path, "w"))

    @staticmethod
    def __decompose(bs_: bs4.BeautifulSoup) -> None:
        try:
            for rt in bs_("rt"):
                rt.decompose()
            for rp in bs_("rp"):
                rp.decompose()
        except AttributeError as err:
            print(err)

    @staticmethod
    def check_exist(path: str) -> bool:
        return os.path.exists(path)

    @classmethod
    def get_cards(cls) -> list[str]:
        return [c for c in os.listdir(cls.AOZORA_CARDS) if c.isdecimal()]

    @classmethod
    def get_novels(cls, card: str) -> list[str]:
        f = cls.AOZORA_FILES.format(card)
        return glob.glob(os.path.join(f, "*.html"))


if __name__ == "__main__":
    AozoraParser().parse()
