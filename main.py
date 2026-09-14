import streamlit as st
from PIL import Image
import pypdf
from google import genai

st.set_page_config(page_title="BATMAN PHYSICS MASTER", layout="wide")

# ----------------------------------------------------
# 1. GEMINI API SETUP (SECURE & HIDDEN)
# ----------------------------------------------------
# secrets.toml එකෙන් API Key එක රහසිගතව ලබාගැනීම
API_KEY = st.secrets.get("GEMINI_API_KEY", "")

if not API_KEY:
    st.error("⚠️ Gemini API Key එක හමු නොවීය! කරුණාකර `.streamlit/secrets.toml` එකට API Key එක ඇතුළත් කරන්න.")
    st.stop()

# Gemini Client එක සාදාගැනීම
client = genai.Client(api_key=API_KEY)

# ----------------------------------------------------
# 2. HELPER FUNCTIONS FOR FILE PROCESSING
# ----------------------------------------------------
def extract_text_from_pdf(pdf_file):
    """PDF එකෙන් Text කියවාගැනීම"""
    pdf_reader = pypdf.PdfReader(pdf_file)
    extracted_text = ""
    for page in pdf_reader.pages:
        extracted_text += page.extract_text() or ""
    return extracted_text

def ask_gemini(prompt_text, image_obj=None, lang="sin"):
    """Gemini 3.6 Flash Model එක භාවිතයෙන් ප්‍රශ්න විසඳීම"""
    try:
        lang_instruction = "Respond in Sinhala language clearly." if lang == "sin" else "Respond in English language clearly."
        
        system_instruction = f"""
        You are an expert Sri Lankan G.C.E. A/L Physics Master Tutor created for Janidu Kaveesha's app.
        Solve the Physics problem step-by-step with accurate equations and clear logic.
        {lang_instruction}
        """

        contents = []
        if image_obj:
            contents.append(image_obj)
        
        contents.append(f"{system_instruction}\n\nQuestion / Text Content:\n{prompt_text}")

        # Gemini Flash Model එක භාවිත කිරීම
        response = client.models.generate_content(
            model='gemini-3.6-flash',
            contents=contents
        )
        return response.text
    except Exception as e:
        return f"❌ Error: {str(e)}"

# ----------------------------------------------------
# 3. STREAMLIT USER INTERFACE (UI)
# ----------------------------------------------------
st.title("⚡ BATMAN PHYSICS MASTER - AI TUTOR")
st.caption("Developed by Janidu Kaveesha | Powered by Gemini Flash AI")

st.markdown("---")

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("⚙️ Settings & Inputs")
    
    # Language Selection
    lang_choice = st.radio("🌐 භාෂාව (Language):", ["සිංහල", "English"])
    lang_code = "sin" if lang_choice == "සිංහල" else "eng"

    st.markdown("---")
    
    # Input Type Selector
    input_type = st.radio("📥 ප්‍රශ්නය ලබාදෙන ආකාරය තෝරන්න:", ["Text (ලියන ලද ප්‍රශ්න)", "Image (ඡායාරූප)", "PDF File"])
    
    user_text = ""
    uploaded_image = None
    
    if input_type == "Text (ලියන ලද ප්‍රශ්න)":
        user_text = st.text_area("✍️ Physics ප්‍රශ්නය මෙතන Type කරන්න:", height=150)
        
    elif input_type == "Image (ඡායාරූප)":
        img_file = st.file_uploader("📸 ප්‍රශ්නය සහිත රූපය (JPG, PNG) Upload කරන්න:", type=["jpg", "jpeg", "png"])
        if img_file:
            uploaded_image = Image.open(img_file)
            st.image(uploaded_image, caption="Uploaded Question Image", use_container_width=True)
        user_text = st.text_input("📝 අමතර විස්තරයක් ඇත්නම් (Optional):", "")

    elif input_type == "PDF File":
        pdf_file = st.file_uploader("📄 Physics PDF එක Upload කරන්න:", type=["pdf"])
        if pdf_file:
            with st.spinner("PDF එක කියවමින් පවතී..."):
                user_text = extract_text_from_pdf(pdf_file)
                st.success("PDF එක සාර්ථකව කියවන ලදී!")

    solve_btn = st.button("⚡ Solve Question with AI", use_container_width=True, type="primary")

with col2:
    st.subheader("🤖 AI Step-by-Step Solution")
    
    if solve_btn:
        if not user_text and not uploaded_image:
            st.warning("කරුණාකර ප්‍රශ්නයක්, Image එකක් හෝ PDF එකක් ඇතුළත් කරන්න!")
        else:
            with st.spinner("Gemini Flash AI එකෙන් ගණන විසඳමින් පවතී... ⚡"):
                solution = ask_gemini(user_text, image_obj=uploaded_image, lang=lang_code)
                st.markdown(solution)