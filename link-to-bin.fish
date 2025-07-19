#!/usr/bin/env fish

# Ensure ~/bin exists
mkdir -p ~/bin

# Loop over matching files
for file in *.sh *.bash *.fish *.py
    # Skip if no match
    if not test -e $file
        continue
    end

    # Remove extension
    set filename (basename $file | sed -E 's/\.(sh|bash|fish|py)$//')

    # Create symlink
    ln -sf (pwd)/$file ~/bin/$filename
end
