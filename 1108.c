#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Question:
// Easy
// Given a valid (IPv4) IP address, return a defanged version of that IP address.
// A defanged IP address replaces every period "." with "[.]".

char *defangIPaddr(char *address)
{
    int len = strlen(address);
    // char defang[len + 7];
    char *defang = (char *)malloc(sizeof(char) * (len + 6) + 1);
    int i = 0;
    int count = 0;
    while (address[i] != '\0')
    {
        if (address[i] == '.')
        {
            *(defang + count) = '[';
            count++;
            *(defang + count) = '.';
            count++;
            *(defang + count) = ']';
            count++;
        }
        else
        {
            *(defang + count) = address[i];
            count++;
        }
        i++;
    }
    *(defang + count) = '\0';
    return defang;
}

int main()
{
    char ipv4[8];
    strcpy(ipv4, "1.1.1.1");
    printf("%s", defangIPaddr(ipv4));
}
