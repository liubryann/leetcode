#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//Question
//Easy
// Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.
// Symbol       Value
// I             1
// V             5
// X             10
// L             50
// C             100
// D             500
// M             1000

int romanToInt(char *s)
{
    int result = 0;
    int i = 0;
    while (s[i] != '\0')
    {
        switch (s[i])
        {
        case 'I':
            if (s[i + 1] == 'V')
            {
                result += 4;
                i++;
            }
            else if (s[i + 1] == 'X')
            {
                result += 9;
                i++;
            }
            else
            {
                result += 1;
            }
            break;
        case 'V':
            result += 5;
            break;
        case 'X':
            if (s[i + 1] == 'L')
            {
                result += 40;
                i++;
            }
            else if (s[i + 1] == 'C')
            {
                result += 90;
                i++;
            }
            else
            {
                result += 10;
            }
            break;
        case 'L':
            result += 50;
            break;
        case 'C':
            if (s[i + 1] == 'D')
            {
                result += 400;
                i++;
            }
            else if (s[i + 1] == 'M')
            {
                result += 900;
                i++;
            }
            else
            {
                result += 100;
            }
            break;
        case 'D':
            result += 500;
            break;
        case 'M':
            result += 1000;
            break;
        }
        i++;
    }
    return result;
}