# -*- coding:gbk -*-
__author__ = 'Yu'

import Image
import win32gui,win32con,win32api
import urllib,re,sys,os

def setWallpaperFromBMP(imagepath):
    k = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Panel\\Desktop",0,win32con.KEY_SET_VALUE)
    win32api.RegSetValueEx(k, "WallpaperStyle", 0, win32con.REG_SZ, "2")
    win32api.RegSetValueEx(k, "TileWallpaper", 0, win32con.REG_SZ, "0")
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER,imagepath, 1+2)

def setWallPaper(imagePath):
    bmpImage = Image.open(imagePath)
    newPath = imagePath.replace('.jpg', '.bmp')
    bmpImage.save(newPath, "BMP")
    setWallpaperFromBMP(newPath)

def get_bing_backphoto():
    if (os.path.exists('c:/bingPhotos')== False):
        os.mkdir('c:/bingPhotos')
    url = 'http://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&nc=1361089515117&FORM=HYLH1'
    html = urllib.urlopen(url).read()
    if html == 'null':
        print 'open & read bing error!'
        sys.exit(-1)
    reg = re.compile('"url":"(.*?)","urlbase"',re.S)
    text = re.findall(reg,html)
#http://s.cn.bing.net/az/hprichbg/rb/LongJi_ZH-CN8658435963_1366x768.jpg
    for imgurl in text:
        right = imgurl.rindex('/')
        name = imgurl.replace(imgurl[:right+1],'')
        savepath = 'c:/bingPhotos/'+ name
        urllib.urlretrieve(imgurl, savepath)
        print name + ' save success!'
        return savepath

if __name__ == '__main__':
     setWallPaper(get_bing_backphoto())