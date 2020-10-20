#include “stdlib.h”
#include “avr/io.h”
#include “lcd.h”
#include “clickwheel.h”

#define F_CPU 8000000UL  // 8 MHz

void main(void) {

	char buffer[32];
	int count;

	uiinit();
	lcd_init(LCD_DISP_ON);

	for(;;) 
	{

		//check to see if a new command has been recieved and process command
		//and print appropriate button response

		switch(uiaction()) {
			case CW_CMD_CW:
				lcd_gotoxy(0,0);
				lcd_puts(“clockwise       “);
				count = count + 10;
				utoa(count, buffer, 10);
				lcd_gotoxy(6,1);
				lcd_puts(buffer);
				lcd_puts(”     “);
				uireset();
				break;
				
			case CW_CMD_CCW:
				lcd_gotoxy(0,0);
				lcd_puts(“counterclockwise”);
				count = count – 10;
				utoa(count, buffer, 10);
				lcd_gotoxy(6,1);
				lcd_puts(buffer);
				lcd_puts(”     “);
				uireset();
				break;
				
			case CW_CMD_PP:
				lcd_gotoxy(0,0);
				lcd_puts(“play/pause      “);

				uireset();
				break;
			case CW_CMD_MENU:
				lcd_gotoxy(0,0);
				lcd_puts(“menu            “);
				uireset();
				break;
				
			case CW_CMD_BACK:
				lcd_gotoxy(0,0);
				lcd_puts(“back            “);
				count –;
				utoa(count, buffer, 10);
				lcd_gotoxy(6,1);
				lcd_puts(buffer);
				lcd_puts(”     “);
				uireset();
				break;
				
			case CW_CMD_FORWARD:
				lcd_gotoxy(0,0);
				lcd_puts(“forward         “);
				count ++;
				utoa(count, buffer, 10);
				lcd_gotoxy(6,1);
				lcd_puts(buffer);
				lcd_puts(”     “);
				uireset();
				break;
				
			case CW_CMD_CBTN:
				lcd_gotoxy(0,0);
				lcd_puts(“center button   “);
				uireset();
				count = 0;
				break;
				
			default:
				1;
		}

	}
}

// LINK: https://jasongarr.wordpress.com/project-pages/ipod-clickwheel-hack/
// Article: https://hackaday.com/2010/02/05/repurposing-a-click-wheel/