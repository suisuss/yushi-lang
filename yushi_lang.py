from lexer import Lexer
from parser import Parser
from evaluator import Evaluator
import pprint

pp = pprint.PrettyPrinter(indent=4)


def main():
    filename = 'test_code/hello_world.yu'
    file = open(filename, 'r')

    lexer = Lexer(file)
    parser = Parser(lexer.tokens)


    lexer.tokenizer()
    print("-" * 20)
    print("TOKENS:")
    pp.pprint(lexer.tokens)

    parser.build_AST()
    print("-" * 20)
    print("AST:")
    pp.pprint(parser.AST)

    evaluator = Evaluator(parser.AST)

    print("-" * 20)
    print("OUTPUT:")
    evaluator.run(parser.AST)


if __name__ == "__main__":
    main()



