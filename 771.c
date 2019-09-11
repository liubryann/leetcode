#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Question:
// Easy
// You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.
// The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

int numJewelsInStones(char *J, char *S)
{
    int i = 0;
    int count = 0;
    while (S[i] != '\0')
    {
        int j = 0;
        while (J[j] != '\0')
        {
            if (S[i] == J[j])
            {
                count++;
                break;
            }
            j++;
        }
        i++;
    }
    return count;
}

int main()
{
    char J[50];
    char S[50];
    strcpy(J, "aA");
    strcpy(S, "aAAbbbb");
    printf("%d\n", numJewelsInStones(J, S));

    strcpy(J, "z");
    strcpy(S, "ZZ");
    printf("%d\n", numJewelsInStones(J, S));

    return 0;
}