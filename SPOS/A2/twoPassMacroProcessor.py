from macroPass1 import macroPass1
from macroPass2 import macroPass2

pass1 = macroPass1()
pass2 = macroPass2()
print("Pass1:")
pass1.parseFile()
pass1.writeMacroNameTable()
pass1.writeParamNameTable()
pass1.writeMacroDefTable()
pass1.writeKeywordParamDefTable()
print("\nPass2:")
pass2.readMacroDefTable()
pass2.readMacroNameTable()
pass2.readKeywordParamDefTable()
pass2.readParamNameTable()
pass2.parseFile()

