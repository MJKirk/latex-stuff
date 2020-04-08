#!/usr/bin/env python3

# Checks a bibtex file and prints out entries that don't have DOIs and are on the arXiv.
# Useful for checking if any preprints that you cite have been published since you
# added them to the bibtex.

import sys
from pybtex.database import parse_file

# This should be a bibtex file
filename = sys.argv[1]
bibs = parse_file(filename)

for e in bibs.entries:
    if ( bibs.entries[e].type == "article" and 
         "doi" not in bibs.entries[e].fields and 
         "eprint" in bibs.entries[e].fields ):
        print (e, bibs.entries[e].fields["eprint"])
