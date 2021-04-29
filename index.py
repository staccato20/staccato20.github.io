class contact:
    def __init__(self, name, call, sex):
        self.name = name
        self.call = call
        self.sex = sex
      
result = []
while True:
    name = input("\n이름을 입력하세요 : ")
    if name == "그만":
        for a in result:
            print("이름은 " + a.name + "," + "전화번호는 " + a.call + "," + "성별은 " + a.sex + "입니다.")

        break
    call = input("전화번호를 입력하세요 : ")
    sex= input("성별을 입력하세요(male이나 female로 작성해주세요) : ")
       
    if sex != "male" and sex != "female":
        sex = "unknown"

    addressbook = contact(name, call, sex)
    result.append(addressbook)

    for a in result:
        print("이름은 " + a.name + "," + "전화번호는 " + a.call + "," + "성별은 " + a.sex + "입니다.")