#include <iostream>




#include "ws2812-rpi.h"
using namespace std;


#define U_CHAR unsigned char


//MATRIX DEFINES
#define LED_MATRIX_ROW 16 //ROWS
#define LED_MATRIX_COL 16 //COLS
#define LED_MATRIX_TOTAL (LED_MATRIX_ROW * LED_MATRIX_COL)

struct LED_INFO
{
	U_CHAR r;
	U_CHAR g;
	U_CHAR b;
};


struct LED_MATRIX
{
	LED_INFO leds[LED_MATRIX_TOTAL];
	
	
};


int main(int argc, char *argv[])
{
	
	
	NeoPixel *n = new NeoPixel(16);

	while(true)
	{
		n->clear();
		n->setPixelColor(0, 255, 255, 0);
		n->show();
	}
		
	n->show();
	delete n;
	
	
	return 0;
}