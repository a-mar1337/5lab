@ECHO OFF

pushd %~dp0

if "%1" == "" goto help
if "%1" == "help" goto help

if "%1" == "html" (
    sphinx-build -b html . _build/html
    goto end
)

:help
echo Usage: make ^<target^>
echo Targets: html

:end
popd