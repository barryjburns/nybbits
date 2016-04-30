#!/bin/bash

BEFORE="style.css"
AFTER="${BEFORE/.css/.min.css}"

rm *.min.css;

find . -maxdepth 1 -type f -name '*.css' | while read before; do
  after="${before/.css/.min.css}";
  echo "Minifying: ${before} -> ${after}...";
  cleancss -o "${after}" -s "${before}";
  wc -c "${before}" "${after}" | cut -f 1 -d ' ' | head -n 2 | {
    read bs;
    read as;
    echo "$[bs-as] bytes saved.";
  };
done;

