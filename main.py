import streamlit as st
import sympy as sp
import re
import random

# ---------------------------------------------------------
# 1. PAGE CONFIG & DYNAMIC BATMAN THEME (CSS)
# ---------------------------------------------------------
st.set_page_config(
    page_title="Batman Physics Engine",
    page_icon="🦇",
    layout="wide"
)

# Sidebar Control
st.sidebar.title("⚙️ ENGINE CONTROLS")
language = st.sidebar.radio("🌐 Language / භාෂාව", ["SI", "EN"], format_func=lambda x: "සිංහල" if x == "SI" else "English")
bat_mode = st.sidebar.toggle("🦇 Batman Personality Mode (Bat-Mode)", value=True)

# High Quality Dark Knight Wallpaper Direct Link
BATMAN_BG_URL = "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?q=80&w=1920&auto=format&fit=crop"

if bat_mode:
    st.markdown(f"""
        <style>
        .stApp {{
            background: linear-gradient(rgba(11, 12, 16, 0.85), rgba(11, 12, 16, 0.85)),
                        url('{BATMAN_BG_URL}') !important;
            background-size: cover !important;
            background-position: center !important;
            background-attachment: fixed !important;
        }}
        
        /* Streamlit Content Container Opacity Fix */
        [data-testid="stHeader"], [data-testid="stAppViewContainer"] {{
            background: transparent !important;
        }}
        </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
        .stApp {
            background-color: #0b0c10 !important;
        }
        </style>
    """, unsafe_allow_html=True)

# Main Dark Knight Styling
st.markdown("""
    <style>
    h1, h2, h3 {
        color: #ffcc00 !important;
        text-shadow: 0px 0px 8px rgba(255, 204, 0, 0.4);
    }
    
    .stTextInput > div > div > input, .stTextArea > div > div > textarea {
        background-color: rgba(31, 40, 51, 0.9) !important;
        color: #ffcc00 !important;
        border: 1px solid #ffcc00 !important;
        border-radius: 8px;
    }

    .stButton > button {
        background-color: #ffcc00 !important;
        color: #000000 !important;
        font-weight: bold !important;
        border-radius: 8px !important;
        border: none !important;
        transition: 0.3s;
    }
    
    .stButton > button:hover {
        background-color: #e6b800 !important;
        box-shadow: 0px 0px 12px #ffcc00;
    }

    section[data-testid="stSidebar"] {
        background-color: rgba(18, 18, 18, 0.95) !important;
        border-right: 1px solid #333;
    }
    
    .bat-card {
        background-color: rgba(22, 27, 34, 0.88);
        border: 1px solid #ffcc00;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.7);
        margin-bottom: 15px;
        backdrop-filter: blur(5px);
    }
    
    .bat-alert {
        background-color: rgba(42, 0, 0, 0.85);
        border: 2px solid #ff0000;
        color: #ff4d4d;
        padding: 10px;
        border-radius: 8px;
        font-weight: bold;
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. DICTIONARY & BILINGUAL / BAT-MODE DIALOGUES
# ---------------------------------------------------------
BAT_QUOTES = [
    "🦇 *\"Alfred, cancel my 8 PM meeting with the Joker. I need to solve this Physics problem first.\"*",
    "🦇 *\"Joker thought he could escape using gravity. He forgot $g = 9.8\\text{ ms}^{-2}$!\"*",
    "🦇 *\"I am Vengeance. I am the Night. I am... a Physics Tutor!\"*",
    "🦇 *\"Robin! Bring the Bat-Calculator! Math is out of control in Gotham!\"*",
    "🦇 *\"In Gotham's dark alleys, even criminals obey Newton's 3rd Law.\"*",
    "🦇 *\"Superman flies using powers. I fly using aerodynamics and pure Physics. We are not the same.\"*"
]

LANG_DATA = {
    "SI": {
        "title": "🦇 BATMAN PHYSICS MASTER (A/L ENGINE)",
        "solver_tab": "⚡ AI Logic Solver (ගණන් සූත්‍ර)",
        "vault_tab": "📖 A/L Theory Vault (සිලබස් එක)",
        "input_label": "ගණන හෝ දත්ත ඇතුළත් කරන්න (Eg: u=0, a=2, t=5):",
        "solve_btn": "ගණනය කරන්න (Solve)",
        "result_header": "🔍 විසඳුම (Step-by-Step Analysis):",
        "normal_prefix": "💡 **භෞතික විද්‍යාත්මක විසඳුම:**\n",
        "bat_prefix": "🦇 **BAT-COMPUTER ANALYSIS:**\n*Gotham නොසැලේ, භෞතික විද්‍යාත්මක නියමයන් කිසිදා පරාජය කළ නොහැක!*\n\n"
    },
    "EN": {
        "title": "🦇 BATMAN PHYSICS MASTER (A/L ENGINE)",
        "solver_tab": "⚡ AI Logic Solver",
        "vault_tab": "📖 A/L Theory Vault",
        "input_label": "Enter Physics Query or Variables (e.g. u=0, a=2, t=5):",
        "solve_btn": "Solve Physics Query",
        "result_header": "🔍 Step-by-Step Solution:",
        "normal_prefix": "💡 **Standard Solution:**\n",
        "bat_prefix": "🦇 **BAT-COMPUTER ANALYSIS:**\n*Justice is non-negotiable, and so are the laws of Physics in Gotham!*\n\n"
    }
}

SYLLABUS = {
    "1. Measurement & Units / මිනුම් හා ඒකක": """
    • **SI Base Units:** Mass (kg), Length (m), Time (s), Current (A), Temp (K), Amount (mol), Luminous Intensity (cd)
    • **Dimensions:** [Velocity] = LT⁻¹, [Acceleration] = LT⁻², [Force] = MLT⁻², [Work/Energy] = ML²T⁻²
    • **Errors:** Fractional Error = Δx / x , Percentage Error = (Δx / x) × 100%
    """,
    "2. Mechanics / යාන්ත්‍රික විද්‍යාව": """
    • **Motion Equations:** 
      - v = u + at
      - s = ut + ½at²
      - v² = u² + 2as
      - s = ((u + v) / 2) * t
    • **Newton's Laws:** F = ma,  p = mv (Momentum)
    • **Work, Energy & Power:** Work W = F s cosθ, Ek = ½mv², Ep = mgh, Power P = W/t = Fv
    """,
    "3. Oscillations & Waves / තරංග හා දෝලන": """
    • **Simple Harmonic Motion (SHM):** Acceleration a = -ω²x, Period T = 2π/ω
    • **Wave Velocity:** v = f λ
    • **Doppler Effect:** Observed Frequency f' = f ((v ± v_observer) / (v ∓ v_source))
    """,
    "4. Thermal Physics / තාප භෞතික විද්‍යාව": """
    • **Heat Capacity:** Q = mcΔθ , Q = mL (Latent Heat)
    • **Thermal Conduction:** Rate of heat flow dQ/dt = kA(T₁ - T₂)/d
    • **Ideal Gas Law:** PV = nRT , PV = N k_B T
    """,
    "5. Gravitational Fields / ගුරුත්වාකර්ෂණ ක්ෂේත්‍ර": """
    • **Universal Gravitation:** F = G (m₁ m₂) / r²
    • **Field Intensity:** g = GM / R²
    • **Escape Velocity:** v_e = √(2gR) = √(2GM/R)
    """,
    "6. Electrostatic Fields / ස්ථිති විද්‍යුත් ක්ෂේත්‍ර": """
    • **Coulomb's Law:** F = (1 / 4πε₀) * (q₁ q₂) / r²
    • **Electric Field (E):** E = F / q = V / d
    • **Capacitance:** C = Q / V, Energy Stored U = ½ C V²
    """,
    "7. Magnetic Fields / චුම්බක ක්ෂේත්‍ර": """
    • **Force on Current Carrying Wire:** F = B I L sinθ
    • **Force on Moving Charge:** F = q v B sinθ
    • **Faraday's Law of Induction:** e.m.f (ε) = -N (dΦ / dt)
    """,
    "8. Current Electricity / ධාරා විද්‍යුතය": """
    • **Ohm's Law:** V = I R , Resistance R = ρ L / A
    • **Kirchhoff's Laws:** 
      - Current Law (Junction): ΣI_in = ΣI_out
      - Voltage Law (Loop): ΣE = Σ(I R)
    • **Electrical Power:** P = VI = I²R = V²/R
    """,
    "9. Electronics / ඉලෙක්ට්‍රොනික විද්‍යාව": """
    • **BJT Transistor:** I_E = I_B + I_C , Current Gain β = I_C / I_B
    • **Operational Amplifiers (Op-Amp):** 
      - Inverting Gain = - R_f / R_in
      - Non-Inverting Gain = 1 + (R_f / R_in)
    """,
    "10. Properties of Matter / පදාර්ථයේ යාන්ත්‍රික ගුණ": """
    • **Hooke's Law & Elasticity:** Stress = F/A, Strain = ΔL/L₀, Young's Modulus E = Stress / Strain
    • **Surface Tension:** T = F / L , Excess pressure inside bubble P = 4T / r
    • **Viscosity (Stokes' Law):** Drag Force F = 6πηrv
    """,
    "11. Radiation & Modern Physics / විකිරණය හා නූතන භෞතික විද්‍යාව": """
    • **Photoelectric Effect:** Energy E = hf = h c / λ, Einstein's Eq: hf = Φ + ½ m v_max²
    • **Mass-Energy Equivalence:** E = Δm c²
    """
}

def play_sound(sound_url):
    sound_html = f"""
        <audio autoplay style="display:none;">
            <source src="{sound_url}" type="audio/mp3">
        </audio>
    """
    st.markdown(sound_html, unsafe_allow_html=True)

# ---------------------------------------------------------
# 3. ADVANCED SYMPY & TEXT SOLVER ENGINE
# ---------------------------------------------------------
def solve_physics(query_text, is_bat_mode, lang):
    q = query_text.lower()
    
    u_m = re.search(r'u\s*[:=]\s*(-?\d+(\.\d+)?)', q)
    v_m = re.search(r'v\s*[:=]\s*(-?\d+(\.\d+)?)', q)
    a_m = re.search(r'a\s*[:=]\s*(-?\d+(\.\d+)?)', q)
    t_m = re.search(r't\s*[:=]\s*(-?\d+(\.\d+)?)', q)
    s_m = re.search(r's\s*[:=]\s*(-?\d+(\.\d+)?)', q)
    
    if u_m:
        u = float(u_m.group(1))
    elif "නිශ්චලතාව" in q or "rest" in q:
        u = 0.0
    else:
        u = None
        
    v = float(v_m.group(1)) if v_m else None
    
    if a_m:
        a = float(a_m.group(1))
    else:
        a_match = re.search(r'(\d+(\.\d+)?)\s*(\\text\{\s*ms\s*\}\^\{-2\}|ms\^-2|ms2)', q)
        a = float(a_match.group(1)) if a_match else None

    if t_m:
        t = float(t_m.group(1))
    else:
        t_match = re.search(r'(\d+(\.\d+)?)\s*(\\text\{\s*s\s*\}|s|තප්පර)', q)
        t = float(t_match.group(1)) if t_match else None

    s = float(s_m.group(1)) if s_m else None

    u_sym, v_sym, a_sym, t_sym, s_sym = sp.symbols('u v a t s')
    output = ""
    calculated = False

    if u is not None and a is not None and t is not None and v is None:
        eq1 = sp.Eq(v_sym, u_sym + a_sym * t_sym)
        eq2 = sp.Eq(s_sym, u_sym * t_sym + sp.Rational(1, 2) * a_sym * (t_sym**2))
        
        v_ans = float(sp.solve(eq1.subs({u_sym: u, a_sym: a, t_sym: t}), v_sym)[0])
        s_ans = float(sp.solve(eq2.subs({u_sym: u, a_sym: a, t_sym: t}), s_sym)[0])
        
        output += f"📌 **[ලබාගත් දත්ත / Extracted Data]:** $u = {u}\\text{{ ms}}^{{-1}}$, $a = {a}\\text{{ ms}}^{{-2}}$, $t = {t}\\text{{ s}}$\n\n"
        output += f"**[1. අවසාන ප්‍රවේගය (v)]:** $v = u + at$\n"
        output += f"$$\implies v = {u} + ({a} \\times {t}) = {v_ans}\\text{{ ms}}^{{-1}}$$\n\n"
        output += f"**[2. ගමන් කළ මුළු දුර (s)]:** $s = ut + \\frac{{1}}{{2}}at^2$\n"
        output += f"$$\implies s = ({u} \\times {t}) + \\frac{{1}}{{2}}({a})({t}^2) = {s_ans}\\text{{ m}}$$\n"
        calculated = True

    elif u is not None and v is not None and a is not None and t is None:
        eq1 = sp.Eq(v_sym, u_sym + a_sym * t_sym)
        eq2 = sp.Eq(v_sym**2, u_sym**2 + 2 * a_sym * s_sym)
        
        t_ans = float(sp.solve(eq1.subs({u_sym: u, v_sym: v, a_sym: a}), t_sym)[0])
        s_ans = float(sp.solve(eq2.subs({u_sym: u, v_sym: v, a_sym: a}), s_sym)[0])
        
        output += f"📌 **[ලබාගත් දත්ත / Extracted Data]:** $u = {u}\\text{{ ms}}^{{-1}}$, $v = {v}\\text{{ ms}}^{{-1}}$, $a = {a}\\text{{ ms}}^{{-2}}$\n\n"
        output += f"**[1. ගතවූ කාලය (t)]:** $v = u + at \implies t = \\frac{{v - u}}{{a}}$\n"
        output += f"$$\implies t = \\frac{{{v} - {u}}}{{{a}}} = {t_ans}\\text{{ s}}$$\n\n"
        output += f"**[2. ගමන් කළ මුළු දුර (s)]:** $v^2 = u^2 + 2as \implies s = \\frac{{v^2 - u^2}}{{2a}}$\n"
        output += f"$$\implies s = \\frac{{{v}^2 - {u}^2}}{{2({a})}} = {s_ans}\\text{{ m}}$$\n"
        calculated = True

    if not calculated:
        output += "### 📖 Relevant Formulas & Concepts Found:\n"
        if any(k in q for k in ["balaya", "force", "බලය", "f="]):
            output += "- **Newton's 2nd Law:** $F = ma$\n- **Linear Momentum:** $p = mv$\n"
        if any(k in q for k in ["current", "v=ir", "ධාරාව", "ප්‍රතිරෝධය", "ohm"]):
            output += "- **Ohm's Law:** $V = IR$\n- **Electrical Power:** $P = VI = I^2R = \\frac{V^2}{R}$\n"
        if any(k in q for k in ["heat", "q=", "තාපය", "temp"]):
            output += "- **Heat Energy:** $Q = mc\\Delta\\theta$\n- **Latent Heat:** $Q = mL$\n"
        if any(k in q for k in ["wave", "v=f", "තරංග", "frequency"]):
            output += "- **Wave Equation:** $v = f\\lambda$\n- **Time Period:** $T = \\frac{1}{f}$\n"
        if any(k in q for k in ["capacitance", "ධාරිතාව", "c="]):
            output += "- **Capacitor Charge:** $Q = CV$\n- **Stored Energy:** $U = \\frac{1}{2}CV^2$\n"
            
        if output == "### 📖 Relevant Formulas & Concepts Found:\n":
            output = "⚠️ *නොදන්නා Variable රටාවක්. කරුණාකර (u=0, a=4, t=8) වැනි ආකාරයකට Variables ඇතුළත් කරන්න.*"

    prefix = LANG_DATA[lang]["bat_prefix"] if is_bat_mode else LANG_DATA[lang]["normal_prefix"]
    
    if is_bat_mode:
        random_quote = random.choice(BAT_QUOTES)
        output += f"\n\n---\n{random_quote}"
        
    return prefix + output

# ---------------------------------------------------------
# 4. STREAMLIT UI LAYOUT
# ---------------------------------------------------------

if bat_mode:
    st.sidebar.markdown("""
        <div class="bat-alert">
            🚨 BAT-SIGNAL ACTIVATED!<br>
            Gotham Visual Theme & Audio Engine Online.
        </div>
    """, unsafe_allow_html=True)

st.title(LANG_DATA[language]["title"])

tab1, tab2 = st.tabs([LANG_DATA[language]["solver_tab"], LANG_DATA[language]["vault_tab"]])

with tab1:
    st.markdown('<div class="bat-card">', unsafe_allow_html=True)
    user_query = st.text_area(LANG_DATA[language]["input_label"], value="u=0, a=4, t=8", height=100)
    
    if st.button(LANG_DATA[language]["solve_btn"]):
        if user_query.strip():
            with st.spinner("Bat-Computer Analyzing Equations..."):
                solution = solve_physics(user_query, bat_mode, language)
                st.markdown("---")
                
                if bat_mode:
                    st.warning("🦇 BAT-SIGNAL DETECTED: Physics laws successfully applied!")
                    play_sound("https://assets.mixkit.co/active_storage/sfx/2869/2869-preview.mp3")
                
                st.subheader(LANG_DATA[language]["result_header"])
                st.markdown(solution)
        else:
            st.warning("කරුණාකර දත්ත ඇතුළත් කරන්න.")
    st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    st.subheader("📚 Full A/L Physics Syllabus Database")
    selected_unit = st.selectbox("පාඩම තෝරන්න (Select Unit):", list(SYLLABUS.keys()))
    
    st.markdown('<div class="bat-card">', unsafe_allow_html=True)
    st.markdown(f"### {selected_unit}")
    st.markdown(SYLLABUS[selected_unit])
    st.markdown('</div>', unsafe_allow_html=True)