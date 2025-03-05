//001 컴퓨터과학과 2312282 임다희

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <string.h>

int main(){
	int MAXARG=100;
	int pid,i;
	int j=1;
	int enable=1;
	int is_background=0;
	char str[MAXARG];
	char *args[MAXARG];
	char *command;
	char *saveptr;
	
	while(enable==1){
	
		printf("[shell] ");
		fgets(str,sizeof(str),stdin);
		str[strcspn(str,"\n")]='\0';
		
		if(strcmp("quit",str)==0){
			enable=0;
			break;}
		
		i=0;
		command=strtok_r(str," ",&saveptr);		
		while(command!=NULL&&i<MAXARG){
			args[i]=command;
			i++;
			command=strtok_r(NULL," ",&saveptr);
		}
		
		if(i>0 && strcmp(args[i-1], "&")==0){
			is_background=1;
			args[i-1]=NULL;
		}
		else{is_background=0;}
		
		if(i<MAXARG){
			args[i]=NULL;
		}
		
		pid=fork();
				
		if(pid==0){	
			execvp(args[0],args);			
		}
		else{
			if(is_background==0){
				wait(NULL);}
			else{
				printf("[%d] %d\n",j,pid);
				j++;
				}	
		}
	}
	return 0;
}
