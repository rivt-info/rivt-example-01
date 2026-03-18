if "%1" == "pdf" (
sphinx-build -b pdf rstdocs pdfdocs
echo.
echo.Build finished. The PDF files are in pdfdocs
)