#!/bin/bash

DOC="nota.txt"


echo Vas a apagar el ordenador. 
echo ¿Quieres recordar algo cuando vuelvas a encender el ordenador?

read texto

echo "$texto" > $DOC
