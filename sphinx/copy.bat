@ECHO OFF

if not exist "..\docs" mkdir ..\docs
if not exist "..\docs\_markup" mkdir ..\docs\_markup

XCOPY ".\_build\html" "..\docs" /s
XCOPY ".\_build\markdown" "..\docs\_markup" /s
XCOPY ".\source\*.md" "..\docs\_markup"

Rem echo.
Rem echo.Generating markup tree...
Rem echo.
Rem py -3.7 ./tree.py -s ../docs/_markup