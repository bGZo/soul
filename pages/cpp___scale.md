- `<stdlib.h>/<itoa>`: 任意进制的转换
  - `windows` 特有
  - ```cpp
    //via: https://www.cnblogs.com/gongpixin/p/4477361.html
    #include<iostream>
    #include<stdio.h> 
    using namespace std;
    
    char*my_itoa(int num,char*str,int radix){//原数字，存放地址，要转换的转换进制 
        const char table[]="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ" ;
        char*ptr=str ;
        bool negative=false ;
        if(num==0){
            //num=0
            *ptr++='0' ;
            *ptr='/0' ;
            // don`t forget the end of the string is '/0'!!!!!!!!!
            return str ;
        }
        if(num<0){
            //if num is negative ,the add '-'and change num to positive
            *ptr++='-' ;
            num*=-1 ;
            negative=true ;
        }
        while(num){
            *ptr++=table[num%radix];
            num/=radix ;
        }
        *ptr='\0' ;
        //if num is negative ,the add '-'and change num to positive
        // in the below, we have to converse the string
        char*start=(negative?str+1:str);
        //now start points the head of the string
        ptr--;
        //now prt points the end of the string
        while(start<ptr){
            char temp=*start ;
            *start=*ptr ;
            *ptr=temp ;
            start++;
            ptr--;
        }
        return str ;
    }
    int main(){
      int a=15;
      char str[100];
      my_itoa(a,str,8);
      printf("%s\n",str);
      return 0;
    }
    ```
-