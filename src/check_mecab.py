import MeCab


def make_tagger() -> MeCab.Tagger:
    tagger: MeCab.Tagger
    try:
        tagger = MeCab.Tagger('')
    except RuntimeError:
        tagger = MeCab.Tagger('-r/etc/mecabrc')

    return tagger


def parse(text: str = "これはテストです！！！！") -> None:
    t = make_tagger()
    t.parse('')
    node = t.parseToNode(text)
    while node:
        word = node.surface
        pos = node.feature.split(",")[1]
        print('{0} , {1}'.format(word, pos))
        node = node.next


if __name__ == '__main__':
    parse()
