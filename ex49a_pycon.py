from ex48.parser import *
x = parse_sentence([('verb', 'run'), ('direction', 'north')])
x.subject
x.verb
x.object
x = parse_sentence([('noun', 'bear'), ('verb', 'eat'), ('stop', 'the'),
                    ('noun', 'honey')])
x.subject
x.verb
x.object
