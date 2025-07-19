#!/usr/bin/env fish
# rename_episodes.fish
# Usage:  rename_episodes.fish [folder]

set dir (pwd)          # default to current dir
if test (count $argv) -ge 1
    set dir $argv[1]
end

# Loop through every .mp4 in the chosen directory
for f in $dir/*.mp4
    # Skip if it isn’t a regular file
    if not test -f $f
        continue
    end

    set filename (basename -- "$f")

    # Pull the first number inside […] using a regex capture group
    set num_match (string match -r '.*\[(\d+)\].*\.mp4' -- "$filename")

    # If the pattern matched, num_match will be the whole filename;
    # strip everything except the captured digits
    if test -n "$num_match"
        set num (string replace -r '.*\[(\d+)\].*\.mp4' '$1' -- "$filename")
        set newname (printf "e%03d.mp4" $num)   # zero-pad to 3 digits
        set newpath "$dir/$newname"

        # Show what will happen first (safety); remove “echo” when happy
        echo mv -- "$f" "$newpath"
        mv -- "$f" "$newpath"
    end
end
