REM Run Sphinx to make the html documentation (rst) files from the code.
pushd docs
call make clean html
call make html
popd
@echo Done
@sleep 3