/*
SOURCES:
	https://jasongarr.wordpress.com/project-pages/ipod-clickwheel-hack/ by Jason Garr
	https://hackaday.com/2010/02/05/repurposing-a-click-wheel/ by Mike Szczys
*/

#include “clickwheel.h”
#include “avr/interrupt.h”

volatile unsigned char cmd;
volatile char posn1, db_compare;
volatile union 
{
	unsigned char byte[4];
	unsigned long int word;
} cmd_packet;

ISR(INT1_vect) 
{
	if (CW_SDA) 
	{
		cmd_packet.byte[0] |= 0x80;
	}

	if (((cmd_packet.byte[0] == 128) || (cmd_packet.byte[0] == 192)) && (cmd_packet.byte[3] == 26))
	{
		cmd = 0x20;
		EIMSK &= ~(0x02);
	}
	else
	{
		cmd_packet.byte[3] = (cmd_packet.byte[3]>>1);
		cmd_packet.byte[3] |= (cmd_packet.byte[2]<<7);

		cmd_packet.byte[2] = (cmd_packet.byte[2]>>1);
		cmd_packet.byte[2] |= (cmd_packet.byte[1]<<7);

		cmd_packet.byte[1] = (cmd_packet.byte[1]>>1);
		cmd_packet.byte[1] |= (cmd_packet.byte[0]<<7);

		cmd_packet.byte[0] = (cmd_packet.byte[0]>>1);
	}
}

unsigned char uiaction(void) {
	if (cmd == CW_CMD_FLAG ) {

		if(cmd_packet.byte[CW_BTN_CMD] != 0)
		{
			cmd = cmd_packet.byte[2];
			return;
		}
		else
		{
			if (cmd_packet.byte[CW_WHEEL_CMD] > posn1)
			{
				while (db_compare > CW_DEADBAND)
				{
					cmd = CW_CMD_CW;
					db_compare = CW_DEADBAND / 2;
					break;
				}
				db_compare += 1;
			}
			
			if (cmd_packet.byte[CW_WHEEL_CMD] < posn1)
			{
				while (db_compare <= 0)
				{
					cmd = CW_CMD_CCW;
					db_compare = CW_DEADBAND / 2;
					break;
				}
				db_compare -= 1;
			}
			posn1 = cmd_packet.byte[CW_WHEEL_CMD];

		}
		cmd &= ~CW_CMD_FLAG;
		cmd_packet.word = 0x00000000;
	}
	EIMSK |= 0x02;
	return cmd;
}

void uiinit()
{
	//initialize clickwheel port as
	DATA_PORT |= (1<<CW_SDA_PIN) | (1<<CW_SCL_PIN);

	//configure INT1_vect and pins for sampling clickwheel data transmissions
	//on rising edges of the clock
	EICRA = 0x0C;    //sets for rising edge interrupt on INT1
	EIMSK = 0x02;    //enable interrupts on port INT1
	sei();
}

void uireset()
{
	cmd_packet.word = 0x00000000;
	cmd = 0;
}