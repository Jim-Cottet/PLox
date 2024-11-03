from enum import Enum

class TypeDef(Enum):
    EXPR_UNARY = 1;
    EXPR_GROUPING = 2;
    EXPR_BINARY = 3;
    EXPR_LITERAL = 4;
    EXPR_VARIABLE = 5;
    EXPR_ASSIGN = 6;
