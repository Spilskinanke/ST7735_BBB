import Adafruit_BBIO.SPI as SPI
from Adafruit_BBIO.SPI import SPI
import sys

from Adafruit_BBIO.GPIO import GPIO

define DELAY 0x80

#define TFT_CS_LOW              0           // CS normally controlled by hardware
#define TFT_CS_HIGH             0x08

int DC
#define DC_COMMAND              0
#define DC_DATA                 0x40

#define RESET_LOW               0
#define RESET_HIGH              0x80


def writecomm(command):
    DC = DC_COMMAND
    spi.writebytes(command)
    
    
def writedata(data):
    DC = DC_DATA
    spi.writebytes(data)
    

def st_init():
    bool isdelay
    for i in inittable:
        writecomm(i[0])
        if (i[1] == DELAY):
          isdelay = True
        else
          isdelay = False
        for j in i[2:]:
          if (isdelay):
            isdelay = False #delay by ms here
          else:
            writedata(j)
          

            
      
      

spi = SPI(0,1)

spi.open(0,1)



print(spi.writebytes([0xFFF0, 0xFFFF]))
returnal = spi.readbytes(32)
print(returnal)
spi.close()

inittable = [                 
    [ST7735_SWRESET,   DELAY, 
      150],                   
    [ST7735_SLPOUT ,   DELAY,  
      255],                   
    [ST7735_FRMCTR1, 3      ,  
      0x01, 0x2C, 0x2D],      
    [ST7735_FRMCTR2, 3      ,  
      0x01, 0x2C, 0x2D],       
    [ST7735_FRMCTR3, 6      , 
      0x01, 0x2C, 0x2D,      
      0x01, 0x2C, 0x2D],       
    [ST7735_INVCTR , 1      ,  
      0x07],                  
    [ST7735_PWCTR1 , 3      , 
      0xA2,					
      0x02,                  
      0x84],                  
    [ST7735_PWCTR2 , 1      ,  
      0xC5],                   
    [ST7735_PWCTR3 , 2      ,  
      0x0A,                   
      0x00],                  
    [ST7735_PWCTR4 , 2      , 
      0x8A,                   
      0x2A],
    [ST7735_PWCTR5 , 2      ,  
      0x8A, 0xEE],
    [ST7735_VMCTR1 , 1      , 
      0x0E],
    [ST7735_INVOFF , 0]      ,  
    [ST7735_MADCTL , 1      , 
      0xC8],                   
    [ST7735_COLMOD , 1      , 
      0x05],
    [ST7735_CASET  , 4      ,  
      0x00, 0x00,             
      0x00, 0x7F],             
    [ST7735_RASET  , 4      ,  
      0x00, 0x00,             
      0x00, 0x9F],
     [ST7735_GMCTRP1, 16      ,
      0x02, 0x1c, 0x07, 0x12,
      0x37, 0x32, 0x29, 0x2d,
      0x29, 0x25, 0x2B, 0x39,
      0x00, 0x01, 0x03, 0x10],
    [ST7735_GMCTRN1, 16      ,
      0x03, 0x1d, 0x07, 0x06,
      0x2E, 0x2C, 0x29, 0x2D,
      0x2E, 0x2E, 0x37, 0x3F,
      0x00, 0x00, 0x02, 0x10],
    [ST7735_NORON  ,    DELAY, 
      10],                    
    [ST7735_DISPON ,    DELAY, 
      100]]