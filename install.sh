#!/bin/bash
echo "Creating plugin folder "
mkdir -p "$(tutor plugins printroot)"
echo "Copying files"
cp -r ./* "$(tutor plugins printroot)"
echo "Done"
echo "Now run tutor plugins list and tutor plugins enable <plugin_name>"
echo "To enable all mfe plugins: tutor plugins enable mfe-account mfe-authn mfe-discussions mfe-learner-dashboard mfe-learning mfe-profile"

echo "available plugins:"
for f in $(ls *.py); do
    echo "tutor plugins install $(basename $f .py)"
done





