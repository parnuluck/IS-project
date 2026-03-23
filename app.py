import streamlit as st

st.set_page_config(
    page_title="AI Health & Sentiment App",
    page_icon="🤖",
    layout="wide"
)

# -----------------------------
# 🎨 Minimal Style
# -----------------------------
st.markdown("""
<style>
.title {
    font-size:40px;
    font-weight:700;
}
.subtitle {
    font-size:18px;
    color:#6b7280;
}
.name {
    font-size:16px;
    color:#9ca3af;
}
.card {
    padding:18px;
    border-radius:12px;
    background-color:#f9fafb;
    border:1px solid #e5e7eb;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Header
# -----------------------------
col1, col2 = st.columns([1, 4])

with col1:
    st.markdown("""
    <img src="https://media.discordapp.net/attachments/872884301421748244/1292779900159266916/Q1.jpg?ex=69c2589a&is=69c1071a&hm=0ec3ea63b3c8353b3b7037bda444eb9307d01b9d64175aabfc8fedceb7f1b206&=&format=webp&width=644&height=859"
    width="120" style="border-radius:50%;">
    """, unsafe_allow_html=True)

with col2:
    st.markdown('<div class="title">AI Prediction Dashboard</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Diabetes Prediction & Sentiment Analysis</div>', unsafe_allow_html=True)
    st.markdown('<div class="name">Parnuluck Saetang 6704062612359</div>', unsafe_allow_html=True)

st.divider()

# -----------------------------
# About
# -----------------------------
st.subheader("About")

st.write("""
This project combines Machine Learning and Neural Network models to analyze two types of data:

• Diabetes prediction from health data  
• Sentiment analysis from text reviews  
""")

# -----------------------------
# Features
# -----------------------------
st.subheader("Features")

col1, col2, col3 = st.columns(3)

with col1:
    with st.container(border=True):
        st.markdown("**Diabetes Prediction**")
        st.write("""
        • Random Forest  
        • Gradient Boosting  
        • Logistic Regression
        """)

with col2:
    with st.container(border=True):
        st.markdown("**Neural Network**")
        st.write("""
        • TF-IDF  
        • MLP Classifier  
        • NLP Processing
        """)

with col3:
    with st.container(border=True):
        st.markdown("**Sentiment Result**")
        st.write("""
        • Positive 😊  
        • Negative 😡  
        • Real-time
        """)

# -----------------------------
# Stats
# -----------------------------
st.subheader("Overview")

col1, col2, col3 = st.columns(3)

col1.metric("ML Accuracy", "75%")
col2.metric("NN Accuracy", "85%")
col3.metric("Dataset Size", "5K+")

# -----------------------------
# Guide
# -----------------------------
st.subheader("How to Use")

st.write("""
1. Open ML Model → View diabetes prediction  
2. Open NN Model → Explore training results  
3. Open Test ML → Try input 
4. Open Test NN → Try your own input  
""")

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.caption("Simple • Clean • Functional")
