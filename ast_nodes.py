# ==========================================
# PROGRAM
# ==========================================

class Program:

    def __init__(self, statements):

        self.statements = statements

# ==========================================
# BASIC VALUES
# ==========================================

class Number:

    def __init__(self, value):

        self.value = value


class String:

    def __init__(self, value):

        self.value = value


class Identifier:

    def __init__(self, name):

        self.name = name

# ==========================================
# EXPRESSIONS
# ==========================================

class BinaryOp:

    def __init__(self, left, op, right):

        self.left = left
        self.op = op
        self.right = right

# ==========================================
# ASSIGNMENT
# ==========================================

class Assignment:

    def __init__(self, name, value):

        self.name = name
        self.value = value

# ==========================================
# PRINT
# ==========================================

class Print:

    def __init__(self, value):

        self.value = value

# ==========================================
# IF / ELSE
# ==========================================

class If:

    def __init__(self, condition, body, else_body=None):

        self.condition = condition
        self.body = body
        self.else_body = else_body

# ==========================================
# WHILE LOOP
# ==========================================

class While:

    def __init__(self, condition, body):

        self.condition = condition
        self.body = body

# ==========================================
# FUNCTION
# ==========================================

class Function:

    def __init__(self, name, params, body):

        self.name = name
        self.params = params
        self.body = body

# ==========================================
# RETURN
# ==========================================

class Return:

    def __init__(self, value):

        self.value = value

# ==========================================
# FUNCTION CALL
# ==========================================

class FunctionCall:

    def __init__(self, name, args):

        self.name = name
        self.args = args