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
# Install from pypi
$ pip install aovec
# Clone aozorabunko/aozorabunko (>20GB)
$ aovec c
# Parse html files and write to results to novels/
$ aovec parse
# Make word2vec and write to aozora_model.model
$ aovec mkvec
```

## Help

```bash
$ aovec -h
usage: aovec [-h] [-V] {clone,parse,mkvec} ...

Make Word2Vec from aozorabunko/aozorabunko

positional arguments:
  {clone,parse,mkvec}
    clone              clone aozorabunko/aozorabunko (>20GB)
    parse              parse html files and write to results
    mkvec              make word2vec and write to *.model

optional arguments:
  -h, --help           show this help message and exit
  -V, --version        show program's version number and exit
```

```bash
$ aovec clone -h
usage: aovec clone [-h]

optional arguments:
  -h, --help  show this help message and exit
```

```bash
$ aovec parse -h
usage: aovec parse [-h] [-d DIR]

optional arguments:
  -h, --help            show this help message and exit
  -d DIR, --savedir DIR
                        directory name of saving results (default: novels)
```

```bash
$ aovec mkvec -h
usage: aovec mkvec [-h] [-d DIR] [-o NAME]

optional arguments:
  -h, --help            show this help message and exit
  -d DIR, --parsedir DIR
                        directory name of saved parsing results (default:
                        novels)
  -o NAME, --model NAME
                        name of word2vec model (default: aozora_model.model)
```
