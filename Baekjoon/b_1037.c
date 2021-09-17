#include <stdio.h>

int main(){
    int N,A[50],num,max,min;
    scanf("%d",&num);
    for(int i=0;i<num;i++){
        scanf("%d",&A[i]);
    }
    max=A[0];
    min=A[0];
    for(int i=1;i<num;i++){
        if(max<A[i]) max=A[i];
        if(min>A[i]) min=A[i];
    }
    printf("%d",max*min);
    return 0;
}
