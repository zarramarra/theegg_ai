#!/bin/bash

NUM=5
DOC="texto_de_ejemplo.txt"

echo Las $NUM palabras más comunes en el archivo $DOC son
sed -e 's/[^[:alpha:]]/ /g' $DOC | tr '\n' " " |  tr -s " " | tr " " '\n'| tr 'A-Z' 'a-z' | sort | uniq -c | sort -nr | nl | head -n $NUM

