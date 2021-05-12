#include "mbed.h"
#include "mbed_rpc.h"
#include "stm32l475e_iot01_accelero.h"
#include <cmath>
void getAcc(Arguments *in, Reply *out);
float Measured_angle=0;

BufferedSerial pc(USBTX, USBRX);
RPCFunction rpcAcc(&getAcc, "getAcc");

int main() {
   // Enable the the accelerometer
   printf("Start accelerometer init\n");
   BSP_ACCELERO_Init();

   char buf[256], outbuf[256];

   FILE *devin = fdopen(&pc, "r");
   FILE *devout = fdopen(&pc, "w");

   while (true) {
      memset(buf, 0, 256);      // clear buffer
      for(int i=0; i<255; i++) {
         char recv = fgetc(devin);
         if (recv == '\r' || recv == '\n') {
            printf("\r\n");
            break;
         }
         buf[i] = fputc(recv, devout);
      }
      RPC::call(buf, outbuf);
      printf("%s\r\n", outbuf);
   }
}

void getAcc(Arguments *in, Reply *out) {
   int16_t pDataXYZ[3] = {0};
   char buffer[200];
   //while(Measured_angle<700){
      
      BSP_ACCELERO_AccGetXYZ(pDataXYZ);
      int h= pDataXYZ[2];
      if(h>1000) h=1000;
      printf("h: %d\n",h);
      Measured_angle = (acos(h/1000.0)) * (180/3.142);
      float test = acos(600.0/1000);
      float test_radian = test*(180/3.142);
      //printf("test: %1.1f\n",test);
      //printf("test_radian: %1.1f\n",test_radian);
      sprintf(buffer, "\n\rAccelerometer values: (%d, %d, %d,%1.1f)\n\r", pDataXYZ[0], pDataXYZ[1], h,Measured_angle);
      out->putData(buffer);
      ThisThread :: sleep_for(700ms);
   //}
   
}