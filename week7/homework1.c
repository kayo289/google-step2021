#include<stdio.h>
#include <stdio.h>
#include <time.h>
int main()
{
	printf("CPU時間： %lu\n", clock());
	int n = 5;
	int a[5][5] = {{1,2,3,4,5},{6,7,8,9,10},{1,2,3,4,5},{1,2,3,4,5},{1,2,3,4,5}};
	int b[5][5] = {{1,2,3,4,5},{6,7,8,9,10},{1,2,3,4,5},{1,2,3,4,5},{1,2,3,4,5}};
	int c[5][5] = {{1,2,3,4,5},{6,7,8,9,10},{1,2,3,4,5},{1,2,3,4,5},{1,2,3,4,5}};
	// ijk
	for(int i = 0; i < n; i++)
			for(int j = 0; j < n; j++)
					for(int k = 0; k < n; k++)
							c[i][j] += a[i][k] * b[j][k];
	printf("CPU時間： %lu\n", clock());
	// ikj
	for(int i = 0; i < n; i++)
			for(int k = 0; k < n; k++)
					for(int j = 0; j < n; j++)
							c[i][j] += a[i][k] * b[k][j];
	printf("CPU時間： %lu\n", clock());
	// jik
	for(int j = 0; j < n; j++)
			for(int i = 0; i < n; i++)
					for(int k = 0; k < n; k++)
							c[i][j] += a[i][k] * b[j][k];
	printf("CPU時間： %lu\n", clock());

	// jki
	for(int j = 0; j < n; j++)
			for(int k = 0; k < n; k++)
					for(int i = 0; i < n; i++)
							c[i][j] += a[i][k] * b[k][j];
	printf("CPU時間： %lu\n", clock());
	// kij
	for(int k = 0; k < n; k++)
			for(int i = 0; i < n; i++)
					for(int j = 0; j < n; j++)
							c[i][j] += a[i][k] * b[k][j];
	printf("CPU時間： %lu\n", clock());

	// kji
	for(int k = 0; k < n; k++)
			for(int j = 0; j < n; j++)
					for(int i = 0; i < n; i++)
							c[i][j] += a[i][k] * b[k][j];
	printf("CPU時間： %lu\n", clock());

	return (0);
}
