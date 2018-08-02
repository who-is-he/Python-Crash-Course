"""
regex'd with 
    find: \t'(\w*)':
    replace: jargon['$1']:
not perfect, but pretty cool
"""

from collections import OrderedDict

jargon = OrderedDict()

jargon['inheritance'] = 'the mechanism of basing an object or class upon another object (prototypal inheritance) or class (class-based inheritance), retaining the same implementation;'
jargon['object'] = 'a variable, a data structure, a function, or a method, and as such, is a value in memory referenced by an identifier.'
jargon['class'] = 'an extensible program-code-template for creating objects, providing initial values for state (member variables) and implementations of behavior (member functions or methods)'
jargon['table'] = 'a data structure used to organize information, just as it is on paper.'
jargon['array'] = 'a storage array, also called a disk array, is a data storage system that is used for block-based, file-based or object storage.'
jargon['source code'] = 'any collection of code, possibly with comments, written using a human-readable programming language, usually as plain text.'
jargon['algorithm'] = 'an unambiguous specification of how to solve a class of problems.'
jargon['function'] = '(aka subroutine) a sequence of program instructions that performs a specific task, packaged as a unit.'
jargon['method'] = 'a procedure associated with a message and an object.'
jargon['property'] = 'a special sort of class member, intermediate in functionality between a field (or data member) and a method.'

for word, definition in jargon.items():
    print(word.title() + ' - ' + str(definition))