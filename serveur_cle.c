#include <stdio.h> //printf
#include <string.h> //memset
#include <stdlib.h> //exit(0);
#include <arpa/inet.h>
#include <sys/socket.h>
#include <unistd.h>




#define INVALID_SOCKET -1
#define SOCKET_ERROR -1
#define closesocket(s) close(s)



/*
struct sockaddr_in {
   uint8_t         sin_len;        longueur totale
   sa_family_t     sin_family;     famille : AF_INET
   in_port_t       sin_port;       le numéro de port
   struct in_addr  sin_addr;       l'adresse internet
   unsigned char   sin_zero[8];    un champ de 8 zéros
};
*/






#define MAX 1024
#define PORT 5005


int main(int argc, char *argv[])
{

  int sock;
  struct sockaddr_in serveur, si_other;
  char buffer[100];

  sock = socket(AF_INET, SOCK_DGRAM, 0);
  if(sock == INVALID_SOCKET)
  {
      perror("socket()");
      exit(0);
  }

  int i, slen = sizeof(si_other), recv_len;

  serveur.sin_addr.s_addr = htonl(INADDR_ANY);
  serveur.sin_family = AF_INET;
  serveur.sin_port = htons(PORT);

  if(bind (sock, (struct sockaddr*) &serveur, sizeof(serveur)) == SOCKET_ERROR)
  {
      perror("bind()");
      printf("socket bind failed...\n");
      exit(0);
  }
  else
    printf("Socket successfully created..\n");
  bzero(&serveur, sizeof(serveur));



  /* serveur receptionne données*/

  int n;
  while(1)
  {

    if(n = recvfrom(sock, buffer, sizeof buffer - 1, 0, (struct sockaddr *) &si_other, &slen) < 0)
    {
        perror("recvfrom()");
        exit(0);
    }

    /*buffer[n] = '\0';*/
    printf("Client : %s\n", buffer);
/*
    char *hello = "Hello from server";

    if(sendto(sock, buffer, strlen(hello), 0, (struct sockaddr*) &si_other, slen) < 0)
    {
        perror("sendto()");
        exit(0);
    }
    else
      printf("Hello message sent.\n");
*/
      char send_buffer[512];

      FILE *photo = fopen("image.jpg","r");
      printf("file desc\n");
    	fseek(photo, 0, SEEK_END);
    	int picture_size = ftell(photo);
    	fseek(photo, 0, SEEK_SET);
    	printf("Picture Size %d\n", picture_size);
      char buffer_photo [picture_size];
      fread(buffer_photo,1,sizeof(buffer_photo),photo);
      int taille_buffer;
      taille_buffer = sizeof(buffer_photo);
      printf("buffer size %d\n", taille_buffer);
      printf("BUFFER %s\n", buffer_photo);

      int total; //octets envoyés
      int reste; //octet qu'il reste
      total = 0;
      reste = taille_buffer;
      int i = 0;
      int nb_buffer = 0;



      while (total<30720){
          while (i<512)
        {
          int indice;
          indice = nb_buffer * 512 + i;
          send_buffer[i] = buffer_photo[indice];
          i +=1;
        }

        nb_buffer += 1;

        sendto(sock, send_buffer, sizeof(send_buffer),0, (struct sockaddr*) &si_other, slen);
        bzero(send_buffer,sizeof(send_buffer));
        total = total + 512;
    }

    char fin_buffer[87];
    int a = 0;
    while (a<87)
    {
        int indice;
        indice = 30720 + a;
        fin_buffer[a] = buffer_photo[indice];
        a +=1;
    }
    sendto(sock, fin_buffer, sizeof(fin_buffer),0, (struct sockaddr*) &si_other, slen);


    FILE* fic;
    fic = fopen("holla.txt","wb");
    fwrite(send_buffer,1,512,fic);
    fclose(fic);









      fclose(photo);
}
    close(sock);
    return 0;
}
