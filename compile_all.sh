#!/bin/bash

# Change to the directory containing the script
cd "$(dirname "$(readlink -f "$0")")"

# Set default options
DEBUG=""
VERSION=$(python3 --version | awk '{printf ("%.2f",substr($2,0,3))}')

# Process command line options
while [[ $# -gt 0 ]]; do
    case "$1" in
        --debug)
            echo "DEBUG ON"
            set -x
            DEBUG="yes"
            trap '' SIGHUP SIGINT SIGQUIT SIGTERM
            shift
            ;;
        *)
            echo "Invalid option: $1" >&2
            exit 1
            ;;
    esac
done

# List Python scripts
find . -type f -name "*.py" -exec realpath {} \; | sort > py_scripts.lis

# Process each script
while read -r FNAME ; do
    FNAME1="$(echo "${FNAME}" | cut -d"." -f1)"
    echo "Working on Python script: ${FNAME}"
    black -l78 "${FNAME}" || exit 1
    cython3 --embed -3 -o "${FNAME1}".c "${FNAME1}".py || exit 1
    gcc -O2 -I /usr/include/python"${VERSION}" -o "${FNAME1}" "${FNAME1}".c -lpython"${VERSION}" -lm -fPIC -fwrapv -fno-strict-aliasing || exit 1
done < py_scripts.lis

# Clean up
rm -f *.c
