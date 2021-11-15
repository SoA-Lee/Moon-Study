import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        
        Scanner sc = new Scanner(System.in);
        
        int x = sc.nextInt();
        int y = sc.nextInt();
        
        if(x>0){
            if(y>0){
                System.out.print(1);
            }
            else{
                System.out.println(4);
            }
        }else{
            if(y>0){
                System.out.print(2);
            }
            else{
                System.out.println(3);
            }            
        }
    }
}
/*
# JavaScript
const readline = require("readline");
 
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});
 
let input = [];
 
rl.on('line', function (line) {
    input.push(line);
  }).on('close', function () {
 
let x = Number(input[0]);
let y = Number(input[1]);
 
if(x >0){
        y > 0 ? console.log(1) : console.log(4)
    }
  if(x <0){
        y > 0 ? console.log(2) : console.log(3)
    }
    
    process.exit();
});

# C++
#include <stdio.h>
int main() {
  int x, y;
  scanf("%d %d", &x, &y);
  if (x > 0 && y > 0)
    printf("1");
  if (x < 0 && y > 0)
    printf("2");
  if (x < 0 && y < 0)
    printf("3");
  if (x > 0 && y < 0)
    printf("4");
}

# python
x = int(input())
y = int(input())

if x>0:
    if y>0:
        print(1)
    else:
        print(4)
else:
    if y>0:
        print(2)
    else:
        print(3)
*/
