# 소득과 세금 변수 선언
income = 55000000  # 연소득 (예: 5,500만 원)
tax = 0

# 소득 수준 분류 및 세금 계산
if income <= 12000000:
    level = "저소득층"
    tax = income * 0.06  # 6% 세율
elif income <= 46000000:
    level = "중간소득층"
    tax = income * 0.15  # 15% 세율
elif income <= 88000000:
    level = "고소득층"
    tax = income * 0.24  # 24% 세율
else:
    level = "초고소득층"
    tax = income * 0.35  # 35% 세율

# 결과 출력
print(f"소득 수준: {level}")
print(f"예상 세금: {tax:,.0f}원")
