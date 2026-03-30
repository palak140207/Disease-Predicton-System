import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import time
import requests
from streamlit_lottie import st_lottie


st.set_page_config(page_title="Disease Predictor", layout="wide", page_icon="🩺")


page_bg = """
<style>
.stApp {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: #ffffff;
}

.main-header {
    text-align: center;
    color: #ffffff;
    font-size: 3em;
    font-weight: bold;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    margin-bottom: 20px;
    animation: bounceIn 1.5s ease-out;
}

@keyframes bounceIn {
    0% {
        opacity: 0;
        transform: scale(0.3);
    }
    50% {
        opacity: 1;
        transform: scale(1.05);
    }
    70% {
        transform: scale(0.9);
    }
    100% {
        opacity: 1;
        transform: scale(1);
    }
}

.symptom-card {
    background: rgba(255, 255, 255, 0.1);
    border-radius: 15px;
    padding: 20px;
    margin: 10px;
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.2);
    animation: slideInUp 0.8s ease-out;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.symptom-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 30px rgba(0,0,0,0.3);
}

@keyframes slideInUp {
    from {
        opacity: 0;
        transform: translateY(30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.stButton>button {
    background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
    color: white;
    border: none;
    border-radius: 25px;
    height: 50px;
    font-size: 18px;
    font-weight: bold;
    transition: all 0.3s ease;
    animation: pulse 2s infinite;
}

.stButton>button:hover {
    transform: translateY(-2px) scale(1.05);
    box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    animation: none;
}

@keyframes pulse {
    0% {
        box-shadow: 0 0 0 0 rgba(255, 107, 107, 0.7);
    }
    70% {
        box-shadow: 0 0 0 10px rgba(255, 107, 107, 0);
    }
    100% {
        box-shadow: 0 0 0 0 rgba(255, 107, 107, 0);
    }
}
}

.stSelectbox > div > div {
    background: rgba(255, 255, 255, 0.1);
    border-radius: 10px;
    color: white;
}

.stSelectbox label {
    color: #ffffff !important;
    font-weight: bold;
}

.prediction-result {
    background: rgba(255, 255, 255, 0.2);
    border-radius: 15px;
    padding: 20px;
    margin: 20px 0;
    text-align: center;
    animation: zoomIn 0.6s ease-out;
    border: 2px solid rgba(255, 255, 255, 0.3);
}

@keyframes zoomIn {
    from {
        opacity: 0;
        transform: scale(0.5);
    }
    to {
        opacity: 1;
        transform: scale(1);
    }
}

.footer {
    text-align: center;
    margin-top: 50px;
    color: rgba(255, 255, 255, 0.7);
    animation: fadeInUp 1s ease-out;
}

@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes float {
    0%, 100% {
        transform: translateY(0px);
    }
    50% {
        transform: translateY(-10px);
    }
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# Intro Animation and Video
st.markdown("""
<div style="position: relative; width: 100%; height: 400px; overflow: hidden; border-radius: 15px; margin-bottom: 20px;">
    <video autoplay muted loop style="width: 100%; height: 100%; object-fit: cover; filter: brightness(0.7);">
        <source src="https://sample-videos.com/zip/10/mp4/SampleVideo_1280x720_1mb.mp4" type="video/mp4">
        Your browser does not support the video tag.
    </video>
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); text-align: center; color: white; z-index: 2;">
        <h1 style="font-size: 3em; text-shadow: 2px 2px 4px rgba(0,0,0,0.8); animation: fadeIn 2s ease-in;">🩺 Welcome to Disease Predictor</h1>
        <p style="font-size: 1.5em; text-shadow: 1px 1px 2px rgba(0,0,0,0.8); animation: fadeIn 3s ease-in;">AI-Powered Health Analysis</p>
    </div>
</div>
<style>
@keyframes fadeIn {
    from { opacity: 0; transform: translate(-50%, -60%); }
    to { opacity: 1; transform: translate(-50%, -50%); }
}
</style>
""", unsafe_allow_html=True)

# Loading Animation
with st.spinner("Initializing AI Health System..."):
    time.sleep(1)

def load_lottie(url):
    r = requests.get(url)
    return r.json()

lottie_health = load_lottie("https://assets2.lottiefiles.com/packages/lf20_tutvdkg0.json")
lottie_loading = load_lottie("https://assets5.lottiefiles.com/packages/lf20_usmfx6bp.json")


# Sidebar
with st.sidebar:
    st.title("🩺 About")
    st.write("This AI-powered disease prediction system analyzes your symptoms and provides possible disease predictions.")
    st.write("**⚠️ Disclaimer:** This is not a substitute for professional medical advice.")
    st.write("---")
    st.write("Built with ❤️ using Streamlit & ML")


# Main content
st.markdown('<div class="main-header">🩺 Disease Prediction System</div>', unsafe_allow_html=True)

col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("""
    <div style="animation: float 3s ease-in-out infinite;">
    """, unsafe_allow_html=True)
    st_lottie(lottie_health, height=250)
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.write("### Enter your symptoms below to get an instant prediction")
    st.write("Select 'Yes' or 'No' for each symptom you are experiencing.")


# Dataset and Model
data = {
    'fever':            [1,1,0,1,0,1,0,1,1,1],
    'cough':            [1,0,1,1,0,1,0,1,0,0],
    'headache':         [0,1,0,1,0,1,0,1,1,1],
    'fatigue':          [1,1,0,1,0,1,0,1,1,0],
    'nausea':           [0,1,0,1,0,1,1,0,1,0],
    'vomiting':         [0,1,0,0,0,1,1,0,1,0],
    'body_pain':        [1,1,0,1,0,1,0,1,1,0],
    'sore_throat':      [1,0,1,1,0,0,1,1,0,0],
    'short_breath':     [0,0,0,1,0,1,1,1,1,0],
    'disease': [
        'Flu', 'Dengue', 'Cold', 'COVID-19', 'Healthy',
        'Malaria', 'Food Poisoning', 'COVID-19', 'Dengue', 'viral'
    ]
}

df = pd.DataFrame(data)
X = df.drop('disease', axis=1)
y = df['disease']
model = DecisionTreeClassifier()
model.fit(X, y)


data = {
    'fever':            [1,1,0,1,0,1,0,1,1,1],
    'cough':            [1,0,1,1,0,1,0,1,0,0],
    'headache':         [0,1,0,1,0,1,0,1,1,1],
    'fatigue':          [1,1,0,1,0,1,0,1,1,0],
    'nausea':           [0,1,0,1,0,1,1,0,1,0],
    'vomiting':         [0,1,0,0,0,1,1,0,1,0],
    'body_pain':        [1,1,0,1,0,1,0,1,1,0],
    'sore_throat':      [1,0,1,1,0,0,1,1,0,0],
    'short_breath':     [0,0,0,1,0,1,1,1,1,0],
    'disease': [
        'Flu', 'Dengue', 'Cold', 'COVID-19', 'Healthy',
        'Malaria', 'Food Poisoning', 'COVID-19', 'Dengue', 'viral'
    ]
}


df = pd.DataFrame(data)

X = df.drop('disease', axis=1)
y = df['disease']


model = DecisionTreeClassifier()
model.fit(X, y)


st.header("🦠 Select Your Symptoms")

col1, col2, col3 = st.columns(3)

with col1:
    with st.container():
        st.subheader("🌡️ Fever")
        fever = 1 if st.selectbox("Do you have fever?", ["No", "Yes"], key="fever") == "Yes" else 0
    
    with st.container():
        st.subheader("🤧 Cough")
        cough = 1 if st.selectbox("Do you have cough?", ["No", "Yes"], key="cough") == "Yes" else 0
    
    with st.container():
        st.subheader("🤕 Headache")
        headache = 1 if st.selectbox("Do you have headache?", ["No", "Yes"], key="headache") == "Yes" else 0

with col2:
    with st.container():
        st.subheader("😴 Fatigue")
        fatigue = 1 if st.selectbox("Do you feel fatigued?", ["No", "Yes"], key="fatigue") == "Yes" else 0
    
    with st.container():
        st.subheader("🤢 Nausea")
        nausea = 1 if st.selectbox("Do you feel nauseous?", ["No", "Yes"], key="nausea") == "Yes" else 0
    
    with st.container():
        st.subheader("🤮 Vomiting")
        vomiting = 1 if st.selectbox("Are you vomiting?", ["No", "Yes"], key="vomiting") == "Yes" else 0

with col3:
    with st.container():
        st.subheader("🦴 Body Pain")
        body_pain = 1 if st.selectbox("Do you have body pain?", ["No", "Yes"], key="body_pain") == "Yes" else 0
    
    with st.container():
        st.subheader("👄 Sore Throat")
        sore_throat = 1 if st.selectbox("Do you have sore throat?", ["No", "Yes"], key="sore_throat") == "Yes" else 0
    
    with st.container():
        st.subheader("💨 Shortness of Breath")
        short_breath = 1 if st.selectbox("Do you have shortness of breath?", ["No", "Yes"], key="short_breath") == "Yes" else 0


st.write("---")

if st.button("🔍 Predict Disease", use_container_width=True):
    with st.spinner("🔬 Analyzing your symptoms..."):
        time.sleep(2)
    
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    for i in range(100):
        time.sleep(0.02)
        progress_bar.progress(i + 1)
        if i < 30:
            status_text.text("🧠 Processing symptoms...")
        elif i < 70:
            status_text.text("🤖 Running AI model...")
        else:
            status_text.text("📊 Generating prediction...")
    
    progress_bar.empty()
    status_text.empty()

    sample = [[fever, cough, headache, fatigue, nausea, vomiting,
               body_pain, sore_throat, short_breath]]

    prediction = model.predict(sample)[0]

    st.markdown('<div class="prediction-result">', unsafe_allow_html=True)
    st.success(f"🎯 **Predicted Disease: {prediction}**")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.subheader("💊 Medical Suggestions")
    
    suggestions = {
        "Flu": "Rest, stay hydrated, and take over-the-counter medications like acetaminophen.",
        "Dengue": "Consult a doctor immediately. Monitor platelet count and stay hydrated.",
        "COVID-19": "Isolate yourself, monitor symptoms, and seek medical attention if needed.",
        "Malaria": "Take prescribed antimalarial medication and consult a healthcare professional.",
        "Food Poisoning": "Stay hydrated, eat bland foods, and rest. Seek medical help if severe.",
        "Cold": "Rest, drink fluids, use saline nasal sprays, and take pain relievers if needed.",
        "viral": "Rest, take antiviral medications if prescribed, and maintain good hygiene.",
        "Healthy": "Great! You appear to be healthy. Continue maintaining a healthy lifestyle."
    }
    
    if prediction in suggestions:
        st.info(f"💡 {suggestions[prediction]}")
    else:
        st.info("Please consult a healthcare professional for accurate diagnosis.")

st.markdown('<div class="footer">', unsafe_allow_html=True)
st.write("---")
st.caption("⚠️ **Disclaimer:** This AI system provides predictions based on symptoms but is not a substitute for professional medical advice. Always consult a qualified healthcare provider for proper diagnosis and treatment.")
st.caption("Built with Streamlit & Machine Learning | © 2024")
st.markdown('</div>', unsafe_allow_html=True)