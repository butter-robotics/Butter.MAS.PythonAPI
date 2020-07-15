@ECHO OFF

if not exist "..\docs" mkdir ..\docs
if not exist "..\wiki" mkdir ..\wiki

XCOPY ".\_build\html" "..\docs" /s
XCOPY ".\_build\markdown" "..\wiki" /s
XCOPY ".\source\*.md" "..\wiki"

Rem echo.
Rem echo.Generating markup tree...
Rem echo.
Rem py -3.7 ./tree.py -s ../wiki