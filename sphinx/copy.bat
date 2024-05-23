@ECHO OFF

if not exist "..\docs" mkdir ..\docs
if not exist "..\wiki" mkdir ..\wiki

Rem XCOPY ".\_build\html" "..\docs" /s
XCOPY ".\_build\markdown" "..\wiki\v2" /s
XCOPY ".\source\*.md" "..\wiki\v2"

Rem echo.
Rem echo.Generating markup tree...
Rem echo.
Rem py -3.7 ./tree.py -s ../wiki/v2 -n revision.tree