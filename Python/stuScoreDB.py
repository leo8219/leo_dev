student = dict()

while True:
    select = int(input("[실행 메뉴 선택]\n1. 성적신규입력\n2. 성적조회\n3. 성적수정\n4. 성적삭제\n5. 성적출력\n6. 종료\n입력 >> "))

    if(select<1 or select>6):
        print("유효한 숫자를 입력하세요")
        continue
    else:
        if(select == 1):
            stuNum = int(input("학번을 입력하세요:"))
            if(stuNum not in student)== True:
                name = input("이름 : ")
                kor = int(input("국어 성적 : "))
                mth = int(input("수학 성적 : "))
                eng = int(input("영어 성적 : "))
                snc = int(input("과학 성적 : "))
                total = kor+mth+eng+snc
                avg = total/4
                student[stuNum] = [name, kor, mth, eng, snc, total, avg]
                print("성적입력완료")
                continue
            else:
                print("DB에 학생이 이미 존재합니다")
        elif(select == 2):
            search = int(input("조회할 학번을 입력하세요: "))
            if(search in student) == True:
                info = student[search]
                print("이름\t국어\t수학\t영어\t과학\t총점\t평균")
                for i in range(len(info)):
                    print(info[i:i+1],end='\t')
                print("학생조회를 완료하였습니다")
                continue
            else:
                print("DB에 학생이 존재하지 않습니다")
        elif(select == 3):
            update = int(input("수정할 학번을 입력하세요: "))
            if(search in student) == True:
                name = input("이름 : ")
                kor = int(input("국어 성적 : "))
                mth = int(input("수학 성적 : "))
                eng = int(input("영어 성적 : "))
                snc = int(input("과학 성적 : "))
                total = kor+mth+eng+snc
                avg = total/4
                student[update] = [name,kor,mth,eng,snc,total]
                print("수정을 완료하였습니다")
                continue
            else:
                print("DB에 학생이 존재하지 않습니다")
                continue
        elif(select == 4):
            delete = int(input("삭제할 학번을 입력하세요 : "))
            if(delete in student) == True:
                student.pop(delete)
                print("삭제를 완료하였습니다")
                continue
            else:
                print("DB에 학생이 존재하지 않습니다")
                continue
        elif(select == 5):
            print("DB 전체 내용을 출력합니다")
            print("이름\t국어\t수학\t영어\t과학\t총점\t평균")
            for id in student:
                info = student[id]
                for i in range(len(info)):
                    print(info[i:i+1],end='\t')
                print()
            print("DB 출력을 완료하였습니다")
            continue
                
        elif(select == 6):
            print("프로그램을 종료합니다.")
            break