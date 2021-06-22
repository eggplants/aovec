# aovec

[![PyPI version](https://badge.fury.io/py/aovec.svg)](https://badge.fury.io/py/aovec)

- Make Word2Vec from [aozorabunko/aozorabunko](https://github.com/aozorabunko/aozorabunko)
- This code is inspired by [sheepover96/aozora_analyzer](https://github.com/sheepover96/aozora_analyzer):
  - <https://serenard.hatenablog.com/entry/2019/04/28/170322>

## Requirements

- Git
- MeCab

## How to use

```bash
$ pip install aovec
# clone aozorabunko/aozorabunko (>20GB)
$ aovec c
# parse html files and write to results to novels/
$ aovec parse
# make word2vec and write to aozora_model.model
$ aovec mkvec
```
