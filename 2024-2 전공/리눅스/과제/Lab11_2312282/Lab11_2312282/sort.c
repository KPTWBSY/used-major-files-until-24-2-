//001 컴퓨터과학전공 2312282 임다희
#include <stdio.h>
#include <string.h>
#include "copy.h"
char line[MAXLINE];
char lines[MAXLINE][MAXLINE];

int main()
{
	int line_count=0;
	
	printf("Modified File(Make)\n");
	printf("Enter text:");
	while (fgets(lines[line_count],MAXLINE,stdin)!=NULL){
		line_count++;
	}
	
	for(int i=0; i<line_count-1; i++){
		for(int j=1; j<line_count-i; j++){
			if(strlen(lines[j-1])>strlen(lines[j])){
				copy(lines[j],line);
				copy(lines[j-1],lines[j]);
				copy(line,lines[j-1]);
				}
			}
		}
		
	printf("-----Sorted Result-----");	
	for(int i=0; i<line_count; i++){
		for(int j=0; j<strlen(lines[i]); j++){
			printf("%c", lines[i][j]);
			}
		}
				
	return 0;
}
