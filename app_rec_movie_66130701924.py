
import streamlit as st
import pickle
from myfunction_66130701924 import get_movie_recommendations

# ====== ส่วนหัวของเว็บ ======
st.set_page_config(page_title="🎬 Movie Recommendation App", layout="centered")
st.title("🎥 Movie Recommendation System")
st.markdown("แอปนี้ใช้ข้อมูลจากโมเดล Collaborative Filtering เพื่อแนะนำภาพยนตร์ที่เหมาะกับคุณ")

# ====== โหลดข้อมูล ======
with open("recommendation_data.pkl", "rb") as file:
    user_similarity_df, user_movie_ratings = pickle.load(file)

# ====== UI: เลือก user ======
all_users = user_movie_ratings.index.tolist()
user_id = st.selectbox("เลือก User ID:", all_users, index=0)

# ====== UI: กำหนดจำนวนภาพยนตร์ที่ต้องการแนะนำ ======
num_recs = st.slider("จำนวนภาพยนตร์ที่ต้องการแนะนำ:", 1, 20, 10)

# ====== ปุ่มประมวลผล ======
if st.button("🎯 แนะนำภาพยนตร์"):
    recommendations = get_movie_recommendations(user_id, user_similarity_df, user_movie_ratings, num_recs)
    
    if recommendations:
        st.success(f"ภาพยนตร์แนะนำสำหรับผู้ใช้ **User {user_id}**:")
        for i, movie_title in enumerate(recommendations, start=1):
            st.write(f"{i}. 🎬 {movie_title}")
    else:
        st.warning("ไม่พบคำแนะนำสำหรับผู้ใช้นี้ 😅")

# ====== Footer ======
st.markdown("---")
st.caption("Developed with ❤️ using Streamlit")

