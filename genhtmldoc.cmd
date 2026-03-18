echo Y | rmdir docs /S
sphinx-build -E rstdocs htmldocs 
copy /y CNAME .\docs\
copy /y .nojekyll .\docs\
xcopy /y .\rstdocs\README.txt .\docs\
make pdf