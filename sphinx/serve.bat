@ECHO OFF

echo.
echo.+++ Making HTML files...
echo.
CALL make.bat html

echo.
echo.+++ Making HTML files...
echo.
CALL make.bat markdown

echo.
echo.+++ Copying the output into the docs directory...
echo.
CALL copy.bat