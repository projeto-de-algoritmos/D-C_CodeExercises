//Exercício LeetCode: 775. Global and Local Inversions
//O exercício pode ser acessado em: https://leetcode.com/problems/global-and-local-inversions/description/

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct retorno{
    int *nums;
    int amount;
    long long inversions;
}  retorno;

retorno mergeAndCount(int *numsA, int nA, int *numsB, int nB){

    int inversionsMergeAndCount = 0;
    int auxiliar[nA + nB];
    int marcadorA = nA;
    int marcadorB = 0;

    int i = 0;
    while(i < nA + nB){

        if(marcadorA == 0){
            auxiliar[i] = numsB[marcadorB];
            marcadorB++;
            i++;
            continue;
        }

        if(marcadorB == nB){
            auxiliar[i] = numsA[nA-marcadorA];
            marcadorA--;
            i++;
            continue;
        }

        if(numsA[nA - marcadorA] > numsB[marcadorB]){

            inversionsMergeAndCount = inversionsMergeAndCount + marcadorA;

            auxiliar[i] = numsB[marcadorB];

            marcadorB++;

        }else{
            auxiliar[i] = numsA[nA - marcadorA];
            marcadorA--;
        }

        i++;
    }

    for(int i = 0; i < nA; i++){
        numsA[i] = auxiliar[i];
    }
    for(int i = 0; i < nB; i++){
        numsB[i] = auxiliar[i+nA];
    }

    retorno retornoMergeAndCount;
    retornoMergeAndCount.nums = auxiliar;  
    retornoMergeAndCount.amount = (nA+nB);
    retornoMergeAndCount.inversions = inversionsMergeAndCount;

    return retornoMergeAndCount;
}

//Sort and Count
retorno countGlobalInversions(int nums[], int n, int inv){
    
    retorno retornoSortAndCount;
    
    retornoSortAndCount.nums = nums;
    retornoSortAndCount.amount = n;
    retornoSortAndCount.inversions = inv;

    if(retornoSortAndCount.amount == 1){
        return retornoSortAndCount;
    }

    //Divido o vetor ao meio dessa forma, para caso seja ímpar
    int lengthA, lengthB;
    lengthA = n/2;
    lengthB = n - n/2;
    
    retorno retornoA = countGlobalInversions(retornoSortAndCount.nums,lengthA, 0);
    retorno retornoB = countGlobalInversions(&retornoSortAndCount.nums[lengthA],lengthB, 0);
    retorno retornoMegeAndCount = mergeAndCount(retornoSortAndCount.nums,lengthA, &retornoSortAndCount.nums[lengthA],lengthB);  

    retornoSortAndCount.inversions = retornoA.inversions + retornoB.inversions+ retornoMegeAndCount.inversions;
    retornoSortAndCount.nums = retornoMegeAndCount.nums;

    return retornoSortAndCount;
}

//Linear O(n)
int countLocalInversions(int *nums, int n){

    int inversions = 0;

    for(int i = 0; i < n-1; i++){

        if(nums[i] > nums[i+1]){
            inversions++;
        }
    }

    return inversions;

}

bool isIdealPermutation(int* nums, int numsSize){

    int localInversions = countLocalInversions(nums, numsSize);
    int globalInversions = countGlobalInversions(nums, numsSize, 0).inversions;

    if(localInversions == globalInversions){
        return true;
    }else{
        return false;
    }
}

//Exemplo de main para executar e testar o código
/*int main(void){

    int n;
    scanf("%d", &n);

    int nums[n];

    for(int i = 0; i < n; i++){
        scanf("%d", &nums[i]);
    }

    int localInversions = countLocalInversions(nums, n);
    int globalInversions = countGlobalInversions(nums, n, 0).inversions;

    printf("%d ", localInversions);
    printf("%d\n", globalInversions);

    if(localInversions == globalInversions){
        printf("true\n");
    }else{
        printf("false\n");
    }

    return 0;
}*/