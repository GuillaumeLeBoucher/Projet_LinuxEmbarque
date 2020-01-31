#include <stdio.h> 
#include <string.h> 
#include <fcntl.h> 
#include <sys/stat.h> 
#include <sys/types.h> 
#include <unistd.h> 
  
int main() 
{ 
    int fd; 
  
    // FIFO file path 
    char * myfifo = "./mypipe"; 
  
    // Creating the named file(FIFO) 
    // mkfifo(<pathname>, <permission>) 
    mkfifo(myfifo, 0666); 
  
    char* msg;


    while(1)
    {
        for (int i =0; i<=2; i++)
        {
            // Open FIFO for write only 
            fd = open(myfifo, O_WRONLY);
            
            if (i==0)
            {
                msg = "0";
            }
            if (i==1)
            {
                msg = "1";
            }            
            if (i==2)
            {
                msg = "2";
            }

            // Write the input arr2ing on FIFO 
            // and close it 
            write(fd, msg, strlen(msg)+1);

            close(fd);

            sleep(1);
        }

    }

    return 0; 
} 