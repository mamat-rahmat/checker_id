# Checker ID

A simple script to check "suspicious" word in Indonesian po translation file. Suspicious means it is recognized by KBBI (Kamus Besar Bahasa Indonesia).

## Details

Checker ID will parse the po file, stem the strmsg, check every word with [Kateglo API](http://kateglo.com/api.php), and output list of word that is not recognized by KBBI. Please note that these word needs further investigation.

## Requirements
* Python 2.x
* polib
* Pysastrawi
* Requests

## Usage
To run a script against a po file
`python checker_id.py /path/to/file`
To run a script against all po files in a directory
`python checker_id.py /directory/to/transverse`

## Lisence

[LISENCE](LISENCE)