import glob
import os
import sys
from typing import Any, List, Optional

import MeCab  # type: ignore[import]
from gensim.models import Word2Vec  # type: ignore[import]


class AozoraVecMaker:
    __pwd__ = os.getcwd()
    STOPWORDS = [
        "これ",
        "それ",
        "あれ",
        "この",
        "その",
        "あの",
        "ここ",
        "そこ",
        "あそこ",
        "こちら",
        "どこ",
        "だれ",
        "なに",
        "なん",
        "何",
        "私",
        "貴方",
        "貴方方",
        "我々",
        "私達",
        "あの人",
        "あのかた",
        "彼女",
        "彼",
        "です",
        "あります",
        "おります",
        "います",
        "は",
        "が",
        "の",
        "に",
        "を",
        "で",
        "え",
        "から",
        "まで",
        "より",
        "も",
        "どの",
        "と",
        "し",
        "それで",
        "しかし",
        "",
        *[chr(i) for i in range(12354, 12436)],
    ]

    def __init__(self, novel_dir: str = "novel") -> None:
        self.novel_dir = os.path.join(self.__pwd__, novel_dir)
        if not os.path.exists(self.novel_dir):
            raise FileExistsError(self.novel_dir)
        sys.stdout = sys.stderr = open(os.devnull, "w")
        self.__tagger = self.__make_tagger()
        sys.stdout, sys.stderr = sys.__stdout__, sys.__stderr__

    def make_model(
        self,
        save_modelname: str = "aozora_model",
        epochs: int = 5,
        vector_size: int = 100,
        min_count: int = 5,
        window: int = 5,
        workers: int = 3,
        binary: bool = False,
        both: bool = False,
    ) -> None:
        def t(line: str) -> List[Any]:
            return self.tokenizer(line, part_use=None)

        all_novel_lines = []
        ps = glob.glob(os.path.join(self.novel_dir, "*", "*"))
        ps_len = len(ps)
        for idx, p in enumerate(ps):
            print("{}/{}".format(idx + 1, ps_len), end="\r", file=sys.stderr)
            f = open(p, "r")
            novel_content = f.read()
            novel_text_lines = novel_content.split("\n")

            tokenized_novel_text_lines = [t(line) for line in novel_text_lines]
            all_novel_lines.extend(tokenized_novel_text_lines)

        model = Word2Vec(
            all_novel_lines,
            epochs=epochs,
            vector_size=vector_size,
            min_count=min_count,
            window=window,
            workers=workers,
        )
        self.__save_model(model, save_modelname, binary, both)

    def __save_model(
        self, model: Word2Vec, save_modelname: str, binary: bool, both: bool
    ) -> None:
        model_name = os.path.join(self.__pwd__, save_modelname + ".model")
        kv_name = os.path.join(self.__pwd__, save_modelname + ".kv")

        if both:
            model.save(model_name)
            model.wv.save_word2vec_format(kv_name + ".bin", binary=True)
            model.wv.save_word2vec_format(kv_name)
            return None

        model.save(model_name)
        if binary:
            model.wv.save_word2vec_format(kv_name + ".bin", binary=True)
        else:
            model.wv.save_word2vec_format(kv_name)

    def tokenizer(
        self, words: str, part_use: Optional[List[str]] = ["名詞", "形容詞"]
    ) -> List[Any]:
        self.__tagger.parse("")
        nodes: MeCab.Tagger = self.__tagger.parseToNode(words)
        tokenized = []
        while nodes:
            word = nodes.surface
            pos = nodes.feature.split(",")
            part = pos[0]
            if len(part) >= 7:
                word = pos[6]

            if self.__is_word(word, part, part_use):
                tokenized.append(word)

            nodes = nodes.next

        return tokenized

    @classmethod
    def __is_word(cls, word: str, part: str, part_use: Optional[List[str]]) -> bool:
        is_stop = word not in cls.STOPWORDS
        is_part = part is None or part_use is None
        return is_stop and (
            is_part
            or (type(part_use) is list and part in part_use and not word.isalnum())
        )

    @staticmethod
    def __make_tagger() -> MeCab.Tagger:
        try:
            tagger = MeCab.Tagger("")
        except RuntimeError:
            tagger = MeCab.Tagger("-r/etc/mecabrc")

        return tagger


if __name__ == "__main__":
    AozoraVecMaker().make_model()
