#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

void encode(char *data, size_t size, int key)
{
    for (size_t i = 0; i < size; i++)
    {
        data[i] = data[i] ^ key;
    }
}

int main(int argc, char *argv[])
{
    if (argc != 3)
    {
        printf("Usage: %s <input_file> <output_file>\n", argv[0]);
        system("pause");
        return 1;
    }

    FILE *inputFile = fopen(argv[1], "rb");
    if (!inputFile)
    {
        perror("Failed to open input file");
        system("pause");
        return 1;
    }

    fseek(inputFile, 0, SEEK_END);
    size_t fileSize = ftell(inputFile);
    rewind(inputFile);

    char *buffer = (char *)malloc(fileSize);
    if (!buffer)
    {
        perror("Memory allocation error");
        fclose(inputFile);
        system("pause");
        return 1;
    }

    fread(buffer, 1, fileSize, inputFile);
    fclose(inputFile);

    encode(buffer, fileSize, 0xDE);
    encode(buffer, fileSize, 0xAD);
    encode(buffer, fileSize, 0xBA);
    encode(buffer, fileSize, 0xBE);

    FILE *outputFile = fopen(argv[2], "wb");
    if (!outputFile)
    {
        perror("Failed to open output file");
        free(buffer);
        system("pause");
        return 1;
    }

    fwrite(buffer, 1, fileSize, outputFile);
    fclose(outputFile);

    printf("Text successfully encoded and written to file %s\n", argv[2]);

    // Free allocated memory
    free(buffer);

    // Pause before exiting
    system("pause");

    return 0;
}
