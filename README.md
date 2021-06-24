# aovec

[![Model scheduled release](https://github.com/eggplants/aovec/actions/workflows/model_release.yml/badge.svg)](https://github.com/eggplants/aovec/actions/workflows/model_release.yml)
[![Release Package](https://github.com/eggplants/aovec/actions/workflows/release.yml/badge.svg)](https://github.com/eggplants/aovec/actions/workflows/release.yml) [![PyPI version](https://badge.fury.io/py/aovec.svg)](https://badge.fury.io/py/aovec)

- Make Word2Vec from [aozorabunko/aozorabunko](https://github.com/aozorabunko/aozorabunko)

- Pre-built models are available from `week*` [Releases](https://github.com/eggplants/aovec/releases).

[![model](https://img.shields.io/badge/dynamic/json.svg?label=Model&query=$[0].assets[0].browser_download_url&url=https://api.github.com/repos/eggplants/aovec/releases)](https://github.com/eggplants/aovec/releases)

## Requirements

- Git
- MeCab
  - MeCab Checker: [src/check_mecab.py](https://github.com/eggplants/aovec/blob/master/src/check_mecab.py)

## How to use

- Make `*.model` file

```bash
# Install from pypi
$ pip install aovec
# Clone aozorabunko/aozorabunko (>20GB)
$ aovec clone
# Parse html files and write to results to novels/
$ aovec parse
# Make word2vec and write to aozora_model.model
$ aovec mkvec
```

- Use from Python (See: [official document](https://radimrehurek.com/gensim/models/word2vec.html))

```python
from gensim.models import Word2Vec, KeyedVectors

model = Word2Vec.load('aozora_model.model')

# or...
model = KeyedVectors.load_word2vec_format('aozora_model.kv',
                                          unicode_errors='ignore')
# or...
model = KeyedVectors.load_word2vec_format('aozora_model.kv.bin',
                                          binary=True,
                                          unicode_errors='ignore')
```

## (Optional)Set up `mecab-ipadic-neologd` on Ubuntu

- Download and install

```bash
$ sudo apt install build-essential
$ git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd neologd && cd $_
$ sudo bin/install-mecab-ipadic-neologd -y
$ sudo mv /usr/lib/*/mecab/dic/mecab-ipadic-neologd /var/lib/mecab/dic
```

- Update `/etc/mecabrc`

```bash
$ sudo cp /etc/mecabrc /stc/mecabrc.bak
$ sudo sed -i 's_^dicdir.*_; &\'$'\ndicdir = /var/lib/mecab/dic/mecab-ipadic-neologd_' /etc/mecabrc
```

```diff
--- /etc/mecabrc.bak
+++ /etc/mecabrc
@@ -3,7 +3,8 @@
 ;
 ; $Id: mecabrc.in,v 1.3 2006/05/29 15:36:08 taku-ku Exp $;
 ;
-dicdir = /var/lib/mecab/dic/debian
+; dicdir = /var/lib/mecab/dic/debian
+dicdir = /var/lib/mecab/dic/mecab-ipadic-neologd

 ; userdic = /home/foo/bar/user.dic
```

## Help

```bash
usage: aovec [-h] [-V] {clone,c,parse,p,mkvec,m} ...

Make Word2Vec from aozorabunko/aozorabunko

positional arguments:
  {clone,c,parse,p,mkvec,m}
    clone (c)           clone aozorabunko/aozorabunko (>20GB)
    parse (p)           parse html files and write to results
    mkvec (m)           make word2vec and write to *.model

optional arguments:
  -h, --help            show this help message and exit
  -V, --version         show program's version number and exit
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
usage: aovec mkvec [-h] [-d DIR] [-o NAME] [-e INT] [-v INT] [-m INT] [-w INT]
                   [-p INT] [-b] [--both]

optional arguments:
  -h, --help            show this help message and exit
  -d DIR, --parsedir DIR
                        directory name of saved parsing results (default:
                        novels)
  -o NAME, --model NAME
                        name of word2vec model (default: aozora_model)
  -e INT, --epochs INT  number of word2vec epochs (default: 5)
  -v INT, --vector_size INT
                        dimensionality of the word vectors (default: 1000)
  -m INT, --min_count INT
                        ignore words total frequency lower than this (default:
                        5)
  -w INT, --window INT  window size of words before and for learning (default:
                        5)
  -p INT, --workers INT
                        worker threads (default: 3)
  -b, --binary          save model files as one binary (default: False)
  --both                save model files as both row data and binary (default:
                        False)
```

## License

MIT
