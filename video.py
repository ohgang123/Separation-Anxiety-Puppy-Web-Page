st.title("이상행동 감지 시 강아지 사진 실시간 확인")
import streamlit as st
import os


# train2 폴더의 1.png~9.png 이미지를 3x3 그리드로 표시
img_dir = os.path.join(os.path.dirname(__file__), "train2")
img_files = [f"{i}.png" for i in range(1, 10)]

rows = [img_files[i:i+3] for i in range(0, 9, 3)]
for row in rows:
    cols = st.columns(3)
    for idx, img_name in enumerate(row):
        img_path = os.path.join(img_dir, img_name)
        if os.path.exists(img_path):
            cols[idx].image(img_path, caption=f"{img_name}", use_container_width=True)
        else:
            cols[idx].warning(f"{img_name} 파일이 없습니다.")
