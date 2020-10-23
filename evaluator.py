
class Evaluator:
    '''
    Evaluator executes code according to the AST
    '''

    def __init__(self, AST):
        self.AST = AST

    def run(self, node):
        if isinstance(node, list):
            '''
            If a node in the AST is a list then it's describing a function.
            '''
            for n in node:
                for k, v in n.items():
                    self.execute([k, v])

        elif isinstance(node, dict):
            '''
            If a node in the AST is a dict then it's describing a subroutines within a function?
              - IDK what terminology to use here.
            '''
            for k, v in node.items():
                self.execute((k, v))

    def execute(self, instruction):
        if isinstance(instruction[1], list):
            '''
            If the value of the instruction is a list then it's a function.
            '''
            self.run(instruction[1])

        elif instruction[0] == 'print':
            self.print(instruction[1])
        
        elif instruction[0] == 'stop':
            self.stop()

        elif instruction[0] == 'do':
            self.do(instruction[1])

    def print(self, value):
        print(value)

    def stop(self):
        quit()

    def do(self, value):
        for node in self.AST:
            if value in node:
                self.run(node[value])



