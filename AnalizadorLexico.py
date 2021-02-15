# ----------------------------------------------------------------------
# AnalizadorLexicoctokens.py
#
# Grupo # 7
# 
# ----------------------------------------------------------------------

# Librerías
import ply.lex as lex
import re
import codecs
import os
import sys

# Palabras reservadas y tokens

tokens = [
    # Literals (identifier, integer constant, float constant, string constant, char const)
    'ID', 'TYPEID', 'INTEGER', 'FLOAT', 'STRING', 'CHARACTER',
    # Operators (+,-,*,/,%,|,&,~,^,<<,>>, ||, &&, !, <, <=, >, >=, ==, !=)
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'MODULO',
    'OR', 'AND', 'NOT', 'XOR', 'LSHIFT', 'RSHIFT',
    'LOR', 'LAND', 'LNOT',
    'LT', 'LE', 'GT', 'GE', 'EQ', 'NE',
    # Assignment (=, *=, /=, %=, +=, -=, <<=, >>=, &=, ^=, |=)
    'EQUALS', 'TIMESEQUAL', 'DIVEQUAL', 'MODEQUAL', 'PLUSEQUAL', 'MINUSEQUAL',
    'LSHIFTEQUAL','RSHIFTEQUAL', 'ANDEQUAL', 'XOREQUAL', 'OREQUAL',
    # Increment/decrement (++,--)
    'INCREMENT', 'DECREMENT',
    # Structure dereference (->)
    'ARROW',
    # Ternary operator (?)
    'TERNARY',
    # Delimeters ( ) [ ] { } , . ; :
    'LPAREN', 'RPAREN',
    'LBRACKET', 'RBRACKET',
    'LBRACE', 'RBRACE',
    'COMMA', 'PERIOD', 'SEMI', 'COLON',
    # Ellipsis (...)
    'ELLIPSIS',
    # Preprocess
    'PREPROCESS'
]

# Operators
t_PLUS             = r'\+'
t_MINUS            = r'-'
t_TIMES            = r'\*'
t_DIVIDE           = r'/'
t_MODULO           = r'%'
t_OR               = r'\|'
t_AND              = r'&'
t_NOT              = r'~'
t_XOR              = r'\^'
t_LSHIFT           = r'<<'
t_RSHIFT           = r'>>'
t_LOR              = r'\|\|'
t_LAND             = r'&&'
t_LNOT             = r'!'
t_LT               = r'<'
t_GT               = r'>'
t_LE               = r'<='
t_GE               = r'>='
t_EQ               = r'=='
t_NE               = r'!='

# Assignment operators
t_EQUALS           = r'='
t_TIMESEQUAL       = r'\*='
t_DIVEQUAL         = r'/='
t_MODEQUAL         = r'%='
t_PLUSEQUAL        = r'\+='
t_MINUSEQUAL       = r'-='
t_LSHIFTEQUAL      = r'<<='
t_RSHIFTEQUAL      = r'>>='
t_ANDEQUAL         = r'&='
t_OREQUAL          = r'\|='
t_XOREQUAL         = r'\^='

# Increment/decrement
t_INCREMENT        = r'\+\+'
t_DECREMENT        = r'--'

# ->
t_ARROW            = r'->'

# ?
t_TERNARY          = r'\?'

# Delimeters
t_LPAREN           = r'\('
t_RPAREN           = r'\)'
t_LBRACKET         = r'\['
t_RBRACKET         = r'\]'
t_LBRACE           = r'\{'
t_RBRACE           = r'\}'
t_COMMA            = r','
t_PERIOD           = r'\.'
t_SEMI             = r';'
t_COLON            = r':'
t_ELLIPSIS         = r'\.\.\.'

# Identifiers
t_ID = r'[A-Za-z_][A-Za-z0-9_]*'

# Integer literal
t_INTEGER = r'\d+([uU]|[lL]|[uU][lL]|[lL][uU])?'

# Floating literal
t_FLOAT = r'((\d+)(\.\d+)(e(\+|-)?(\d+))? | (\d+)e(\+|-)?(\d+))([lL]|[fF])?'

# String literal
t_STRING = r'\"([^\\\n]|(\\.))*?\"'

# Character constant 'c' or L'c'
t_CHARACTER = r'(L)?\'([^\\\n]|(\\.))*?\''

# Comment (C-Style)
def t_COMMENT(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += 1
    # t.lexer.lineno += t.value.count('\n')
    pass

# Comment (C++-Style)
def t_CPPCOMMENT(t):
    r'//.*'
    t.lexer.lineno += 1
    pass

def t_PREPROCESS(t):
    r'\#include(.)*[<|\"|\'](.*)\.h[>|\"|\']'
    return t

def t_newline(t):
    r'\n'
    t.lexer.lineno += len(t.value)

def t_rc(t):
    r'\r'
    #t.lexer.lineno += len(t.value)

def t_WS(t):
    r'\s'
    pass

def t_error(t):
    print("Caracter ilegal: %5s " %t.value[0])
    t.lexer.skip(1)

# Funcion para elegir el archivo de test

def buscarFichero(directorio):
    ficheros = []
    numArchivo = ''
    respuesta = False
    cont = 1

    for base, dirs, files in os.walk(directorio):
        ficheros.append(files)
    
    for file in files:
        print(str(cont) + ". " + file)
        cont = cont + 1
    
    while respuesta == False:
        numArchivo = input('\nNumero de archivo para el test:')
        for file in files:
            if file == files[int(numArchivo)-1]:
                respuesta = True
                break
        
        print("Archivo elegido: %s " %files[int(numArchivo)-1])

        return files[int(numArchivo)-1]

# Seleccion de directorio y archivo

directorio = os.path.dirname(__file__)+"/test/"
archivo = buscarFichero(directorio)
test = directorio + archivo
fp = codecs.open(test, "r", "utf-8")
codigo = fp.read()
fp.close()

# Creacion del Lexer

analizador = lex.lex()

analizador.input(codigo)

# Analisis, reconocimiento y guardado de los tokens

save = os.path.dirname(__file__) + "/" + archivo + " - TokenList.txt"
fs = codecs.open(save, "wb", "utf-8")
while True:
    tok = analizador.token()
    if not tok: 
        break
    print(tok)
    fs.write(str(tok) + "\n")

fs.close()




