#!/bin/bash
echo "Creating plugin folder "
mkdir -p "$(tutor plugins printroot)"
echo "Copying files"
cp -r ./* "$(tutor plugins printroot)"
echo "Done"
echo "Now run tutor plugins list and tutor plugins enable <plugin_name>"