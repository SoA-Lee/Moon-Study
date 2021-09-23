#include <stdio.h>
 
int main()
{
    int T;
    scanf("%d", &T);
    for(int i = 0; i < T; i++)
    {
        char question[80];
        int sum = 0, score = 1;
        scanf("%s", question);
        for(int j = 0; question[j] != 0; j++)
        {
            if(question[j] == 'O')
            {
                sum += score;
                score++;
            }
            else
                score = 1;
        }
        printf("%d\n", sum);
    }
    return 0;
}
