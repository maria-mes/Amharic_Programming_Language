Keywords and Meanings

The Amharic Programming Language (APL) is a beginner‑friendly language designed to make programming more intuitive for Ethiopian learners. By replacing English keywords with Amharic equivalents, APL lowers the entry barrier for those new to coding and provides a culturally relevant learning experience.

Amharic Keyword	Meaning in English	Purpose
ቁጥር	variable (number)	Declare variables
ከሆነ	if	Conditional statement
ያለበለዚያ	else	Alternative condition
እስከ	while	Loop structure
ተግባር	function	Function definition
ተመለስ	return	Return value from function
አትም	print	Output statement

These keywords are designed to reduce the learning barrier for beginners who are not familiar with English programming syntax.


✨ Core Features
🔑 Keywords

| Amharic Keyword | English Meaning | Purpose |
| --- | --- | --- |
| ቁጥር | variable (number) | Declare variables |
| ከሆነ | if | Conditional statement |
| ያለበለዚያ | else | Alternative condition |
| እስከ | while | Loop structure |
| ተግባር | function | Function definition |
| ተመለስ | return | Return value |
| አትም | print | Output statement |

2. Syntax Rules

The language follows a simple and structured syntax designed for readability.

2.1 Variables

Variables are declared using the keyword ቁጥር.

ቁጥር x = 10
2.2 Arithmetic Expressions

Supports basic mathematical operations:

Addition +
Subtraction -
Multiplication *
Division /
ቁጥር y = x + 5 * 2
2.3 Conditional Statements

If-else statements use braces {} for block structure.

ከሆነ x > 5 {
    አትም("Greater")
}
ያለበለዚያ {
    አትም("Smaller")
}
2.4 Loops

The language supports a while loop using the keyword እስከ.

እስከ x <= 5 {
    x = x + 1
}
2.5 Functions

Functions are defined using ተግባር and return values using ተመለስ.

ተግባር ደምር(a, b) {
    ተመለስ a + b
}

ቁጥር ውጤት = ደምር(7, 8)
አትም(ውጤት)

15

2.6 Function Calls
ቁጥር ውጤት = ደምር(5, 3)
3. Example Programs
3.1 Basic Program (Variables + Math)
ቁጥር x = 10
ቁጥር y = 5

ቁጥር ውጤት = x + y * 2

አትም(ውጤት)
3.2 Control Flow (If + Loop)
ቁጥር x = 1

እስከ x <= 5 {

    ከሆነ x == 3 {
        አትም("ሶስት")
    }
    ያለበለዚያ {
        አትም(x)
    }

    x = x + 1
}
3.3 Functions Example
ተግባር ደምር(a, b) {
    ተመለስ a + b
}

ቁጥር ውጤት = ደምር(7, 8)

አትም(ውጤት)

3.4 Control FLow
ቁጥር x = 1

እስከ x <= 5 {
    ከሆነ x == 3 {
        አትም("ሶስት")
    }
    ያለበለዚያ {
        አትም(x)
    }
    x = x + 1
}


Compiler Pipeline

APL follows a three‑stage compiler design:

Lexer → Converts Amharic source into tokens.

Parser → Validates syntax and builds an Abstract Syntax Tree (AST).

Code Generator → Produces equivalent Python code for execution.

This ensures that APL remains simple for beginners while still being backed by a robust compiler architecture.

4. Beginner-Friendly Design Explanation

This language is designed specifically for beginners with the following improvements:

Local Language Keywords → Learners think in Amharic, not English.

Simplified Syntax → Uses braces {} instead of indentation.

Essential Features Only → Variables, conditions, loops, functions.

Clear Program Flow → Declare → Logic → Output.

Error Messages in Amharic → Mistakes explained in native language.
4.1 Use of Local Language

Instead of English keywords like if, while, and print, this language uses Amharic words such as ከሆነ, እስከ, and አትም, making it easier for native speakers to understand programming logic.

4.2 Simple Syntax

The language avoids complex syntax rules such as indentation-based blocks. Instead, it uses braces {}, which are easier to understand and parse.

4.3 Reduced Complexity

Only essential programming features are included:

Variables
Conditions
Loops
Functions

This keeps the language small and beginner-focused.

4.4 Clear Structure

Each program follows a predictable structure:

Declare variables
Write logic
Output results

This helps learners understand program flow easily.

4.5 Error Handling in Local Language

Error messages are displayed in Amharic, helping users understand mistakes without needing English knowledge.


🚀 Getting Started
Install Python 3.10+.

Translate Amharic source:

bash
python3 translator.py examples/basic.አም
Run generated Python:

bash
python3 examples/basic.py
Summary

This language demonstrates how programming concepts can be simplified using local language design while still maintaining a fully functional compiler pipeline that translates into Python code.