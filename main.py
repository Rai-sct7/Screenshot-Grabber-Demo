import pywhatkit
import win32api
import win32con
import win32gui
import win32ui


#Create handle
hdesktop = win32gui.GetDesktopWindow()

#Get device dimensions
width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)

#Get device context
desktop_dc = win32gui.GetWindowDC(hdesktop)
img_dc = win32ui.CreateDCFromHandle(desktop_dc)
mem_dc = img_dc.CreateCompatibleDC()

#Create BITMAP object
ss = win32ui.CreateBitmap()
ss.CreateCompatibleBitmap(img_dc,width,height)
mem_dc.SelectObject(ss)

#Copy the screen
mem_dc.BitBlt((0,0),(width,height),img_dc,(left,top),win32con.SRCCOPY)

#Save it to a path
ss.SaveBitmapFile(mem_dc, 'c:\\WINDOWS\\Temp\\screenshot.bmp')

#Free objects
mem_dc.DeleteDC()
win32gui.DeleteObject(ss.GetHandle())

#Whatsapp fun
pywhatkit.sendwhats_image("NUMBER","c:\\WINDOWS\\Temp\\screenshot.bmp","TUFF")
