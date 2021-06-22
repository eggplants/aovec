# aovec

- Make Word2Vec from [aozorabunko/aozorabunko](https://github.com/aozorabunko/aozorabunko)
- Refactoring:
  - <https://serenard.hatenablog.com/entry/2019/04/28/170322>

## How to use

```bash
# clone aozorabunko/aozorabunko (>20GB)
$ python AozoraCloner.py
# parse html files and write to results to novels/
$ python AozoraParser.py
# make word2vec and write to aozora_model.model
$ python AozoraVecMaker.py
```
