import Adafruit_BBIO.SPI as SPI
from Adafruit_BBIO.SPI import SPI

import Adafruit_BBIO.GPIO as GPIO



import sys
import time
ST7735_TFTWIDTH  =   128
ST7735_TFTHEIGHT =  160

ST7735_NOP     = 0x00 
ST7735_SWRESET = 0x01
ST7735_RDDID   = 0x04
ST7735_RDDST   = 0x09

ST7735_SLPIN   = 0x10
ST7735_SLPOUT  = 0x11
ST7735_PTLON   = 0x12
ST7735_NORON   = 0x13

ST7735_INVOFF  = 0x20
ST7735_INVON   = 0x21
ST7735_DISPOFF = 0x28
ST7735_DISPON  = 0x29
ST7735_CASET   = 0x2A
ST7735_RASET   = 0x2B
ST7735_RAMWR   = 0x2C
ST7735_RAMRD   = 0x2E

ST7735_PTLAR   = 0x30
ST7735_COLMOD  = 0x3A
ST7735_MADCTL  = 0x36

ST7735_FRMCTR1 = 0xB1
ST7735_FRMCTR2 = 0xB2
ST7735_FRMCTR3 = 0xB3
ST7735_INVCTR  = 0xB4
ST7735_DISSET5 = 0xB6

ST7735_PWCTR1  = 0xC0
ST7735_PWCTR2  = 0xC1
ST7735_PWCTR3  = 0xC2
ST7735_PWCTR4  = 0xC3
ST7735_PWCTR5  = 0xC4
ST7735_VMCTR1  = 0xC5

ST7735_RDID1   = 0xDA
ST7735_RDID2   = 0xDB
ST7735_RDID3   = 0xDC
ST7735_RDID4   = 0xDD

ST7735_PWCTR6  = 0xFC

ST7735_GMCTRP1 = 0xE0
ST7735_GMCTRN1 = 0xE1
DELAY = 0x80
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
GPIO.setup("P9_19", GPIO.OUT)
GPIO.setup("P9_20", GPIO.OUT)









def writecomm(command):
    GPIO.output("P9_19", GPIO.LOW)
    spi.xfer2([command])
    
    
def writedata(data):
    GPIO.output("P9_19", GPIO.HIGH)
    spi.xfer2([data])
    

def st_init():
    GPIO.output("P9_20", GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output("P9_20", GPIO.LOW)
    time.sleep(0.5)
    GPIO.output("P9_20", GPIO.HIGH)
    time.sleep(0.5)
    
    
    isdelay = False
    for i in inittable:
        writecomm(i[0])
        if (i[1] == DELAY):
          isdelay = True
          print("DELAY")
        else:
          isdelay = False
        for j in i[2:]:
          if (isdelay):
            time.sleep(0.5)
            isdelay = False
            print("DELAY FOR", j)
          else:
            writedata(j)
        writecomm(ST7735_MADCTL)
        writedata(0xC0)

def setAddrWindow(x0, y0, x1, y1):
  writecomm(ST7735_CASET)
  writedata(0x00)
  writedata(x0 + 2)
  writedata(0x00)
  writedata(x1 + 2)

  writecomm(ST7735_RASET)
  writedata(0x00)
  writedata(y0 + 1)
  writedata(0x00)
  writedata(y1 + 1)
      
  writecomm(ST7735_RAMWR)


def drawPixel(x, y, color):
  if((x < 0) or (x >= ST7735_TFTWIDTH) or (y < 0) or (y >= ST7735_TFTHEIGHT)):
    return

  setAddrWindow(x,y,x+1,y+1)

  writedata(color >> 8)
  writedata(color)








spi = SPI(0,1)
#spi.bpw(8)
spi.open(0,1)
st_init()
drawPixel(0x23,0x23,0x0000)
drawPixel(0x24, 0x24, 0x0000)