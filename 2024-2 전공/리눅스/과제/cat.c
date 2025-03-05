//001 컴퓨터과학전공 2312282 임다희

#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]){
	FILE *fp;
	int c;
	int show_line_numbers=0;
	int line_number=1;
	
	if(argc>1){
		if (strcmp(argv[1],"-n")==0){show_line_numbers=1;}
		else if(argv[1][0] == '-') { // $ other options
			printf("Error: Invalid option '%s'. Please use the -n option\n",argv[1]);
			return 1;
		}
	}
	
		
	if(show_line_numbers==0){ //no option
		if(argc < 2){ // $ cat
			fp=stdin;
			int is_first_char=1;
			while((c=fgetc(fp))!=EOF){
				if(is_first_char){
					printf("  ");
					is_first_char=0;}
				if(c=='\n'){is_first_char=1;}
				fputc(c,stdout);
				}
		}
		
		else{ // $ cat file1, file2..
		for(int i=1; i<argc; i++){
			fp=fopen(argv[i],"r");
			if(fp==NULL){
				printf("File Error: %s\n",argv[i]);
				return 1;
				}
					
			c=fgetc(fp);
			while(c!=EOF){
				fputc(c,stdout);
				c=fgetc(fp);
				}
			fclose(fp);			
			}
		}		
	}
	
	else if(show_line_numbers==1){ // $ cat -n * 
		if(argc==2){ // $ cat -n
			fp=stdin;
			int is_first_char=1;
			while((c=fgetc(fp))!=EOF){
				if(is_first_char){
					printf("\t%d  ",line_number);
					line_number++;
					is_first_char=0;}
				if(c=='\n'){is_first_char=1;}
				fputc(c,stdout);
			}
		}
		
		else{ // $ cat -n file1, file2...
		for(int i=2; i<argc; i++){
			fp=fopen(argv[i],"r");
			if(fp==NULL){
				printf("File Error: %s\n",argv[i]);
				return 1;
				}
			
			printf("\t%d  ",line_number);
			c=fgetc(fp);
			while(c!=EOF){
				int next=fgetc(fp);			
				fputc(c,stdout);
				if(c=='\n' && next!=EOF){
					line_number++;
					printf("\t%d  ",line_number);
					}
				c=next;
				}
			line_number++;	
			fclose(fp);	
		}
	}}
	
return 0;
}

