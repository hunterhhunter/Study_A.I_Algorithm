# 1. 리스트 객체에 데이터를 담고 제어문과 함수만 사용하여 구성한 프로그램

# 자동차 리스트를 전역 변수로 선언.
car_list = list()

# Python의 리스트는 Container 로서 여러 자료형이 원소로 들어올 수 있다.
def 자동차정보입력():
  car_name = input("차량 이름 입력: ")
  engine_price = int(input("차량 가격 입력: "))
  tire_price = int(input("타이어 가격 입력: "))
  option_name = input("추가할 옵션 입력(공백으로 구분): ").split(" ")
  option = "있음" if len(option_name) > 0 else "없음"
  max_speed = int(input("차량 최고 속도 입력"))
  price = engine_price + tire_price

  # 하나의 차량이므로 하나의 주머니에 묶어서 추가.
  # 출력이 메인 목적이므로 문자열로 정보 담기.
    # 향후 값에 대한 연산 필요 시 문자열 자를 예정.
  car_list.append([f"이름 : {car_name}", f"엔진 가격: {engine_price}", f"타이어 가격: {tire_price}", f"옵션: {option}", f"옵션 이름: {option_name}", f"최고속도: {max_speed}", f"구매 가격: {price}"])

  # None 반환
  return

def 자동차목록보기():
  if len(car_list) == 0:
    print("현재 등록된 자동차가 없습니다.")
  for infos in car_list:
    for info in infos:
      print(info)
  return

def 자동차별구매가격조회():
  if len(car_list) == 0:
    print("현재 등록된 자동차가 없습니다.")
  for infos in car_list:
    for info in infos:
      if "이름 : " in info:
        print(info)
      if "구매 가격 : " in info:
        print(info)
  return

def 옵션보유자동차정보조회():
  if len(car_list) == 0:
    print("현재 등록된 자동차가 없습니다.")
  for infos in car_list:
    for info in infos:
      if "옵션 : 있음" in info:
        print(*infos, sep = "\n")
  return

def 빠른자동차와느린자동차의속도차조회():
  if len(car_list) == 0:
    print("현재 등록된 자동차가 없습니다.")
  speed_list = list()
  for infos in car_list:
    # 차량 정보 전체와 정수형 최고속도를 원소로 하여 speed_list 지역변수에 append
    for info in infos:
      if "최고속도 : " in info:
        speed_list.append([infos, int(info.replace("최고속도 : ", ""))])

  # max 함수 또한 key 파라미터를 보유하고 있으므로 람다식 활용.
  print(max(speed_list, key = lambda x : x[1]))
  print(min(speed_list, key = lambda x : x[1]))
  return

def main():
  cmd_list = [자동차정보입력, 자동차목록보기, 자동차별구매가격조회, 옵션보유자동차정보조회, 빠른자동차와느린자동차의속도차조회, exit()]

  while True:
    cmd_list[int(input(f"""{"#" * 4} 자동차 정보 프로그램 {"#" * 4}
    1. 자동차 정보 입력
    2. 저장된 목록 보기
    3. 각 자동차의 구매 가격 조회
    4. 옵션이 있는 자동차 정보 조회
    5. 빠른 자동차와 느린 자동차의 속도차 조회
    6. 프로그램 이용 종료
    {"#" * 20}
    입력: """)) -1]()

# __name__ 객체가 main 함수의 주소를 가리키고 있을 때 main 함수 실행.
if __name__ == "__main__":
  main()