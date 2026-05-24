from ast_nodes import *

# ==========================================
# CODE GENERATOR
# ==========================================

class CodeGenerator:

    def __init__(self):

        self.indent_level = 0

    # ======================================
    # INDENTATION
    # ======================================

    def indent(self):

        return "    " * self.indent_level

    # ======================================
    # MAIN GENERATE
    # ======================================

    def generate(self, node):

        method_name = f'gen_{type(node).__name__}'

        method = getattr(self, method_name)

        return method(node)

    # ======================================
    # PROGRAM
    # ======================================

    def gen_Program(self, node):

        output = []

        for stmt in node.statements:

            output.append(
                self.generate(stmt)
            )

        return '\n'.join(output)

    # ======================================
    # VALUES
    # ======================================

    def gen_Number(self, node):

        return str(node.value)

    def gen_String(self, node):

        return f'"{node.value}"'

    def gen_Identifier(self, node):

        return node.name

    # ======================================
    # BINARY OP
    # ======================================

    def gen_BinaryOp(self, node):

        left = self.generate(node.left)

        right = self.generate(node.right)

        return f'{left} {node.op} {right}'

    # ======================================
    # ASSIGNMENT
    # ======================================

    def gen_Assignment(self, node):

        value = self.generate(node.value)

        return (
            self.indent()
            + f'{node.name} = {value}'
        )

    # ======================================
    # PRINT
    # ======================================

    def gen_Print(self, node):

        value = self.generate(node.value)

        return (
            self.indent()
            + f'print({value})'
        )

    # ======================================
    # IF / ELSE
    # ======================================

    def gen_If(self, node):

        condition = self.generate(node.condition)

        result = (
            self.indent()
            + f'if {condition}:\n'
        )

        # Increase indentation
        self.indent_level += 1

        for stmt in node.body:

            result += (
                self.generate(stmt)
                + '\n'
            )

        # Decrease indentation
        self.indent_level -= 1

        # ELSE
        if node.else_body:

            result += (
                self.indent()
                + 'else:\n'
            )

            self.indent_level += 1

            for stmt in node.else_body:

                result += (
                    self.generate(stmt)
                    + '\n'
                )

            self.indent_level -= 1

        return result.rstrip()

    # ======================================
    # WHILE
    # ======================================

    def gen_While(self, node):

        condition = self.generate(node.condition)

        result = (
            self.indent()
            + f'while {condition}:\n'
        )

        self.indent_level += 1

        for stmt in node.body:

            result += (
                self.generate(stmt)
                + '\n'
            )

        self.indent_level -= 1

        return result.rstrip()

    # ======================================
    # FUNCTION
    # ======================================

    def gen_Function(self, node):

        params = ', '.join(node.params)

        result = (
            self.indent()
            + f'def {node.name}({params}):\n'
        )

        self.indent_level += 1

        for stmt in node.body:

            result += (
                self.generate(stmt)
                + '\n'
            )

        self.indent_level -= 1

        return result.rstrip()

    # ======================================
    # RETURN
    # ======================================

    def gen_Return(self, node):

        value = self.generate(node.value)

        return (
            self.indent()
            + f'return {value}'
        )

    # ======================================
    # FUNCTION CALL
    # ======================================

    def gen_FunctionCall(self, node):

        args = []

        for arg in node.args:

            args.append(
                self.generate(arg)
            )

        return (
            f'{node.name}({", ".join(args)})'
        )