class Lexer:
    '''
    The lexer converts lines of code into tokens. Performs lexical analysis
    '''

    def __init__(self, data):
        self.data = data
        self.tokens = []
        self.keywords = [
            "print",
            "do",
            "stop"
        ]
    
    def tokenizer(self):
        for line in self.data:
            tmp = []
            tid = ''

            for character in line:

                if character == '"' and tid == '':
                    tid = 'char'
                    tmp = []

                elif character == '"' and tid == 'char':
                    self.tokens.append({'id': tid, 'value': ''.join(tmp)})
                    tid = ''
                    tmp = []

                elif character == ':':
                    self.tokens.append({'id': 'label', 'value': ''.join(tmp)})
                    tmp = []

                elif ''.join(tmp) in self.keywords:
                    self.tokens.append({'id': 'keyword', 'value': ''.join(tmp)})
                    tmp = []

                elif character == '\n':
                    if len(tmp) > 0:
                        self.tokens.append({'id': 'atom', 'value': ''.join(tmp)})
                        tmp = []

                elif (character == ' ' or character == "\t") and tid != 'char':
                    continue

                else:
                    tmp.append(character)
