import glob
import os
from typing import Any, List, Optional

import MeCab
import word2vec


class AozoraVecMaker():
    __pwd__ = os.getcwd()
    STOPWORDS = ['これ', 'それ', 'あれ', 'この', 'その',
                 'あの', 'ここ', 'そこ', 'あそこ', 'こちら',
                 'どこ', 'だれ', 'なに', 'なん', '何',
                 '私', '貴方', '貴方方', '我々', '私達',
                 'あの人', 'あのかた', '彼女', '彼', 'です',
                 'あります', 'おります', 'います', 'は', 'が',
                 'の', 'に', 'を', 'で', 'え',
                 'から', 'まで', 'より', 'も', 'どの',
                 'と', 'し', 'それで', 'しかし', '',
                 *[chr(i) for i in range(12354, 12436)]]

    def __init__(self, novel_dir: str = 'novel'):
        self.novel_dir = os.path.join(self.__pwd__, novel_dir)
        if not os.path.exists(self.novel_dir):
            raise FileExistsError(self.novel_dir)

    @classmethod
    def make_model(cls, save_modelname: str = 'aozora_model.model') -> None:
        def t(line: str) -> List[Any]:
            return cls.tokenizer(line, part_use=None)

        all_novel_lines = []

        for p in glob.glob(os.path.join(cls.novel_dir, '*', '*')):
            f = open(p, 'r')
            novel_content = f.read()
            novel_text_lines = novel_content.split('\n')

            tokenized_novel_text_lines = [t(line)
                                          for line in novel_text_lines]
            all_novel_lines.extend(tokenized_novel_text_lines)

        model = word2vec.Word2Vec(all_novel_lines, iter=100)
        model.save(save_modelname)

    @classmethod
    def tokenizer(cls, words: str,
                  part_use: Optional[List[str]] = ['名詞', '形容詞'],
                  normalize_word: bool = True) -> List[Any]:
        t = cls.__make_tagger()
        t.parse('')
        mecab_word_nodes: MeCab.Tagger = t.parseToNode(words)
        tokenized = []
        while mecab_word_nodes:
            elements = mecab_word_nodes.feature
            word = mecab_word_nodes.surface
            element_list = elements.split(',')
            if normalize_word:
                word = element_list[6]
            part = element_list[0]

            if cls.__is_word(word, part, part_use):
                tokenized.append(word)

            mecab_word_nodes = mecab_word_nodes.next

        return tokenized

    @classmethod
    def __is_word(cls, word: str, part: str, part_use: Optional[List[str]]) -> bool:
        is_stop = word not in cls.STOPWORDS
        is_part1 = part is None or part_use is None
        is_part2 = part in part_use and not word.encode('utf-8').isalnum()
        return is_stop and (is_part1 or is_part2)

    @staticmethod
    def __make_tagger() -> MeCab.Tagger:
        try:
            tagger = MeCab.Tagger('-Ochasen')
        except Exception:
            tagger = MeCab.Tagger('-r/etc/mecabrc -Ochasen')

        return tagger


if __name__ == '__main__':
    AozoraVecMaker().make_model()
