#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
    char var1 = 0x6b;
    char var2 = 0x72;
    char var3 = 0x64;
    char var4 = 0x75;
    char var5 = 0x7b;
    char var6 = 0x79;
    char var7 = 0x30;
    char var8 = 0x75;
    char var9 = 0x5f;
    char var10 = 0x62;
    char var11 = 0x33;
    char var12 = 0x34;
    char var13 = 0x74;
    char var14 = 0x5f;
    char var15 = 0x6d;
    char var16 = 0x79;
    char var17 = 0x5f;
    char var18 = 0x63;
    char var19 = 0x30;
    char var20 = 0x6d;
    char var21 = 0x70;
    char var22 = 0x75;
    char var23 = 0x74;
    char var24 = 0x33;
    char var25 = 0x72;
    char var26 = 0x7d;

    srand(time(NULL));

    int secretNumber = rand() % 999999 + 1;

    int guess;
    int attempts = 0;

    printf("Welcome to the 'Guess the Number' game!\n");
    printf("I have chosen a number between 1 and 999999. Try to guess it.\n");

    do
    {
        printf("Enter your guess: ");
        scanf("%d", &guess);

        attempts++;

        if (guess > secretNumber)
        {
            printf("Too high! Try again.\n");
        }
        else if (guess < secretNumber)
        {
            printf("Too low! Try again.\n");
        }
        else
        {
            printf("Congratulations! You guessed the number in %d attempts.\n", attempts);
        }
    } while (guess != secretNumber);

    system("pause");
    return 0;
}
