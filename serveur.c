#include <stdio.h>
#include <netdb.h>
#include <netinet/in.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <sys/types.h>
#define MAX 80
#define PORT 8080
#define SA struct sockaddr


int app(int sockfd, const struct sockaddr_in cliaddr)
{
	char buffr[MAX];
        char *buffs[MAX];	
	while(1){
		bzero(buffr, MAX);
		
        	// read the message from client and copy it in buffer
		printf("Wait msg from client...");

		int len, n; 
		len = sizeof(cliaddr);  //len is value/resuslt 
		n = recvfrom(sockfd, (char *)buffr, MAX,  
	        	        MSG_WAITALL, ( struct sockaddr *) &cliaddr, 
       			        	&len); 

		int num = atoi(buffr);
		switch(num){
			case 1:
				printf("Take picture");
				break;

			case 2:
				printf ("Receive picture");
				break;
			default :
			
				printf("Unknown Command");
				break;
		}
		
		// send message to client
		
		sendto(sockfd, (const char *)buffs, strlen(buffs),
			MSG_CONFIRM, (const struct sockaddr *) &cliaddr,
			len);
	}
}

int main(int argc, char *argv[]) 
{ 
	int sockfd, connfd; 
	struct sockaddr_in servaddr, cliaddr; 
	char buffer[MAX];
	// socket create and verification 
	sockfd = socket(AF_INET, SOCK_DGRAM, 0); 
	if (sockfd == -1) { 
		printf("socket creation failed...\n"); 
		exit(0); 
	} 
	else
		printf("Socket successfully created..\n"); 
	bzero(&servaddr, sizeof(servaddr)); 

	// assign IP, PORT 
	servaddr.sin_family = AF_INET; 
	servaddr.sin_addr.s_addr = htonl(INADDR_ANY); 
	servaddr.sin_port = htons(PORT); 

	// Binding newly created socket to given IP and verification 
	if ((bind(sockfd, (SA*)&servaddr, sizeof(servaddr))) != 0) { 
		printf("socket bind failed...\n"); 
		exit(0); 
	} 
	else
		printf("Socket successfully binded..\n"); 


	int len, n;

	len = sizeof(cliaddr);  //len is value/resuslt

	n = recvfrom(sockfd, (char *)buffer, MAX,
			MSG_WAITALL, ( struct sockaddr *) &cliaddr,
			&len);

	buffer[n] = '\0';
	printf("Client : %s\n", buffer);
	
	char *hello = "Hello from server";
	sendto(sockfd, (const char *)hello, strlen(hello),
			MSG_CONFIRM, (const struct sockaddr *) &cliaddr,
			len);
	printf("Hello message sent.\n");


	// Function 
	app(sockfd, cliaddr);

	return 0;
} 

