@ECHO OFF

pushd %~dp0

if "%1" == "" goto help
if "%1" == "help" ( goto help )
if "%1" == "html" ( goto html )
if "%1" == "clean" ( goto clean )

:html
sphinx-build -b html . _build/html
goto end

:clean
if exist _build rmdir /s /q _build
goto end

:help
echo Usage: make ^<target^>
echo.
echo Targets:
echo   html    to make standalone HTML files
echo   clean   to remove build directory

:end
popd