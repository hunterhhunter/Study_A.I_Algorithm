#리스트만으로 주차관리 프로그램 만들기
from datetime import datetime, timedelta
# 이름, 차종, 번호, 들어온 시간, 나가는 시간 관리 해주는 프로그램
# 요금도 계산해서 받을 거임
car_list = list()

def bring_time():
    now = datetime.now()
    return now

def enter_info():
    car_type = input('차종을 입력해주세요 : ')
    car_number = input('차 번호를 입력해주세요 : ')
    time_enter = bring_time()
    return [car_type, car_number, time_enter]

def 출차():
    if len(car_list) > 0:
        number = input('차량 번호를 입력해주세요 : ')
        li = [r[2] for r in car_list]
        if number in li:
            time_enter = car_list[li.index(number)][3]
            fee = [20000, 1000, 25]  # 하루 2만, 시간 1000, 분당 25
            total_fee = 0
            time_out = bring_time()
            duration = time_out - time_enter
            total_time = [duration.days, duration.seconds // 3600, (duration.seconds % 3600) // 60]
            for i in range(3):
                total_fee += fee[i] * total_time[i]
            car_list.pop(li.index(number))
            print(f'{total_time[0]}일 {total_time[1]}시간 {total_time[2]}분 있어서 총 요금 {total_fee}원 나웠습니다.')
        else:
            print(f'{number} 차량은 이 주차장에 없습니다.\n')
            return
    else:
        print('현재 주차장에 차가 없습니다.')

def 차량목록():
    if len(car_list) > 0:
        for name, car_type, car_number, enter_time in car_list:
            print(f'이름 : {name} 차종 : {car_type} 차량 번호 : {car_number} 들어온 시간 : {enter_time}\n')
    else:
        print('현재 주차장에 차가 없습니다.')

def 입차():
    name = input('이름을 입력해주세요 : ')
    info = enter_info()
    car_list.append([name, info[0], info[1], info[2]])

def 차량검색():
    li = [r[2] for r in car_list]
    if len(car_list) > 0:
        number = input('차량 번호를 입력해주세요 : ')
        if number in li:
            print(f'이름 : {car_list[li.index(number)][0]}, 차종 : {car_list[li.index(number)][1]}, 차량 번호 : {car_list[li.index(number)][2]}, 들어온 시간 : {car_list[li.index(number)][3]}\n')
        else:
            print(f'{number}의 차량은 이 주차장에 없습니다.\n')
    else:
        print('현재 주차장에 차가 없습니다.')

def main():
    lis = [입차, 출차, 차량목록, 차량검색]
    while True:
        lis[int(input(f'원하시는 서비스 번호를 입력해주세요\n'
                        f'1. 입차\n'
                        f'2. 출차\n'
                        f'3. 차량목록\n'
                        f'4. 차량검색\n'))-1]()
if __name__ == '__main__':
    main()