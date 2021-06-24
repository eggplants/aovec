import argparse
from argparse import Namespace as NS
from typing import List, Optional

from aovec import __version__

from .AozoraCloner import AozoraCloner
from .AozoraParser import AozoraParser
from .AozoraVecMaker import AozoraVecMaker


def command_clone(args: NS) -> None:
    AozoraCloner().clone()


def command_parse(args: NS) -> None:
    AozoraParser(args.savedir).parse()


def command_mkvec(args: NS) -> None:
    AozoraVecMaker(args.parsedir).make_model(
        save_modelname=args.model, epochs=args.epochs,
        vector_size=args.vector_size, min_count=args.min_count,
        window=args.window, workers=args.workers,
        binary=args.binary, both=args.both)


def check_positive(v: str) -> int:
    if int(v) <= 0:
        raise argparse.ArgumentTypeError(
            "%s is an invalid natural number" % int(v))
    return int(v)


def make_argparser() -> argparse.ArgumentParser:
    """Parse arguments."""

    parser = argparse.ArgumentParser(
        prog='aovec',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description='Make Word2Vec from aozorabunko/aozorabunko')

    parser.add_argument('-V', '--version', action='version',
                        version='%(prog)s {}'.format(__version__))

    subparsers = parser.add_subparsers()

    parser_clone = subparsers.add_parser(
        'clone', aliases=['c'], help='clone aozorabunko/aozorabunko (>20GB)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,)
    parser_clone.set_defaults(handler=command_clone)

    parser_parse = subparsers.add_parser(
        'parse', aliases=['p'], help='parse html files and write to results',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,)
    parser_parse.add_argument(
        '-d', '--savedir', default='novels',
        metavar='DIR', help='directory name of saving results')
    parser_parse.set_defaults(handler=command_parse)

    parser_mkvec = subparsers.add_parser(
        'mkvec', aliases=['m'], help='make word2vec and write to *.model',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,)
    parser_mkvec.add_argument(
        '-d', '--parsedir', default='novels',
        metavar='DIR', help='directory name of saved parsing results')
    parser_mkvec.add_argument(
        '-o', '--model', default='aozora_model',
        metavar='NAME', help='name of word2vec model')
    parser_mkvec.add_argument(
        '-e', '--epochs', default=5, type=check_positive,
        metavar='INT', help='number of word2vec epochs')
    parser_mkvec.add_argument(
        '-v', '--vector_size', default=1000, type=check_positive,
        metavar='INT', help='dimensionality of the word vectors')
    parser_mkvec.add_argument(
        '-m', '--min_count', default=5, type=check_positive,
        metavar='INT', help='ignore words total frequency lower than this')
    parser_mkvec.add_argument(
        '-w', '--window', default=5, type=check_positive,
        metavar='INT', help='window size of words before and for learning')
    parser_mkvec.add_argument(
        '-p', '--workers', default=3, type=check_positive,
        metavar='INT', help='worker threads')
    parser_mkvec.add_argument(
        '-b', '--binary', action='store_true',
        help='save model files as one binary')
    parser_mkvec.add_argument(
        '--both', action='store_true',
        help='save model files as both row data and binary')

    parser_mkvec.set_defaults(handler=command_mkvec)

    return parser


def parse(test: Optional[List[str]] = None) -> None:
    parser = make_argparser()
    args = parser.parse_args(test)

    if hasattr(args, 'handler'):
        args.handler(args)
    else:
        parser.print_help()


def main() -> None:
    parse()


if __name__ == '__main__':
    main()
