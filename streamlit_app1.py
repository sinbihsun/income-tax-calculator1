# streamlit_app.py
import streamlit as st

st.set_page_config(page_title="소득세 계산기", page_icon="💰", layout="centered")

st.title("💰 2025 한국 소득세 계산기 (누진공제)")
st.caption("연소득(과세표준 기준)을 입력하면 누진공제로 산출세액을 계산합니다.")

def compute_tax(income: int):
    # 2025년 기준 누진공제 방식
    if income <= 14_000_000:
        rate, deduction, level = 0.06, 0, "저소득층"
    elif income <= 50_000_000:
        rate, deduction, level = 0.15, 1_260_000, "중간소득층"
    elif income <= 88_000_000:
        rate, deduction, level = 0.24, 5_760_000, "고소득층"
    elif income <= 150_000_000:
        rate, deduction, level = 0.35, 15_440_000, "상위소득층"
    elif income <= 300_000_000:
        rate, deduction, level = 0.38, 19_940_000, "초고소득층"
    elif income <= 500_000_000:
        rate, deduction, level = 0.40, 25_940_000, "초고소득층"
    elif income <= 1_000_000_000:
        rate, deduction, level = 0.42, 35_940_000, "초고소득층"
    else:
        rate, deduction, level = 0.45, 65_940_000, "초고소득층"

    tax = income * rate - deduction
    return tax, rate, level

st.subheader("입력")
income = st.number_input("연소득(과세표준, 원)", min_value=0, step=100_000, value=55_000_000, format="%d")

if st.button("세금 계산"):
    tax, rate, level = compute_tax(income)
    st.success("계산 완료!")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("소득 수준", level)
        st.write(f"적용 세율: **{int(rate*100)}%**")
    with col2:
        st.metric("예상 소득세", f"{tax:,.0f} 원")

st.divider()
with st.expander("참고: 현재 저장된 단순 if-else 예시도 실행해보기"):
    st.code(
        '''income = 55000000
tax = 0
if income <= 12000000:
    level = "저소득층"; tax = income * 0.06
elif income <= 46000000:
    level = "중간소득층"; tax = income * 0.15
elif income <= 88000000:
    level = "고소득층"; tax = income * 0.24
else:
    level = "초고소득층"; tax = income * 0.35
print(level, tax)''',
        language="python"
    )
st.caption("※ 실제 계산은 위 누진공제 로직을 사용합니다. 총급여 → 과세표준 변환은 포함되어 있지 않습니다.")
