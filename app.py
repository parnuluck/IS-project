import streamlit as st

st.set_page_config(
    page_title="AI Health & Sentiment App",
    page_icon="🤖",
    layout="wide"
)

# -----------------------------
# Header + Profile
# -----------------------------
col1, col2 = st.columns([1, 4])

with col1:
    st.image("https://cdn-icons-png.flaticon.com/512/4712/4712027.png", width=120)

with col2:
    st.title("🤖 AI Prediction Dashboard")
    st.markdown("### Diabetes Prediction & Sentiment Analysis System")

st.markdown("**Developed by: QQQQQ**")  # 👉 เปลี่ยนเป็นชื่อคุณ

st.divider()

# -----------------------------
# Project Description
# -----------------------------
st.subheader("📌 About This Project")

st.write("""
เว็บแอปนี้ใช้ Machine Learning และ Neural Network เพื่อทำนายข้อมูล 2 ประเภท:

1. 🩺 **Diabetes Prediction**  
   - วิเคราะห์ความเสี่ยงโรคเบาหวานจากข้อมูลสุขภาพ  

2. 💬 **Sentiment Analysis**  
   - วิเคราะห์ความรู้สึกจากข้อความรีวิวภาพยนตร์  
""")

# -----------------------------
# Features Section
# -----------------------------
st.subheader("🚀 Features")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("""
🩺 **Diabetes Prediction**

- Random Forest  
- Gradient Boosting  
- Logistic Regression  
- Ensemble Model  
""")

with col2:
    st.info("""
🧠 **Neural Network**

- TF-IDF  
- MLP Classifier  
- NLP Processing  
""")

with col3:
    st.info("""
💬 **Sentiment Result**

- Positive 😊  
- Negative 😡  
- Real-time prediction  
""")

# -----------------------------
# How to Use
# -----------------------------
st.subheader("🧭 How to Use")

st.write("""
1. ไปที่ **ML Model** → ดูการทำนายโรคเบาหวาน  
2. ไปที่ **NN Model** → ดูการวิเคราะห์ข้อความ  
3. ไปที่ **Test NN** → ทดลองพิมพ์รีวิว  
""")

# -----------------------------
# Highlight Section
# -----------------------------
st.subheader("✨ Highlights")

col1, col2 = st.columns(2)

with col1:
    st.success("✔ รองรับทั้งข้อมูลตัวเลขและข้อความ")
    st.success("✔ ใช้ AI วิเคราะห์แบบอัตโนมัติ")

with col2:
    st.success("✔ ใช้งานง่ายผ่าน Web App")
    st.success("✔ แสดงผลแบบ Real-time")

# -----------------------------
# Call to Action
# -----------------------------
st.divider()

st.success("👉 เริ่มใช้งานได้เลยจากเมนูด้านซ้าย!")

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.caption("Developed with ❤️ using Streamlit | AI Project")
