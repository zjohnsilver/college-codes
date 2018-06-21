//
// Implementando a funcao strcat da biblioteca string.h
// Implemetando a funcao strlen da biblioteca string.h
//
// Created by Jon on 16.03.2016
//
#include <stdio.h>
#include <string.h>

int main(){
    char string1[20], string2[10];
    int i=0, cont=0;

    printf ("Palavra: ");
    scanf ("%s", string1);
    printf ("Palavra: ");
    scanf ("%s", string2);

    // Implemento da funcao strlen.
    while (string1[i]!='\0'){
        i++;
        cont++;
    }

    string1[cont] = ' ';

    i=0;
    // Implemento da funcao strcat usando strlen..
    while (string1[i]!= '\0'){
        string1[cont+1] = string2[i];
        cont++;
        i++;

    }

    printf ("%s\n", string1);




    return 0;
}
