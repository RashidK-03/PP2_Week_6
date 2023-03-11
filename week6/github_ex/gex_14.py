import os
def main():
    filePath = '/This PC/Data (D:)/Programming/PyCharm ENG/helloworld';

    os.remove('/This PC/Data (D:)/Programming/PyCharm ENG/helloworld')

    if os.path.exists(filePath):
        os.remove(filePath)
    else:
        print("Can not delete the file as it doesn't exists")

    try:
        os.remove(filePath)
    except:
        print("Error while deleting file ", filePath)

    try:
        os.ulink(filePath)
    except:
        print("Error while deleting file ", filePath)
if __name__ == '__main__':
    main()