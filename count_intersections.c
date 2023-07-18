#include <stdio.h>
#include <stdlib.h>

//Struct para representar o retorno das funções
typedef struct retorno{
    long long *nums;
    long long  amount;
    long long inversions;
}  retorno;
 
retorno mergeAndCount(long long referencia[], long long *numsA, long long nA, long long *numsB, long long nB){
 
    long long inversionsMergeAndCount = 0;
    long long auxiliar[nA + nB];
    long long marcadorA = nA;
    long long marcadorB = 0;

    long long i = 0;
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
    
    for(long long i = 0; i < nA; i++){
        numsA[i] = auxiliar[i];
    }
    for(long long i = 0; i < nB; i++){
        numsB[i] = auxiliar[i+nA];
    }
 
    retorno retornoMergeAndCount;
    retornoMergeAndCount.nums = auxiliar;  
    retornoMergeAndCount.amount = (nA+nB);
    retornoMergeAndCount.inversions = inversionsMergeAndCount;
 
    return retornoMergeAndCount;
}
 
retorno sortAndCount(long long referencia[], long long nums[], long long n, long long inv){
    
    retorno retornoSortAndCount;
    
    retornoSortAndCount.nums = nums;
    retornoSortAndCount.amount = n;
    retornoSortAndCount.inversions = inv;
 
    if(retornoSortAndCount.amount == 1){
        return retornoSortAndCount;
    }
 
    //Divido o vetor ao meio dessa forma, para caso seja ímpar
    long long lengthA, lengthB;
    lengthA = n/2;
    lengthB = n - n/2;
    
    retorno retornoA = sortAndCount( referencia, retornoSortAndCount.nums, lengthA, 0);
    retorno retornoB = sortAndCount( referencia, &retornoSortAndCount.nums[lengthA], lengthB, 0);
    retorno retornoMergeAndCount = mergeAndCount(referencia, retornoSortAndCount.nums,lengthA, &retornoSortAndCount.nums[lengthA],lengthB);
 
    retornoSortAndCount.inversions = retornoA.inversions + retornoB.inversions+ retornoMergeAndCount.inversions;
    retornoSortAndCount.nums = retornoMergeAndCount.nums;

    return retornoSortAndCount;
}
 
int main(void){
 
    long long T;
    scanf("%lld", &T);
 
    long long n;
    for(long long i = 0; i < T; i++){
        
        scanf("%lld", &n);
        long long permutationA[n];
        long long permutationB[n]; 
 
        for(long long j = 0; j < n; j++){
            scanf("%lld", &permutationA[j]);
        }
 
        for(long long j = 0; j < n; j++){
            scanf("%lld", &permutationB[j]);
        }

        //Preencho o vetor de referencia
        long long referencia[n];
        for(long long j = 0; j < n; j++){
            referencia[ permutationA[j] - 1 ] = j;  
        }

        long long intersections = sortAndCount(referencia, permutationB, n, 0).inversions;

        printf("%lld\n", intersections);
 
    }
    
    return 0;
}