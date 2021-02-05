#include<stdio.h>
#include<math.h>
int main(){

/*
	q3

	int a,b,sum;
	
	printf("Enter any 2 integers:\n");
	scanf("%d%d",&a,&b);

	sum = pow((a+b),3);

	printf("sum = %d\n", sum);

--------------------------------------------------------------	
	q4

	int n, ones, tens, hundreds, thousands;
	
	printf("Enter any 4 digit integer:\n");
	scanf("%d",&n);

	ones = n % 10;
	tens = (n / 10) % 10;
	hundreds = ((n / 10) / 10) % 10;
	thousands = (((n / 10) / 10) / 10) % 10;

	printf("ones = %d\n", ones);
	printf("tens = %d\n", tens);
	printf("hundreds = %d\n", hundreds);
	printf("thousands = %d\n", thousands);

--------------------------------------------------------------
	q5

	int n, ones, tens, hundreds, thousands, rev;
	
	printf("Enter any 4 digit integer:\n\n");
	scanf("%d",&n);

	ones = n % 10;
	tens = (n / 10) % 10;
	hundreds = ((n / 10) / 10) % 10;
	thousands = (((n / 10) / 10) / 10) % 10;

	rev = (ones * 1000) + (tens * 100) + (hundreds * 10) + thousands;  

	printf("Reversed integer = %d\n", rev);

--------------------------------------------------------------
	q6

	int n;
	int a[7];

	printf("Enter any 7 digit integer:\n");
	scanf("%d",&n);
	
	for(int i = 0; i < 7; i++){
		a[6 - i] =  (n % 10);
		n /= 10;
	}

	printf("%d%d%d\n", a[2],a[3],a[4]);	

--------------------------------------------------------------
	q7 

	int n;
	int a[5];

	printf("Enter any 5 digit integer:\n");
	scanf("%d",&n);
	
	for(int i = 0; i < 5; i++){
		a[4 - i] =  (n % 10);
		n /= 10;
	}

	printf("%d%d%d%d%d\n", a[1],a[0],a[2],a[4],a[3]);
	printf("%d%d%d%d%d\n", a[3],a[4],a[2],a[0],a[1]);
	printf("%d%d%d%d%d\n", a[4],a[3],a[2],a[1],a[0]);	

--------------------------------------------------------------
	q8

	int n, l, m, q, sum;
	int a[6];

	printf("Enter any 6 digit integer:\n");
	scanf("%d",&n);
	
	for(int i = 0; i < 6; i++){
		a[5 - i] =  (n % 10);
		n /= 10;
	}

	l = a[4] + a[5];
	m = a[2] + a[3];
	q = a[0] + a[1];
	sum = l + m + q;

	printf("%d%d\n",a[4],a[5]);
	printf("%d%d\n",a[2],a[3]);
	printf("%d%d\n",a[0],a[1]);	

	printf("sum = %d\n", sum);
*/


	int x,y,out;

	scanf("%d", &x);
	scanf("%d", &y);

	printf("x^2 + (3 * (x^3) * y) + (4 * x * y) - (4 * y) + 7 = ?\n");
	out = (pow(x,2)) + (3 * pow(x,3) * y) + (4 * x * y) - (4 * y) + 7;
	printf("%d^2 + (3 * (%d^3) * %d) + (4 * %d * %d) - (4 * %d) + 7 = %d \n",x,x,y,x,y,y,out);


	return 0;
}