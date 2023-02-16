import csv


def ReadFromCSVFile(path):
    Data_List = []
    with open(path, newline='', encoding='utf-8') as CSVFile:
        # csv.reader(csvFile, delimiter='[,: ]')
        DataRows = csv.reader(CSVFile)
        for row in DataRows:
            Data_List.append(row)
    return Data_List


def ReadFromSchoolCSVFile(path):
    Data_List = []
    with open(path, newline='') as CSVFile:
        # csv.reader(csvFile, delimiter='[,: ]')
        DataRows = csv.reader(CSVFile)
        for row in DataRows:
            Data_List.append(row)
    return Data_List


def DictionaryReadFromCSVFile(path):
    with open(path, newline='', encoding='utf-8') as CSVFile:
        # csv.reader(csvFile, delimiter='[,: ]')
        DataRows = csv.DictReader(CSVFile)
        for row in DataRows:
            # print(row['columns'], row['columns'])
            print()


def WriteToCSVFile(path, TextList):
    with open(path, 'a', newline='', encoding='utf-8') as OutputFile:
        OutputWriter = csv.writer(OutputFile, delimiter='\t')
        for row in TextList:
            OutputWriter.writerow(row)


def input_attend_list(DataList, studentList):
    for data in DataList:
        student_ID = data[2]
        student_Name = data[3]
        for student in studentList:
            student_ID_inData = student[1]
            student_Name_inData = student[2]
            if student_ID == student_ID_inData and student_Name == student_Name_inData:
                student.append(1)
    for student in studentList:
        if len(student) != len(studentList[0]):
            student.append(0)
    return studentList


def WriteToCSVFile(path, InputList):
    with open(path, 'a', newline='') as OutputFile:
        OutputWriter = csv.writer(OutputFile, delimiter=',')
        for row in InputList:
            OutputWriter.writerow(row)


path = r'C:\Users\User\Downloads\1103DS'
file_name = r'\student1.csv'
student_list = ReadFromSchoolCSVFile(path + file_name)
print(student_list)
file_name = r'\0630.csv'
data_list = ReadFromCSVFile(path + file_name)
Input_List = input_attend_list(data_list, student_list)
file_name = r'\0714.csv'
data_list = ReadFromCSVFile(path + file_name)
Input_List = input_attend_list(data_list, student_list)
file_name = r'\0727.csv'
data_list = ReadFromCSVFile(path + file_name)
Input_List = input_attend_list(data_list, student_list)
print(Input_List)
file_name = r'\student_result.csv'
WriteToCSVFile(path + file_name, Input_List)

