@ECHO OFF

Rem echo.
Rem echo.+++ Making HTML files...
Rem echo.
Rem CALL make.bat html

echo.
echo.+++ Making markdown files...
echo.
CALL make.bat markdown

echo.
echo.+++ Copying the output into the docs / wiki directories...
echo.
CALL copy.bat