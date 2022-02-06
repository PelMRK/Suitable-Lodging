import pyautogui as pag
import pyperclip
import pandas as pd

addresses = pd.read_csv('addresses.csv', delimiter=',')
print(addresses.loc[0].iloc[1])
text_adr = []
for i in range(len(addresses)):
    text_adr.append(addresses.loc[i].iloc[1])
pag.sleep(1)
routs = pd.Series()

for i in range(len(text_adr)):
    while pag.screenshot().getpixel((30, 305)) != (255, 51, 51):
        pag.sleep(0.05)
    pyperclip.copy('')
    pag.moveTo(393, 301, 0.4)
    pag.sleep(0.15)
    while pag.screenshot().getpixel((393, 301)) == (246, 246, 246):
        pag.sleep(0.05)
    pag.click()
    while pag.screenshot().getpixel((30, 305)) != (255, 255, 255):
        pag.sleep(0.05)
    pag.sleep(0.2)
    pyperclip.copy(text_adr[i])
    pag.hotkey('ctrl', 'V')
    pag.sleep(0.6)
    pag.moveTo(353, 301, 0.15)
    pag.click()
    while pag.screenshot().getpixel((160, 510)) != (246, 246, 246):
        pag.sleep(0.05)
    pag.moveTo(50, 535, 0.5)
    pag.click()
    while pag.screenshot().getpixel((110, 510)) != (255, 255, 255):
        pag.sleep(0.05)
    pag.moveTo(70, 295, 0.3)
    pag.tripleClick()
    pag.sleep(0.6)
    pag.hotkey('ctrl', 'c')
    pag.sleep(0.6)
    res = pyperclip.paste()
    res = res.replace('<div class="masstransit-route-snippet-view__route-duration">', "")
    hrs = 0
    if "ч" in res:
        hrs = int(res.split(" ч")[0])
        res = res.split(" ч")[1]
    if "мин" in res:
        res = int(res.split(" мин")[0])
    else:
        res = 0
    res += hrs*60
    routs.loc[len(routs)] = res
    print(res)
    pag.moveTo(50, 165, 0.5)
    pag.click()

    routs.to_csv("routs.csv", sep=';')
