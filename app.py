import streamlit as st

st.set_page_config(page_title="AI Sentiment Analysis", page_icon="🤖", layout="wide")

# -----------------------------
# Header
# -----------------------------
st.title("🤖 AI Sentiment Analysis Dashboard")
st.markdown("### วิเคราะห์ความรู้สึกจากข้อความด้วย Machine Learning และ Neural Network")

st.divider()

# -----------------------------
# Project Description
# -----------------------------
st.subheader("📌 About This Project")

st.write("""
โปรเจกต์นี้ใช้ Machine Learning และ Neural Network ในการวิเคราะห์ความรู้สึก (Sentiment Analysis) จากข้อความรีวิวภาพยนตร์  

ผู้ใช้สามารถ:
- 🔍 ป้อนข้อความรีวิว
- 🤖 ให้โมเดลวิเคราะห์
- 📊 ดูผลลัพธ์ทันที
""")

# -----------------------------
# Features Section
# -----------------------------
st.subheader("🚀 Features")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("📊 Machine Learning Model\n\n- Random Forest\n- Gradient Boosting\n- Logistic Regression")

with col2:
    st.info("🧠 Neural Network\n\n- TF-IDF\n- MLP Classifier\n- Deep Learning")

with col3:
    st.info("💬 Sentiment Prediction\n\n- Positive 😊\n- Negative 😡")

# -----------------------------
# Navigation Guide
# -----------------------------
st.subheader("🧭 How to Use")

st.write("""
1. ไปที่หน้า **ML Model** เพื่อดูผลลัพธ์ Machine Learning  
2. ไปที่หน้า **NN Model** เพื่อดู Neural Network  
3. ไปที่หน้า **Test NN** เพื่อทดลองพิมพ์รีวิว  
""")

# -----------------------------
# Call to Action
# -----------------------------
st.divider()

st.success("👉 เริ่มใช้งานได้เลยที่เมนูด้านซ้าย!")

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.caption("Developed using Streamlit | Machine Learning Project")
