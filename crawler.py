import requests
from bs4 import BeautifulSoup
import unicodedata


# 方法: 去除\xa0 和 \r
def reformat(text_list):
    # 去掉 \xa0
    try:
        while True:
            text_list.remove('')
    except ValueError:
        pass
    # print(len(textList))
    # print(textList)
    # 去掉 \r
    try:
        while True:
            text_list.remove('\r')
    except ValueError:
        pass
    # print(len(textList))
    # print(textList)
    # 去掉空白格
    for i in range(0, len(text_list)):
        text_list[i] = unicodedata.normalize('NFKD', text_list[i])
        text_list[i] = text_list[i].replace(' ', '')
    # print(len(textList))
    # print(textList)


# 方法: 爬文並存到List
def crawling(url):
    response = requests.get(url)
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "html.parser")

    result = soup.find("div", id="content")

    # print(type(result.getText()))
    return result.getText().split('\n')

    # print(textList)
    # print(len(textList))


# 方法: 找出對話語句
def findDialogue(text_list):
    newList = []
    for sentence in text_list:
        for word in sentence:
            if word == '“':
                newList.append(sentence)
                break

    return newList


# 方法: 擷取出敘述短句的對話語句
def findNarrativeDialogue(text_list):
    for sentence in text_list:
        for word in sentence:
            if word == '“':
                print('“ 在 第 ')
            if word == '”':
                print()


# ”“ “”

# 方法: 從txt檔拉Url
def readTxt():
    with open(r'URL.txt') as f:
        url_list = f.readlines()

        # 去掉\n
        for i in range(0, len(url_list)):
            url_list[i] = url_list[i].replace('\n', '')
        # print(text_list)
        # print(type(text_list))

        return url_list


# 方法: 更改章節
def changeChapter(url):
    response = requests.get(url)
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "html.parser")

    result = soup.find_all("a")

    NextPageString = "下一章"

    for href in result:

        resultText = href.getText
        try:
            print(str(resultText).index(NextPageString))
            print(str(resultText))
            print(href.get('href'))
            return href.get('href')
            break
        except ValueError:
            print("沒有找到")



# 方法: 剔除沒有輔語的對話語句
# def deleteDialodge(text):

# 方法: 順序讀取50章節
def regularLoad(url_text):
    FinishTimes = 0;
    for i in range(1, 200):
        textList = crawling(url_text)
        reformat(textList)
        textList = findDialogue(textList)
        writefile('normal.txt', textList)
        url_text = changeChapter(url_text)
        FinishTimes += 1
        print("章節變更完成 " + FinishTimes)
    print('success')


# 方法: 存入資料
def writefile(text_path, textList):
    with open(text_path, "a", encoding='UTF-8') as file:
        for string in textList:
            file.write(string+'\n')

# 主程式
regularLoad("http://www.uuxs.tw/ls/52_52584/19402701.html")
# changeChapter('http://www.uuxs.tw/ls/52_52584/19402701.html')
#

# print(textList)
