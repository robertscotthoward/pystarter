REM Run Sphinx to make the html documentation (rst) files from the code.
pushd docs
make clean html
make html
popd
@echo Done
@sleep 3