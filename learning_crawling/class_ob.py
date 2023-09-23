
# 게임 정보제공 사이트를 만들고 싶당 
# 캐릭터마다 정보를 자료형으로 정리해야됨

# 2개의 캐릭을 정의
""" nunu = {
    'q' : 'eat', 
    'w' : 'snowball'
    }

garen = {
    'q' : 'strike', 
    'w' : 'courage'
    } """  
# 가렌 = 누누 => 이런 경우 같은 주소를 공유하기 때문에 값을 바꾸면 모든 오브젝트의 값이 변경된다. 
# 복사가 되는 것이 아닌 값을 공유하는게 되버림

# 이런게 몇 백개 있는 경우에는 object 자료형을 사용한다.
# 오브젝트 만드는 문법
# 오브젝트.q = 'eat' 

# 오브젝트 한줄 컷 해주는 기계
class Hero :
    x = 123 # 이 값은 모든 오브젝트(케릭터)들이 공유하는 값이 된다.
    # 오브젝트가 생성될 때 초기화 작업을 하는 함수 
    def __init__(self, skill1, skill2):  # self는 새로 생성될 오브젝트를 말함
        # 이 안의 값들만 각 오브젝트마다 달라짐
        self.q = skill1
        self.w = skill2
    
    # 무조건 self를 넣어줘야함
    def hello(self) :
        print("안녕~@")



# 오브젝트 생성 
누누 = Hero('eat', 'snowball')
가렌 = Hero('strike', 'courage')


print(누누.q)
print(가렌.q)
누누.hello()