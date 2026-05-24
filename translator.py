import sys

from lexer import lexer

from parser import parser, has_error

from code_generator import CodeGenerator

# ==========================================
# CHECK ARGUMENTS
# ==========================================

if len(sys.argv) < 2:

    print("\nUsage:")
    print("python translator.py program.yl\n")

    exit()

# ==========================================
# INPUT FILE
# ==========================================

filename = sys.argv[1]

# ==========================================
# CHECK FILE TYPE
# ==========================================

if not filename.endswith(".yl"):

    print("\nError: Input file must be .yl\n")

    exit()

# ==========================================
# READ SOURCE FILE
# ==========================================

try:

    with open(filename, "r", encoding="utf-8") as file:

        source_code = file.read()

except FileNotFoundError:

    print(f"\nError: File '{filename}' not found.\n")

    exit()

# ==========================================
# PARSE SOURCE CODE
# ==========================================

ast = parser.parse(
    source_code,
    lexer=lexer
)

# ==========================================
# STOP IF PARSE FAILED
# ==========================================

if has_error or ast is None:

    print("\nTranslation failed due to syntax errors.\n")

    exit()

# ==========================================
# GENERATE PYTHON CODE
# ==========================================

generator = CodeGenerator()

python_code = generator.generate(ast)

# ==========================================
# OUTPUT FILE
# ==========================================

output_file = filename.replace(".yl", ".py")

# ==========================================
# SAVE GENERATED CODE
# ==========================================

with open(output_file, "w", encoding="utf-8") as file:

    file.write(python_code)

# ==========================================
# SUCCESS MESSAGE
# ==========================================

print("\nበትክክል ተተርጉሟል!")
print(f"Generated output saved to: {output_file}\n")