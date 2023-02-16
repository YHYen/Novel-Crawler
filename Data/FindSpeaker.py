#!/usr/bin/python3
# -*- coding: utf-8 -*-
from ltp import LTP

ltp = LTP()
path = r'C:\Users\User\PycharmProjects\ProjectS\Data'
dictionary_name = r'\user_dictionary.txt'
file_name = r'\DialogueData.txt'


def LoadTextFile(FilePath):
    with open(FilePath, encoding='utf-8') as TextFile:
        TextList = TextFile.readlines()
        replaceLine(TextList)
    return TextList


def replaceLine(TextList):
    for i in range(0, len(TextList)):
        TextList[i] = TextList[i].replace('\n', '')
    return TextList


def add_into_user_dictionary(word):
    WriteFile(path, dictionary_name)


def WriteFile(FilePath, TextFile):
    with open(FilePath, 'a', encoding='utf-8') as OutputFile:
        for Text in TextFile:
            OutputFile.write(Text + '\n')


def use_user_dictionary():
    ltp.init_dict(path=path + dictionary_name)


def segmentor(TextList):
    use_user_dictionary()
    segment, hidden = ltp.seg(TextList)
    return segment, hidden


def postagger(hidden):
    postag = ltp.pos(hidden)
    return postag


def sementic_role_labeller(hidden):
    sementic_role = ltp.srl(hidden)
    return sementic_role


def find_speaker(TextList):
    segment, hidden = segmentor(TextList)
    sementic_role = sementic_role_labeller(hidden)
    print(sementic_role)


text_list = LoadTextFile(path+file_name)
find_speaker(text_list)
