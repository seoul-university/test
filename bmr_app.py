import streamlit as st

def calculate_bmr(sex, weight, height, age):
    if sex == "남":
        return 66.47 + (13.75 * weight) + (5.003 * height) - (6.755 * age)
    elif sex == "여":
        return 655.1 + (9.563 * weight) + (1.850 * height) - (4.676 * age)
    else:
        return None

def adjust_bmr_by_sleep(bmr, sleep_hours):
    deviation = sleep_hours - 7.5
    adjustment_factor = 1 + (deviation * 0.02)
    return bmr * adjustment_factor

def interpret_sleep(sleep_hours):
    if sleep_hours < 6:
        return "❗ 수면 부족 상태입니다. 대사 효율이 낮아질 수 있어요."
    elif sleep_hours < 7.5:
        return "⚠️ 약간의 수면 부족입니다. 피로 누적이 예상됩니다."
    elif sleep_hours <= 9:
        return "✅ 수면이 충분하여 대사 활동이 원활할 가능성이 높습니다."
    else:
        return "ℹ️ 수면이 과도할 수 있어요. 리듬 유지를 주의하세요."

# Streamlit UI
st.title("🧠 수면 기반 기초대사율(BMR) 계산기")

sex = st.radio("성별을 선택하세요", ("남", "여"))
weight = st.number_input("체중 (kg)", min_value=30.0, max_value=150.0, value=65.0)
height = st.number_input("신장 (cm)", min_value=130.0, max_value=210.0, value=175.0)
age = st.number_input("나이 (세)", min_value=10, max_value=100, value=17)
sleep_hours = st.slider("수면 시간 (시간)", min_value=3.0, max_value=12.0, step=0.5, value=7.0)

if st.button("BMR 계산하기"):
    bmr_base = calculate_bmr(sex, weight, height, age)
    bmr_adjusted = adjust_bmr_by_sleep(bmr_base, sleep_hours)
    comment = interpret_sleep(sleep_hours)

    st.subheader("📋 결과 요약")
    st.write(f"기초대사율 (BMR): **{bmr_base:.2f} kcal/day**")
    st.write(f"수면 조정 후 BMR: **{bmr_adjusted:.2f} kcal/day**")
    st.info(comment)
