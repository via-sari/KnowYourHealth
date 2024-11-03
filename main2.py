import streamlit as st
from typing import Dict, Generator
import ollama

# Set up the page title, layout, and theme
st.set_page_config(page_title="Know Your Health", layout="centered")

# Add custom CSS for styling
st.markdown("""
    <style>
        /* Global styles */
        body {
            background-color: #f5f5f5;
        }
        h1, h2, h3 {
            color: #4CAF50;
            font-family: Arial, sans-serif;
        }
        .section {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }
        .highlight {
            color: #ff5722;
            font-weight: bold;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border-radius: 8px;
            padding: 10px 20px;
        }
        .stTabs > div {
        background-color: #ededed;
        border-radius: 5px;
        padding: 10px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.3);
        }
        .stTabs > div:hover {
            background-color: #ededed;
        }
    </style>
""", unsafe_allow_html=True)


col1, col2 = st.columns([1, 10]); col1.image("kyh.png", width=70); col2.title("Know Your Health")
st.markdown("<p style='text-align: left; font-style: italic; font-size: 18px; color: #555;'>Track and improve your health with personalized health recommendations.</p>", unsafe_allow_html=True)

# Function to generate response using Ollama
def generate_ollama_response(model_name: str, messages: Dict) -> Generator:
    stream = ollama.chat(model=model_name, messages=messages, stream=True)
    for chunk in stream:
        yield chunk['message']['content']

# Create three tabs
tab1, tab2, tab3 = st.tabs(["Input Your Health", "Talk with me", "About"])


# Tab 1: Input Your Health
with tab1:
    st.header("Input Your Health")

    # Individu Section
    st.subheader("Data Individu")
    age = st.text_input("Usia:", placeholder="e.g., 30")
    gender = st.selectbox("Jenis Kelamin:", ["pria", "wanita"])
    height = st.text_input("Tinggi Badan (cm):", placeholder="e.g., 30")
    weight = st.text_input("Berat Badan (kg):", placeholder="e.g., 30")

    # Activity Section
    st.subheader("Data Riwayat Kesehatan")
    # daily_activity = st.text_input("Describe your daily activity level:", placeholder="e.g., moderate")
    alergy = st.text_input("Reaksi alergi yang pernah anda derita:", placeholder="e.g., debu, makanan laut")
    eye_diseases = st.selectbox("Riwayat penyakit mata yang pernah anda derita?:",
                                 ["Tidak ada","Ambiopia (mata malas)","Apakia","Astigmatisma (silinder)",
                                  "Katarak","Retinopati diabetes melitus","Sindroma mata kering","Glaukoma",
                                  "Hipermetropi (rabun jauh)","Keratitis","Degenerasi makula","Miopia (rabun dekat)",
                                  "Neuritis mata","Kerusakan retina","Trauma di mata","Lainnya"])
    eye_opertion = st.selectbox("Operasi Operasi mata yang pernah anda lakukan:",
                                 ["Tidak pernah","Bleparoplasti","Operasi katarak","Transplantasi kornea",
                                  "Operasi laser retina","LASIK","Operasi otot mata","Punctal plug","RK",
                                  "Operasi starbismus","Operasi glaukoma","Vitrektomi","Lainnya"])
    eye_starting = st.selectbox("Penyakit yang mengawali sakit mata anda sekarang:",
                                 ["Sehat","AIDS","Diabetes melitus","Artitis rheumatoid (rematik)",
                                  "Herpes","HIV","Hipertensi","Hipotiroid","Lupus","Sclerosis multiple",
                                  "Sjorgen Grave","Hipertiroid","Lainnya"])
    sistemic_disesae = st.selectbox("Penyakit Penyakit sistemik (umum) apa yang pernah anda derita:",
                                 ["Tidak ada", "Sakit Jantung", "Anemia", "Artritis", "Asma", "Kanker",
                                    "Hipotiroid", "Hipertiorid", "PPOK", "Diabetes mellitus", "Eksema",
                                    "Fibromalgua", "Vertigo", "Kehilangan pendengaran", "Hipertensi", 
                                    "Kolesterol tinggi", "HIV", "Gagal ginjal", "Batu ginjal", "Liver", 
                                    "Sakit pernafasan", "Lupus", "Migraine", "Polimialgia", "Gangguan psikiatri",
                                    "Gangguan pendarahan", "Stroke", "Asam Urat", "Lainnya"])
    
    operation = st.text_input("Operasi apa yang pernah anda lakukan untuk mengatasi penyakit diatas:", placeholder="e.g., debu, makanan laut")
    infection = st.selectbox("Infeksi apa yang pernah anda derita:",
                            ["Tidak ada", "Hepatitis A/B/C", "Herpes simplek", "Histoplasmosis", "HIV/AIDS", 
                             "Meningitis", "MRSA", "Sipilis", "Toxoplasmosis", "Lainnya"])
    family_disease = st.selectbox("Riwayat penyakit keluarga (orangtua, saudara kandung, anak, anggota keluarga serumah):",
                            ["Tidak ada", "Asma", "Buta", "Kanker", "Katarak", "Diabetes mellitus", "Glaukoma",
                              "Sakit jantung", "Hipertensi", "Sakit ginjal", "Ambliopia (mata malas)", 
                              "Degenerasi makula", "Penyakit retina", "Stroke", "Autoimun", "Leukimia", "Lainnya"])


    # Goals Section
    st.subheader("Data Pola Hidup dan Lingkungan")
    # health_concern = st.text_input("Enter your primary health concern:", placeholder="e.g., hypertension")
    salty_food_freq = st.selectbox("Seberapa sering anda mengonsumsi makanan asin, pedas, dan sejenisnya?",
                            ["Setiap hari", "Sering (3-5 kali seminggu)", "Jarang (kurang dari 2 kali seminggu)",
                              "Sangat jarang (minimal sebulan 1 kali)", "Tidak pernah"])
    sweet_food_freq = st.selectbox("Seberapa sering anda mengonsumsi makanan manis?",
                            ["Setiap hari", "Sering (3-5 kali seminggu)", "Jarang (kurang dari 2 kali seminggu)",
                              "Sangat jarang (minimal sebulan 1 kali)", "Tidak pernah"])
    coffee_freq = st.selectbox("Seberapa sering anda meminum kopi?",
                            ["Setiap hari", "Sering (3-5 kali seminggu)", "Jarang (kurang dari 2 kali seminggu)",
                              "Sangat jarang (minimal sebulan 1 kali)", "Tidak pernah"])
    alcohol_freq = st.selectbox("Seberapa sering anda meminum alkohol?",
                            ["Setiap hari", "Sering (3-5 kali seminggu)", "Jarang (kurang dari 2 kali seminggu)",
                              "Sangat jarang (minimal sebulan 1 kali)", "Tidak pernah"])
    cigarette_freq = st.selectbox("Seberapa sering anda merokok?",
                            ["Setiap hari", "Sering (3-5 kali seminggu)", "Jarang (kurang dari 2 kali seminggu)",
                              "Sangat jarang (minimal sebulan 1 kali)", "Tidak pernah"])
    sleep_disorders_freq = st.selectbox("Dalam dua minggu terakhir, seberapa sering Anda merasa kesulitan untuk tidur atau tidur terlalu banyak?",
                            ["Setiap hari", "Sering (3-5 kali seminggu)", "Jarang (kurang dari 2 kali seminggu)",
                              "Sangat jarang (minimal sebulan 1 kali)", "Tidak pernah"])
    mood_disorders_freq = st.selectbox("Dalam dua minggu terakhir, seberapa sering Anda merasa tidak memiliki minat atau kesenangan dalam melakukan aktivitas?",
                            ["Setiap hari", "Sering (3-5 kali seminggu)", "Jarang (kurang dari 2 kali seminggu)",
                              "Sangat jarang (minimal sebulan 1 kali)", "Tidak pernah"])
    mentality_disorders = st.selectbox("Apakah Anda pernah didiagnosis dengan gangguan kesehatan mental?",
                            ["Depresi", "Kecemasan (Anxiety Disorder)", "Gangguan Bipolar", "Skizofrenia", 
                             "Gangguan Stres Pasca Trauma (PTSD)", "Gangguan Obsesif-Kompulsif (OCD)", 
                             "Gangguan Makan (misalnya Anoreksia, Bulimia)", 
                             "Gangguan Kepribadian (misalnya Gangguan Kepribadian Antisosial, Gangguan Kepribadian Borderline)",
                             "Gangguan Perilaku atau Emosi", "Lainnya" "Tidak pernah"])
    tension_freq = st.selectbox("Seberapa sering anda merasakan tekanan dalam pekerjaan atau aktivitas anda?",
                            ["Setiap hari", "Sering (3-5 kali seminggu)", "Jarang (kurang dari 2 kali seminggu)",
                              "Sangat jarang (minimal sebulan 1 kali)", "Tidak pernah"])
    sport_freq = st.selectbox("Seberapa sering anda melakukan aktivitas fisik atau olahraga?",
                            ["Setiap hari", "Sering (3-5 kali seminggu)", "Jarang (kurang dari 2 kali seminggu)",
                              "Sangat jarang (minimal sebulan 1 kali)", "Tidak pernah"])
    
    # Goals Section
    st.subheader("Data Pemeriksaan Kesehatan Rutinan (Opsional)")
    blood_tension = st.text_input("Tekanan Darah: Sistolik / Diastolik (mmHg)", placeholder="e.g., 120/90")
    glucose = st.text_input("Glukosa Darah: (mg/dL atau mmol/L)", placeholder="e.g., 100")
    cholesterol = st.text_input("Kolesterol: Total kolesterol, HDL, LDL (mg/dL atau mmol/L)", placeholder="e.g., 60")

    # Goals Section
    st.subheader("Data Pemeriksaan Mobile JKN")
    jkn_skrinning = st.text_input("Skrinning Riwayat Kesehatan Mobile JKN", placeholder="e.g., risiko rendah diabetes, risiko rendah hipertensi, risiko rendah jantung, risiko rendah ginjal.")

    # Generate text based on input using Ollama with "llama3.2:latest"
    if st.button("Generate Health Insights"):
        if age and gender and height and weight:
            # Define a custom prompt based on inputs
            health_prompt = (f"personal info: {age}, {gender}, {height}, {weight}"
                             f"riwayat penyakit: alergi {alergy}, riwayat penyakit mata {eye_diseases}, operasi mata {eye_opertion}, penyakit sistemik {sistemic_disesae},operasi penyakit sistemik {operation}, riwayat infeksi {infection}, riwayat penyakit keluarga {family_disease}"
                             f"pola hidup: {salty_food_freq} makan makanan asin dan pedas, {sweet_food_freq} makan makanan manis, {coffee_freq} meminum kopi, {alcohol_freq} meminum alkohol, {cigarette_freq} merokok, {sleep_disorders_freq} mengalami sulit tidur, {mood_disorders_freq} merasa kehilangan minat aktivitas, riwayat diagnosis mental {mentality_disorders}, {tension_freq} merasakan tekanan dalam pekerjaan/aktivitas, {sport_freq} olahraga rutin"
                             f"hasil skrinning mobile JKN: {jkn_skrinning}"
                             f"buatkan rekomendasi kesehatan personal: 1. rekomendasi gaya hidup 2. rekomendasi pola makan dan pantangan makanan 3. rekomendasi tindakan preventif dan jadwal pemeriksaan rutin 4.rekomendasi pengelolaan stres 5. rekomendasi olahraga rutin spesifik")
            
            # Call Ollama API with the generated prompt
            messages = [{"role": "user", "content": health_prompt}]
            response = ''.join(generate_ollama_response("llama3.2:latest", messages))
            
            st.write("Rekomendasi Kesehatan Personal:")
            st.write(response)
        else:
            st.warning("Please fill in all fields to generate insights.")


with tab2:
    st.header("Chat with Me")

    # Inform the user about the bot's role
    st.write("Hello! I'm your personal health advisor. How can I assist you with your health concerns?")

    # Setting up chat history
    if "selected_model" not in st.session_state:
        st.session_state.selected_model = "llama3.2:latest"  # Default model
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Displaying chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # User input and response in chat
    if prompt := st.chat_input("How could I help you?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            response = st.write_stream(generate_ollama_response(
                st.session_state.selected_model, st.session_state.messages
            ))
            st.session_state.messages.append({"role": "assistant", "content": response})


# Tab 3: About
with tab3:
    st.header("About")
    # st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.write("""
    **Know Your Health** is a personal health advisory tool designed to help users better understand and manage their health. 
    This app provides customized health insights based on individual data inputs, including age, weight, height, and health history. 
    In addition to generating health advice, users can engage in interactive chat with the AI health advisor, who offers insights 
    on lifestyle choices, potential health risks, and wellness recommendations.

    **Features:**
    - **Health Data Input:** Users can enter various health-related information, such as allergies, eye health history, and lifestyle habits.
    - **Health Insights:** By analyzing the data provided, the app delivers tailored health insights to guide users in making informed health choices.
    - **Interactive Chat:** Users can ask the AI advisor health-related questions and receive responses in real time.

    **Disclaimer:** This tool is intended for general health advice only. It should not replace professional medical advice, diagnosis, or treatment. 
    Always consult a healthcare provider for serious health concerns.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

    # Footer section
    st.markdown("""
        <div style="text-align: center; margin-top: 20px; font-size: small;">
            <p>Know Your Health © 2024 | <a href="https://yourwebsite.com" style="color: #4CAF50;">Learn More</a></p>
        </div>
    """, unsafe_allow_html=True)
