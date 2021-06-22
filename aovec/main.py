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
    AozoraVecMaker(args.parsedir).make_model(args.model)


def make_argparser() -> argparse.ArgumentParser:
    """Parse arguments."""

    parser = argparse.ArgumentParser(
        prog='aovec',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description='Make Word2Vec from aozorabunko/aozorabunko')

    parser.add_argument('-V', '--version', action='version',
                        version='%(prog)s {}'.format(__version__))

    subparsers = parser.add_subparsers()

    parser_clone = subparsers.add_parser('clone', help='see `clone -h`')
    parser_clone.set_defaults(handler=command_clone)

    parser_parse = subparsers.add_parser('parse', help='see `parse -h`')
    parser_parse.add_argument(
        '-r', '--savedir', default='novels',
        metavar='DIR', help='directory name of saving results')
    parser_parse.set_defaults(handler=command_parse)

    parser_mkvec = subparsers.add_parser('mkvec', help='see `parse -h`')
    parser_mkvec.add_argument(
        '-r', '--parsedir', default='novels',
        metavar='DIR', help='directory name of saved parsing results ')
    parser_mkvec.add_argument(
        '-o', '--model', default='aozora_model.model',
        metavar='NAME', help='name of word2vec model')

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
