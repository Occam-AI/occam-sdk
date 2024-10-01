#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <file_path>"
    exit 1
fi

file_path="$1"

if ! [ -f "$file_path" ]; then
    echo "File not found: $file_path"
    exit 1
fi

# Read the file content
content=$(<"$file_path")

# Replace all occurrences of "operation_id_[any word]_" with an empty string
# The -E flag enables extended regular expressions, which is necessary for the + quantifier
content=$(echo "$content" | sed -E 's/operation_id_[a-zA-Z0-9]+_//g')

# Write the modified content back to the file
echo "$content" > "$file_path"

# Also add the occam_client at the end of the base __init__.py file
if [[ "$file_path" == *"occam_sdk/__init__.py" ]]; then
    echo "$occam_client_definition" >> "$file_path"
fi

if [ $? -eq 0 ]; then
    echo "Successfully processed $file_path"
    exit 0
else
    echo "Error processing file"
    exit 1
fi