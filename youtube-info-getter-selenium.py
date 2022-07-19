from selenium import webdriver
import time

tfile = open("table.txt","a",encoding="utf-8")
dfile = open("duration.txt","a",encoding="utf-8")
idfile = open("ids.txt","a",encoding="utf-8")

driver = webdriver.Firefox()

#path = input("Oynatma Adresini Giriniz: ")
driver.get("https://www.youtube.com/watch?v=vwB5ybA1nTo&list=PLnojrglWmasetflw8jDA9JkWSiTUeDtQv")
time.sleep(2)
playlistObjects = driver.find_elements_by_xpath('.//*[@id="playlist-items"]')

for each in range(len(playlistObjects)):
    title = playlistObjects[each].find_element_by_xpath('.//*[@id="video-title"]').text
    duration = playlistObjects[each].find_element_by_id('text').get_attribute("aria-label")
    videoID = playlistObjects[each].find_element_by_xpath('.//a').get_attribute("href")[32:43]
    duration = str(duration)

    editor = duration.split(" ")
    editor.pop(-1)
    if(len(editor) == 3):
        if(len(editor[0]) == 2):
            editor.insert(0,"00")
            editor.insert(1,"saat")
        else:
            editor.append(":00")


    sayi = 0
    duration = ""

    for each in range(len(editor)):
        sayi += 1
        if(sayi%2 == 0 and each != (len(editor)-1)):
            editor[each] = ":"
        else:
            if(len(editor[each]) == 1):
                editor[each] = "0"+editor[each]
        duration += editor[each]

    #title = title[:title.find(" | S")]

    tfile.write(title+"\n")
    dfile.write(duration+"\n")
    idfile.write(videoID+"\n")
    each += 1

print("Bitti")
tfile.close
dfile.close
idfile.close
driver.close
driver.quit



