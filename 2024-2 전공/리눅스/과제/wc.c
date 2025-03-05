//001 컴퓨터과학전공 2312282 임다희

#include <stdio.h>
#include <ctype.h>

int main(int argc, char *argv[]){
	FILE *fp;
	int c;
	int line_count=0;
	int word_count=0;
	int char_count=0;
	int word_end=0;
	
	if(argc<2){ // $ wc

		fp=stdin;
		while((c=fgetc(fp))!=EOF){
			char_count++;
			
			if(c=='\n'){
				line_count++;}
				
			if(isspace(c)){
				if(word_end){
					word_count++;
					word_end=0;}
				}
			else{word_end=1;}
		}
		if(word_end){word_count++;}
	}
	
	else{ // $ wc file1 
		fp=fopen(argv[1],"r");
		
		if(fp==NULL){
			printf("File Error: %s\n",argv[1]);
			return 1;}
			
		while((c=fgetc(fp))!=EOF){
			char_count++;
			
			if(c=='\n'){
				line_count++;}
				
			if(isspace(c)){
				if(word_end){
					word_count++;
					word_end=0;}
				}
			else{word_end=1;}
		}
		if(word_end){word_count++;}
	}
	
	printf("\t%d\t",line_count);
	printf("%d\t",word_count);
	printf("%d\t",char_count);
	if(argv[1]){printf("%s",argv[1]);}
	fputc('\n',stdout);
	return 0;

}

