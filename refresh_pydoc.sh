#! /bin/sh

set -e

SOURCE_DIR=$(pwd)/docs/source
DOC_PREFIX=auto_generated

# 前回の自動生成ファイルを削除
rm -f $SOURCE_DIR/$DOC_PREFIX*

AUTO_GENERATED_DOC=$SOURCE_DIR/$DOC_PREFIX.rst
echo "Auto Generated Pydocs\n======================================\n\n.. toctree::\n   :maxdepth: 2\n   :caption: Contents:\n\n" > $AUTO_GENERATED_DOC

CWD=$(pwd)
PYTHON_FILES=$(find . -name "*.py" | grep -v "test" | grep -v "setup.py" | grep -v "setup.cfg" | grep -v "conf.py" | grep -v "docs" | grep -v "build" | grep -v "dist" | grep -v "venv")

echo "Generating documentation for the following files:"

for file in $PYTHON_FILES; do
    # Get the module name without the .py extension
    file_path=$(dirname $file | sed 's/.\//_/')
    file_name=$(basename $file | sed 's/.py//')
    echo " $file_path"
    echo " $file_name"

    doc_name=$SOURCE_DIR/$DOC_PREFIX$file_path.rst

    if [ -f $doc_name ]; then
        echo "Add to existing documentation for $file"
        echo "   $file_name" >> $doc_name
    else
        echo "Generating documentation for $file"

        # Create the directory if it doesn't exist
        touch $doc_name
        echo "$file_name\n======================================\n\n.. autosummary::\n   :toctree: generated\n   :recursive:\n\n   $file_name\n" > $doc_name
        echo "   $DOC_PREFIX$file_path" >> $AUTO_GENERATED_DOC  # Add the file to the auto generated doc
    fi

done
