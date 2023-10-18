#####################################################
# "조선별다방" 카페 키오스크 프로그램
#   - 일자: 2023년10월13일
#   - 작성자: cholong02
#   - 내용: 카페 음료를 주문 및 판매하는 콘솔 프로그램

from service_kiosk import user_choice, show_menu

# 메뉴와 가격표
#  - Dict Type → 데이터베이스 대체
main_name = {1: "커피(Coffee)", 2: "음료(Drink)", 3: "빵(Bakery)"}

coffee_name = {1: "아메리카노", 2: "카페라떼", 3: "콜드브루", 4: "에스프레소"}
coffee_price = {1: 1500, 2: 3000, 3: 5000, 4: 1000}

drink_name = {1: "스무디", 2: "버블티", 3: "에이드", 4: "생과일주스", 5: "탄산"}
drink_price = {1: 2500, 2: 3000, 3: 2000, 4: 5000, 5: 1000}

bakery_name = {1: "카스테라", 2: "케이크", 3: "허니브레드"}
bakery_price = {1: 4000, 2: 8000, 3: 6000}

# 고객 주문 기록 저장
menu_save = []    # 고객 주문 메뉴 기록
price_save = []   # 고객 주문 가격 기록

# 1.메인 메뉴 출력
while True:
    print("■" * 50)
    print("■■ == 조선별다방 == ")
    print("■■ == ver 1.2")
    print("■■ 메인 메뉴")
    show_menu(main_name)

    # 2.메인 메뉴 선택
    choice = user_choice(len(main_name), "main")

    # 3.서브 메뉴 출력
    if choice == 1:     # 커피
        print("●● 커피(Coffee)")
        show_menu(coffee_name)
    # 4. 서브 메뉴 선택
        choice = user_choice(len(coffee_name))
    # 5. 선택 베뉴 주문 목록 저장
        menu_save.append(coffee_name[choice])
        price_save.append(coffee_price[choice])
    elif choice == 2:   # 음료
        print("●● 음료(Drink)")
        show_menu(drink_name)
        choice = user_choice(len(drink_name))
        menu_save.append(drink_name[choice])
        price_save.append(drink_price[choice])
    elif choice == 3:   # 빵
        print("●● 빵(Bakery)")
        show_menu(bakery_name)
        choice = user_choice(len(bakery_name))
        menu_save.append(bakery_name[choice])
        price_save.append(bakery_price[choice])
    elif choice == 99:
        print("MSG: 조선별다방 키오스크를 종료합니다.")
        exit()

    # 6. 추가 주문  yes or no?
    print("●○ 추가 주문 하시겠습니까?(y/n)")
    flag = 0 # 추가 주문 y/n 여부
    while True:
        choice_yn = input("y/n: ")

        if choice_yn == "y" or choice_yn == "Y":
            break
        elif choice_yn.lower() == "n":
            flag = 1
            break

        else:
            print("MSG: y 또는 n만 입력 하세요.")

# 7. 주문 내역 출력!
    if flag == 1:
        print("="*50)
        print("== 고객님이 주문 하신 메뉴 ==")
        for i, menu in enumerate(menu_save):
            print(f"{i+1}.{menu}")

        total_price = 0  # 총 결제 금액
        for price in price_save:
            total_price += price
        print(f"MSG: 주문 하신 메뉴는 {len(menu_save)}개로 총 결제 금액은 {total_price}원 입니다.")
        print("MSG: 이용해 주셔서 감사 합니다.")

