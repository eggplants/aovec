import MeCab


def make_tagger() -> MeCab.Tagger:
    tagger: MeCab.Tagger
    try:
        tagger = MeCab.Tagger("")
    except RuntimeError:
        tagger = MeCab.Tagger("-r/etc/mecabrc")

    return tagger


def parse(text: str) -> None:
    t = make_tagger()
    t.parse("")
    node = t.parseToNode(text)
    while node:
        word = node.surface
        pos = node.feature.split(",")
        part = pos[0]
        print('"{}:{}"({})'.format(word, pos[6], part))
        node = node.next


if __name__ == "__main__":
    parse("これはテストです！！！！")
    parse("試験的にMeCabを使ってみます。果たして―――")
