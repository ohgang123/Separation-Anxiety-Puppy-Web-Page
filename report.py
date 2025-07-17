st.title("분리불안 알람 일별 리포트")
import streamlit as st
import pandas as pd


# 예시 데이터
data = {
    "행동": ["anxiety", "scratch", "taillow"],
    "횟수": [3, 2, 4]
}
df = pd.DataFrame(data)

st.subheader("행동별 감지 횟수")
st.dataframe(df, use_container_width=True)

# 예쁜 컬러 바 차트
import altair as alt
bar = alt.Chart(df).mark_bar(cornerRadiusTopLeft=8, cornerRadiusTopRight=8).encode(
    x=alt.X('행동', sort=None, title='행동'),
    y=alt.Y('횟수', title='감지 횟수'),
    color=alt.Color('행동', scale=alt.Scale(scheme='set2'), legend=None),
    tooltip=['행동', '횟수']
).properties(
    width=400,
    height=300,
    title="행동별 감지 횟수 시각화"
)
st.altair_chart(bar, use_container_width=True)

# 예쁜 원형 차트
pie = alt.Chart(df).mark_arc(innerRadius=50).encode(
    theta=alt.Theta(field="횟수", type="quantitative"),
    color=alt.Color(field="행동", type="nominal", scale=alt.Scale(scheme='set2')),
    tooltip=['행동', '횟수']
).properties(
    width=400,
    height=300,
    title="행동별 비율"
)
st.altair_chart(pie, use_container_width=True)
