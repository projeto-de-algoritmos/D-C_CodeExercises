#include <stdio.h>
#include <stdlib.h>
 
typedef struct retorno{
    int *nums;
    int  amount;
    long long inversions;
}  retorno;
 
retorno mergeAndCount(int vetorInicial[], int *numsA, int nA, int *numsB, int nB){
 
    int inversionsMergeAndCount = 0;
    int auxiliar[nA + nB];
    int marcadorA = nA;
    int marcadorB = 0;
    
    //Preencho o vetor de referencia
    int referencia[nA+nB];

    for(int i = 0; i <  nA+nB; i++){
        referencia[ vetorInicial[i] - 1 ] = i; 
    }

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
    
        if( referencia[ numsA[nA - marcadorA] - 1 ] >  referencia[ numsB[marcadorB] - 1 ] ){
 
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
 
retorno sortAndCount(int vetorInicial[], int nums[], int n, int inv){
    
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
    
    retorno retornoA = sortAndCount( vetorInicial, retornoSortAndCount.nums, lengthA, 0);
    retorno retornoB = sortAndCount( vetorInicial, &retornoSortAndCount.nums[lengthA], lengthB, 0);
    retorno retornoMergeAndCount = mergeAndCount(vetorInicial, retornoSortAndCount.nums,lengthA, &retornoSortAndCount.nums[lengthA],lengthB);  
 
    retornoSortAndCount.inversions = retornoA.inversions + retornoB.inversions+ retornoMergeAndCount.inversions;
    retornoSortAndCount.nums = retornoMergeAndCount.nums;

    return retornoSortAndCount;
}
 
int main(void){
 
    int T;
    scanf("%d", &T);
 
    int n;
    for(int i = 0; i < T; i++){
        
        scanf("%d", &n);
        int permutationA[n];
        int permutationB[n]; 
 
        for(int j = 0; j < n; j++){
            scanf("%d", &permutationA[j]);
        }
 
        for(int j = 0; j < n; j++){
            scanf("%d", &permutationB[j]);
        }
 
        int intersections = sortAndCount(permutationA, permutationB, n, 0).inversions;

        printf("%d\n", intersections);
 
    }
    
    return 0;
}