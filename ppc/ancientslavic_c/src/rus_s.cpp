#include <stdio.h>

int main() {
    const char* encryptedString = "d}kzt;al>a{P|c;y>lr";

    char key = 0x0F;

    for (int i = 0; encryptedString[i] != '\0'; i++) {
        char decrypted = encryptedString[i] ^ key;
        printf("%c", decrypted);
    }
    printf("\n");

    return 0;
}
