from . import _MeCab
from typing import Any

VERSION: Any

class Tagger(_MeCab.Tagger):
    def __init__(self, rawargs: str = ...) -> None: ...

class Model(_MeCab.Model):
    def __init__(self, rawargs: str = ..., error_check: bool = ...) -> None: ...

# Names in __all__ with no definition:
#   DictionaryInfo
#   Lattice
#   MECAB_ALLOCATE_SENTENCE
#   MECAB_ALL_MORPHS
#   MECAB_ALTERNATIVE
#   MECAB_ANY_BOUNDARY
#   MECAB_BOS_NODE
#   MECAB_EON_NODE
#   MECAB_EOS_NODE
#   MECAB_INSIDE_TOKEN
#   MECAB_MARGINAL_PROB
#   MECAB_NBEST
#   MECAB_NOR_NODE
#   MECAB_ONE_BEST
#   MECAB_PARTIAL
#   MECAB_SYS_DIC
#   MECAB_TOKEN_BOUNDARY
#   MECAB_UNK_DIC
#   MECAB_UNK_NODE
#   MECAB_USR_DIC
#   Node
#   Path
#   SWIG_PyStaticMethod_New
