import streamlit as st

st.set_page_config(
    page_title="Pixel AI Lab",
    page_icon="🧪",
    layout="wide"
)

# -----------------------------
# 🎨 Pixel Style CSS
# -----------------------------
st.markdown("""
<style>
body {
    background-color: #0f172a;
}

.pixel-title {
    font-size: 48px;
    font-weight: bold;
    color: #22c55e;
    text-shadow: 3px 3px #000;
    font-family: monospace;
}

.pixel-sub {
    font-size: 18px;
    color: #94a3b8;
    font-family: monospace;
}

.card {
    background-color: #1e293b;
    padding: 20px;
    border-radius: 10px;
    border: 2px solid #22c55e;
    box-shadow: 4px 4px #000;
}

.center {
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# 🖼️ Pixel Banner
# -----------------------------
st.image(
    "https://images.unsplash.com/photo-1550745165-9bc0b252726f",
    use_container_width=True
)

# -----------------------------
# Header
# -----------------------------
col1, col2 = st.columns([1, 4])

with col1:
    st.markdown("""
    <img src="https://media.discordapp.net/attachments/872884301421748244/1292779900159266916/Q1.jpg"
    width="120" style="border-radius:50%; border:3px solid #22c55e;">
    """, unsafe_allow_html=True)

with col2:
    st.markdown('<div class="pixel-title">🧪 Pixel AI Lab</div>', unsafe_allow_html=True)
    st.markdown('<div class="pixel-sub">Diabetes Prediction & Sentiment Engine</div>', unsafe_allow_html=True)

st.markdown("<div class='pixel-sub'>Developed by: Parnuluck Saetang</div>", unsafe_allow_html=True)

st.divider()

# -----------------------------
# About
# -----------------------------
st.markdown('<div class="pixel-title">📜 About</div>', unsafe_allow_html=True)

st.markdown("""
<div class="pixel-sub">
A retro-inspired AI dashboard that blends healthcare prediction and text intelligence.<br><br>

🩺 Predict diabetes risk using health data  
💬 Analyze sentiment from movie reviews  
</div>
""", unsafe_allow_html=True)

# -----------------------------
# Features (Cards)
# -----------------------------
st.markdown('<div class="pixel-title">⚡ Features</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card center">
    🩺 <b>Diabetes AI</b><br><br>
    Random Forest<br>
    Gradient Boosting<br>
    Logistic Regression
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card center">
    🧠 <b>Neural Network</b><br><br>
    TF-IDF<br>
    MLP Model<br>
    NLP Processing
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card center">
    💬 <b>Sentiment</b><br><br>
    Positive 😊<br>
    Negative 😡<br>
    Real-time
    </div>
    """, unsafe_allow_html=True)

# -----------------------------
# Stats
# -----------------------------
st.markdown('<div class="pixel-title">📊 Stats</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

col1.metric("ML Accuracy", "75%")
col2.metric("NN Accuracy", "85%")
col3.metric("Dataset", "20K+")

# -----------------------------
# How to Use
# -----------------------------
st.markdown('<div class="pixel-title">🕹️ How to Play</div>', unsafe_allow_html=True)

st.markdown("""
<div class="pixel-sub">
1. Open ML Model → Health prediction  
2. Open NN Model → See training results  
3. Open Test NN → Try your own text  
</div>
""", unsafe_allow_html=True)

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.markdown("<div class='pixel-sub center'>Built with ❤️ + caffeine</div>", unsafe_allow_html=True)
