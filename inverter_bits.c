
#include <stdint.h>
#include <stdio.h>

// Faz a inversão de forma recursiva, dividindo ao meio (em relação ao número de bits).

uint32_t inverte(uint32_t n, uint32_t start, uint32_t end)
{

    if (start == end)
    {
        return (n >> (31 - start)) % 2;
    }

    uint32_t mid = (end - start) / 2 + start;

    uint32_t left = inverte(n, start, mid);
    uint32_t right = inverte(n, mid + 1, end);

    return (right << (end - mid)) + left;
}

// Inverte os bits de um número inteiro (sem sinal) de 32 bits, por exemplo:
// Entrada: 43261596  (00000010100101000001111010011100)
// Saída:   964176192 (00111001011110000010100101000000)

uint32_t reverseBits(uint32_t n)
{
    return inverte(n, 0, 31);
}

void main()
{
    uint32_t numero;

    scanf("%ld", &numero);
    printf("%ld", reverseBits(numero));
}