# -*- coding: utf-8 -*-

import personInfo
import linkedlist

class addressbook(object):
    def __init__(self):
        self.MENU_INPUT = 1
        self.MENU_REMOVE = 2
        self.MENU_MODIFY = 3
        self.MENU_SEARCH = 4
        self.MENU_ALL_PRINT = 5
        self.MENU_SAVE = 6
        self.MENU_LOAD = 7
        self.MENU_FINISH = 0
        self.ERROR_NO_MENU = 1
        self.ERROR_FULL = 2
        self.ERROR_EMPTY = 3
        self.ERROR_NOT_SEARCH = 4
        self.ERROR_LOAD_FAIL = 5
        self.list = linkedlist.linkedlist()

    def __del__(self):
        self.list.deleteAll()

        del self.list

    def printMainMenu(self):
        print """\
1. 주소정보를 입력한다.
2. 주소정보를 삭제한다.
3. 주소정보를 수정한다.
4. 주소정보를 검색한다.
5. 전체 주소록을 출력한다.
6. 주소록 파일에 저장한다.
7. 주소록 파일을 불러온다.
0. 종료한다."""

    def print_finish(self):
        print "프로그램을 종료합니다."

    def print_error(self, error):
        if error == self.ERROR_NO_MENU:
            print "없는 번호를 입력하였습니다."
        elif error == self.ERROR_FULL:
            print "주소록이 가득 찼습니다."
        elif error == self.ERROR_EMPTY:
            print "주소록이 비어있습니다."
        elif error == self.ERROR_NOT_SEARCH:
            print "주소정보를 찾을 수 없습니다."
        elif error == self.ERROR_LOAD_FAIL:
            print "addressbook.dat 파일을 불러올수 없습니다."
        else:
            pass

    def isEmpty(self):
        isEmpty = True

        if (self.list.get_length() > 0):
            isEmpty = False

        return isEmpty

    def input(self):
        info = personInfo.personInfo()

        info.name = raw_input("이름 : ")
        info.phone = raw_input("전화번호 : ")
        info.address = raw_input("주소 : ")

        print "입력된 정보"
        self.printHeader(-1)
        self.printPersonInfo(info, -1)

        yesno = raw_input("추가하시겠습니까 ? (y/n) :")

        if (yesno == 'y'):
            self.list.append(info)
            print "추가되었습니다."

    def remove(self):
        if (self.isEmpty() == True):
            self.print_error(self.ERROR_EMPTY)
            return None

        name = raw_input("삭제할 이름: ")

        removeIndex = self.list.find(name)

        if (removeIndex == -1):
            self.print_error(self.ERROR_NOT_SEARCH)
            return None

        self.printHeader(-1)
        self.printPersonInfo(self.list.viewAt(removeIndex), -1)

        yesno = raw_input("삭제하겠습니까? (y/n) :")

        if (yesno == 'y'):
            self.list.deleteNode(removeIndex)
            print "삭제되었습니다."

    def modify(self):
        if (self.isEmpty() == True):
            self.print_error(self.ERROR_EMPTY)
            return None
        
        name = raw_input("수정할 이름: ")
        
        modifyIndex = self.list.find(name)
        
        if (modifyIndex == -1):
            self.print_error(self.ERROR_NOT_SEARCH)
            return None
        
        self.printHeader(-1)
        self.printPersonInfo(self.list.viewAt(modifyIndex), -1)
        
        yesno = raw_input("수정하겠습니까? (y/n) :")
        
        info = personInfo.personInfo()
        
        if (yesno == 'y'):
            info.name = raw_input("이름 : ")
            info.phone = raw_input("전화번호 : ")
            info.address = raw_input("주소 : ")
        
            print "수정된 정보"
        
            target = self.list.getNode(modifyIndex)

            target.data = info

            self.printHeader(-1)
            self.printPersonInfo(target.data, -1)
            print "수정되었습니다."

    def search(self):
        info = personInfo.personInfo()

        if (self.isEmpty() == True):
            self.print_error(self.ERROR_EMPTY)
            return None

        name = raw_input("검색할 이름: ")

        info.name = name
        
        foundIndex = self.list.find(info)
        
        if (foundIndex == -1):
            self.print_error(self.ERROR_NOT_SEARCH)
            return None

        self.printHeader(-1)
        self.printPersonInfo(self.list.viewAt(foundIndex), -1)

    def printHeader(self, printNum):
        print "----------------------------------------------"
        if (printNum != -1):
            print "번호  이름     전화번호      주소"
        else:
            print "이름     전화번호      주소"
        print "----------------------------------------------"

    def printPersonInfo(self, info, printNum):
        if (printNum != -1):
            print "%-4s" % printNum,
        print "%-7s %-14s %-50s" % (info.name, info.phone, info.address)
        #print info

    def printAll(self):
        number = 1
        
        if (self.isEmpty() == True):
            self.print_error(self.ERROR_EMPTY)
            return None 
        
        self.printHeader(1)
        target = self.list.moveFirst()
        while (self.list.isTail() != True):
            self.printPersonInfo(target.data, number)
            target = self.list.moveNext()
            number = number + 1

    def save(self):
        if (self.isEmpty() == True):
            self.print_error(self.ERROR_EMPTY)
            return None

        target = self.list.moveFirst()

        with open('addressbook.dat','w') as f:
            while (self.list.isTail() != True):
                f.write(target.data.name + '\n')
                f.write(target.data.phone + '\n')
                f.write(target.data.address + '\n')
                target = self.list.moveNext()

        print "addressbook.dat 파일에 저장하였습니다."

    def load(self):
        self.list.deleteAll()

        f = open('addressbook.dat','r')
        f.seek(0,2)
        eof = f.tell()
        f.seek(0)
        while True:
            info = personInfo.personInfo()
            info.name = f.readline().rstrip('\n')
            info.phone = f.readline().rstrip('\n')
            info.address = f.readline().rstrip('\n')
            self.list.append(info)
            if eof == f.tell(): break

        print "addressbook.dat 파일을 불러왔습니다."

    def testSetup(self):
        samples = []

        info = personInfo.personInfo()
        info.name = "aaa"
        info.phone = "0001112222"
        info.address = "acb"
        samples.append(info)

        info = personInfo.personInfo()
        info.name = "bbb"
        info.phone = "000111333"
        info.address = "acb"
        samples.append(info)

        info = personInfo.personInfo()
        info.name = "ccc"
        info.phone = "000111444"
        info.address = "acb"
        samples.append(info)

        info = personInfo.personInfo()
        info.name = "ddd"
        info.phone = "0001115555"
        info.address = "acb"
        samples.append(info)

        info = personInfo.personInfo()
        info.name = "eee"
        info.phone = "0001116666"
        info.address = "acb"
        samples.append(info)

        info = personInfo.personInfo()
        info.name = "fff"
        info.phone = "0001117777"
        info.address = "acb"
        samples.append(info)

        info = personInfo.personInfo()
        info.name = "ggg"
        info.phone = "0001118888"
        info.address = "acb"
        samples.append(info)

        info = personInfo.personInfo()
        info.name = "hhh"
        info.phone = "0001119999"
        info.address = "acb"
        samples.append(info)

        info = personInfo.personInfo()
        info.name = "iii"
        info.phone = "0002220000"
        info.address = "acb"
        samples.append(info)

        info = personInfo.personInfo()
        info.name = "jjj"
        info.phone = "0002221111"
        info.address = "acb"
        samples.append(info)
        
        for index in range(10):
            self.list.append(samples[index])
