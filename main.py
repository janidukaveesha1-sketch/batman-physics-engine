import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="BATMAN PHYSICS MASTER", layout="wide")

html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>BATMAN PHYSICS MASTER - JANIDU KAVEESHA</title>
  <style>
    :root {
      --gold-primary: #ffd700;
      --gold-secondary: #d4af37;
      --danger-red: #ff0033;
      --neon-cyan: #00f3ff;
      --bg-dark: #0a0a0c;
    }

    body, html {
      margin: 0; padding: 0;
      width: 100%; height: 100%;
      font-family: 'Segoe UI', Arial, sans-serif;
      background-color: var(--bg-dark);
      color: #fff; overflow: hidden;
    }

    /* START LANDING SCREEN */
    #start-screen {
      position: fixed; top: 0; left: 0;
      width: 100vw; height: 100vh;
      background: #000; display: flex;
      justify-content: center; align-items: center;
      z-index: 9999;
    }

    .power-btn {
      width: 130px; height: 130px;
      border-radius: 50%;
      background: radial-gradient(circle, #ff0033 0%, #300 70%, #000 100%);
      border: 4px solid var(--danger-red);
      color: #fff; font-size: 2.2rem; font-weight: bold;
      cursor: pointer;
      box-shadow: 0 0 35px var(--danger-red);
      transition: transform 0.2s, box-shadow 0.2s;
    }

    .power-btn:hover {
      transform: scale(1.1);
      box-shadow: 0 0 55px var(--neon-cyan);
      border-color: var(--neon-cyan);
    }

    /* LOADING SCREEN */
    #loading-screen {
      position: fixed; top: 0; left: 0;
      width: 100vw; height: 100vh;
      background: rgba(5, 5, 8, 0.95);
      display: none; flex-direction: column;
      justify-content: center; align-items: center;
      z-index: 9998;
    }

    .server-blur-bg {
      position: absolute; width: 100%; height: 100%;
      background: radial-gradient(circle, #00f3ff22 0%, #ff003311 50%, #000 100%);
      filter: blur(25px); z-index: -1;
      animation: pulseBg 2s infinite alternate;
    }

    @keyframes pulseBg { 0% { opacity: 0.3; } 100% { opacity: 0.8; } }

    .fan-container {
      width: 120px; height: 120px; border: 6px solid #222; border-radius: 50%;
      position: relative; display: flex; justify-content: center; align-items: center;
      box-shadow: 0 0 25px var(--neon-cyan);
    }

    .fan-blades {
      width: 100%; height: 100%; position: absolute; border-radius: 50%;
      background: conic-gradient(from 0deg, var(--neon-cyan) 0deg 45deg, transparent 45deg 90deg, var(--neon-cyan) 90deg 135deg, transparent 135deg 180deg, var(--neon-cyan) 180deg 225deg, transparent 225deg 270deg, var(--neon-cyan) 270deg 315deg, transparent 315deg 360deg);
      animation: spinFan 0.15s linear infinite;
    }

    @keyframes spinFan { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }

    .piston-block {
      display: none; width: 220px; height: 140px; position: relative;
      border: 2px solid var(--danger-red); background: rgba(20, 0, 0, 0.85);
      border-radius: 8px; box-shadow: 0 0 30px var(--danger-red); padding: 10px;
    }

    .piston-chamber { display: flex; justify-content: space-around; align-items: flex-end; height: 100%; }

    .piston {
      width: 35px; height: 60px; background: linear-gradient(180deg, #fff, #888, #333);
      border-radius: 4px 4px 0 0; animation: pistonMove 0.2s infinite alternate ease-in-out;
    }
    .piston:nth-child(2) { animation-delay: 0.1s; }
    .piston:nth-child(3) { animation-delay: 0.05s; }

    @keyframes pistonMove {
      0% { transform: translateY(0px); } 100% { transform: translateY(-45px); }
    }

    /* BACKGROUND VIDEO */
    #bg-video {
      position: fixed; right: 0; bottom: 0;
      min-width: 100%; min-height: 100%; z-index: -2;
      object-fit: cover;
    }

    /* MAIN APP WORKSPACE */
    .app-container { display: flex; height: 100vh; background: rgba(0, 0, 0, 0.78); }

    .sidebar {
      width: 310px; background: rgba(10, 10, 15, 0.95);
      padding: 18px; border-right: 2px solid #222;
      display: flex; flex-direction: column; gap: 12px;
      overflow-y: auto;
    }

    .sidebar h2 { color: var(--gold-primary); margin: 0; font-size: 1.2rem; }

    .unit-select {
      width: 100%; background: #111; color: var(--gold-primary);
      border: 1px solid var(--gold-secondary); padding: 8px;
      border-radius: 4px; font-weight: bold; cursor: pointer;
    }

    .content-area {
      flex: 1; padding: 20px; display: flex; gap: 15px;
      overflow-y: auto; height: calc(100vh - 90px);
    }

    .card {
      background: rgba(15, 15, 22, 0.88);
      border: 1px solid #333; border-radius: 8px;
      padding: 18px; box-shadow: 0 0 15px rgba(0,0,0,0.5);
    }

    .theory-section { flex: 1.8; display: flex; flex-direction: column; gap: 12px; }
    .qa-notes-section { flex: 1.2; display: flex; flex-direction: column; gap: 12px; }

    .btn-action {
      background: linear-gradient(45deg, var(--gold-secondary), var(--gold-primary));
      color: #000; font-weight: bold; border: none;
      padding: 8px 12px; border-radius: 4px; cursor: pointer;
    }

    input, textarea {
      width: 95%; background: rgba(0, 0, 0, 0.6);
      border: 1px solid var(--neon-cyan); color: #fff;
      padding: 8px; border-radius: 4px; font-family: inherit;
    }

    /* FOOTER */
    .footer-left { position: fixed; bottom: 12px; left: 15px; z-index: 100; }
    .exit-btn {
      background: linear-gradient(45deg, #400, var(--danger-red));
      color: #fff; border: 1px solid var(--danger-red);
      padding: 8px 15px; font-weight: bold; cursor: pointer; border-radius: 4px;
    }

    .footer-right { position: fixed; bottom: 12px; right: 15px; text-align: right; z-index: 100; }
    .lv-monogram { color: var(--gold-secondary); font-weight: bold; line-height: 1.1; font-size: 0.85rem; }
    .gemini-power { color: var(--neon-cyan); font-size: 0.7rem; font-weight: bold; }

    #shatter-overlay {
      position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
      background: #000; display: none; justify-content: center; align-items: center;
      z-index: 10000;
    }
  </style>
</head>
<body>

  <!-- Relative Path Video for GitHub -->
  <video id="bg-video" autoplay muted loop src="assets/dark-batman-shadow-portrait-live-wallpaper.mp4"></video>

  <!-- Start Screen -->
  <div id="start-screen">
    <button class="power-btn" onclick="initializeEngine()">START</button>
  </div>

  <!-- Loading Screen -->
  <div id="loading-screen">
    <div class="server-blur-bg"></div>
    <div id="fan-anim" class="fan-container"><div class="fan-blades"></div></div>
    <div id="piston-anim" class="piston-block">
      <div class="piston-chamber"><div class="piston"></div><div class="piston"></div><div class="piston"></div></div>
    </div>
    <p style="margin-top:20px; font-weight:bold; color:var(--neon-cyan);">INITIALIZING SYLLABUS ENGINE...</p>
  </div>

  <!-- App Workspace -->
  <div class="app-container">
    <div class="sidebar">
      <h2>📚 A/L PHYSICS UNITS</h2>
      <p style="color:#aaa; font-size:0.8rem; margin-top:-5px;">තෝරන පාඩමේ Theory පහතින් බලන්න:</p>
      
      <select id="unitSelect" class="unit-select" onchange="loadTheoryUnit()">
        <option value="1">01. Measurement (මිනුම්)</option>
        <option value="2">02. Mechanics (යාන්ත්‍රික විද්‍යාව)</option>
        <option value="3">03. Oscillations & Waves (දෝලන හා තරංග)</option>
        <option value="4">04. Thermal Physics (තාප භෞතික විද්‍යාව)</option>
        <option value="5">05. Gravitational Field (ගුරුත්වාකර්ෂණ ක්ෂේත්‍ර)</option>
        <option value="6">06. Electrostatic Field (විද්‍යුත් ක්ෂේත්‍ර)</option>
        <option value="7">07. Current Electricity (ධාරා විද්‍යුතය)</option>
        <option value="8">08. Electromagnetism (චුම්බක ක්ෂේත්‍ර)</option>
        <option value="9">09. Electronics (ඉලෙක්ට්‍රොනික්ස්)</option>
        <option value="10">10. Radiation & Matter (විකිරණ හා පදාර්ථ)</option>
      </select>

      <hr style="border-color:#333; margin:10px 0;">

      <label style="cursor:pointer; font-weight:bold; color:var(--gold-primary); font-size:0.85rem;">
        <input type="checkbox" id="superPerfToggle" onchange="triggerReLoad()"> 🔥 Super Performance Mode
      </label>
    </div>

    <div class="content-area">
      <!-- Theory Display Card -->
      <div class="card theory-section">
        <h2 id="unitTitle" style="color:var(--gold-primary); margin:0;">01. Measurement (මිනුම්)</h2>
        <div id="theoryContent" style="color:#ddd; line-height:1.6; font-size:0.95rem; overflow-y:auto; padding-right:10px;">
          <!-- Theory Content Loaded via JS -->
        </div>
      </div>

      <!-- Questions & Custom Entry Section -->
      <div class="card qa-notes-section">
        <h3 style="color:var(--neon-cyan); margin:0;">❓ ADD / VIEW QUESTIONS</h3>
        <p style="color:#aaa; font-size:0.8rem; margin-top:-5px;">ඔයාගේ ප්‍රශ්න මෙතැනට එකතු කරන්න:</p>
        
        <input type="text" id="qInput" placeholder="Enter Question / ප්‍රශ්නය ඇතුළත් කරන්න...">
        <textarea id="aInput" style="height:60px;" placeholder="Enter Solution / විසඳුම..."></textarea>
        <button class="btn-action" onclick="addCustomQuestion()">➕ Add Question</button>

        <hr style="border-color:#333; margin:10px 0;">

        <h4 style="color:var(--gold-primary); margin:0;">📝 QUICK NOTES</h4>
        <textarea id="userNotes" style="height:120px;" placeholder="Write your notes here..."></textarea>
        <button class="btn-action" style="background:var(--neon-cyan);" onclick="saveNotes()">💾 Save Notes</button>
      </div>
    </div>
  </div>

  <!-- Footer Branding -->
  <div class="footer-left">
    <button class="exit-btn" onclick="executeExitSequence()">EXIT ENGINE ✖</button>
  </div>

  <div class="footer-right">
    <div class="lv-monogram">
      👑 JANIDU KAVEESHA<br>
      <span style="font-size:0.6rem; color:#fff;">✦ LUXURY EDITION ✦</span>
    </div>
    <div class="gemini-power">⚡ POWERED BY GEMINI AI ⚡</div>
  </div>

  <div id="shatter-overlay">
    <div class="lv-monogram" style="font-size: 2rem; text-align: center;">👑 JANIDU KAVEESHA</div>
  </div>

  <script>
    const physicsData = {
      "1": "<b>මූලික ඒකක සහ මාන:</b><br>• දිග (m), ස්කන්ධය (kg), කාලය (s), ධාරාව (A), උෂ්ණත්වය (K)<br>• <b>මාන සූත්‍ර:</b> වේගය [LT⁻¹], ත්වරණය [LT⁻²], බලය [MLT⁻²], කාර්යය [ML²T⁻²]<br>• <b>මිනුම් උපකරණ:</b> වේනියර් කැලිපරය, මයික්‍රෝමීටර් පස් ගේජය, ගෝලමානය (අවම මිනුම = ප්‍රධාන පරිමාණ කොටස / උපපරිමාණ කොටස් ගණන)",
      "2": "<b>චලිත සමීකරණ:</b><br>1) v = u + at<br>2) s = ut + ½at²<br>3) v² = u² + 2as<br>4) s = ((u+v)/2)t<br><br><b>නව්ටන් නියම & ගම්‍යතාව:</b><br>• F = ma<br>• ගම්‍යතාව p = mv<br>• කාර්යය W = F.s | ක්ෂමතාව P = W/t",
      "3": "<b>සරල අනුරූපී චලිතය (S.H.M):</b><br>• ත්වරණය a = -ω²x<br>• ආවර්ත කාලය T = 2π/ω<br>• තනි අංකෝලයක T = 2π√(l/g)<br>• <b>දොප්ලර් ආචරණය:</b> f' = f ((v ± v_o) / (v ∓ v_s))",
      "4": "<b>තාප ගති විද්‍යාව:</b><br>• Q = mcΔθ | Q = mL<br>• ප්‍රථම නියමය: ΔQ = ΔU + ΔW<br>• වායු නියම: PV = nRT",
      "5": "<b>ගුරුත්වාකර්ෂණය:</b><br>• F = G(M1 M2 / r²)<br>• ගුරුත්වජ ක්ෂේත්‍ර තීව්‍රතාව g = GM/R²<br>• මුදවාලීමේ වේගය v = √(2GM/R)",
      "6": "<b>ස්ථිති විද්‍යුතය:</b><br>• කුලෝම් නියමය F = (1 / 4πε) * (q1 q2 / r²)<br>• විද්‍යුත් ක්ෂේත්‍ර තීව්‍රතාව E = F/q<br>• ධාරිතාව C = Q/V = εA/d",
      "7": "<b>ධාරා විද්‍යුතය:</b><br>• ඕම් නියමය V = IR<br>• ප්‍රතිරෝධය R = ρl/A<br>• කර්චොෆ් නියම: ΣI = 0 | ΣE = ΣIR",
      "8": "<b>චුම්බක ක්ෂේත්‍ර:</b><br>• බලය F = B I L sinθ | F = qvB sinθ<br>• ෆැරඩේ නියමය: e = -dΦ/dt",
      "9": "<b>ඉලෙක්ට්‍රොනික්ස්:</b><br>• p-n සන්ධි ඩයෝඩ, ට්‍රාන්සිස්ටර (I_E = I_B + I_C)<br>• Logic Gates: AND, OR, NOT, NAND, NOR",
      "10": "<b>ඡායා විද්‍යුත් ආචරණය:</b><br>• E = hf = hf₀ + ½mv²_max<br>• ද බ්‍රෝග්ලි තරංග ආයාමය λ = h/p"
    };

    const audioCtx = new (window.AudioContext || window.webkitAudioContext)();

    function playSynthesizedSound(type) {
      if (audioCtx.state === 'suspended') audioCtx.resume();
      const now = audioCtx.currentTime;
      if (type === 'fan') {
        const buffer = audioCtx.createBuffer(1, audioCtx.sampleRate * 3.5, audioCtx.sampleRate);
        const data = buffer.getChannelData(0);
        for (let i = 0; i < buffer.length; i++) data[i] = Math.random() * 2 - 1;
        const noise = audioCtx.createBufferSource(); noise.buffer = buffer;
        const filter = audioCtx.createBiquadFilter(); filter.type = 'bandpass'; filter.frequency.value = 400;
        const gain = audioCtx.createGain(); gain.gain.setValueAtTime(0.08, now);
        noise.connect(filter); filter.connect(gain); gain.connect(audioCtx.destination);
        noise.start(now); return { osc: noise };
      } else if (type === 'piston') {
        const osc = audioCtx.createOscillator(); const gain = audioCtx.createGain();
        osc.type = 'sawtooth'; osc.frequency.setValueAtTime(35, now);
        gain.gain.setValueAtTime(0.2, now); osc.connect(gain); gain.connect(audioCtx.destination);
        osc.start(now); return { osc };
      }
    }

    function initializeEngine() {
      document.getElementById('start-screen').style.display = 'none';
      document.getElementById('bg-video').play();
      runLoadingSequence();
      loadTheoryUnit();
      loadSavedNotes();
    }

    function runLoadingSequence() {
      const loader = document.getElementById('loading-screen');
      const isSuperMode = document.getElementById('superPerfToggle').checked;
      loader.style.display = 'flex';
      let sound = isSuperMode ? playSynthesizedSound('piston') : playSynthesizedSound('fan');
      setTimeout(() => {
        if (sound && sound.osc) sound.osc.stop();
        loader.style.display = 'none';
      }, 3000);
    }

    function triggerReLoad() { runLoadingSequence(); }

    function loadTheoryUnit() {
      const val = document.getElementById('unitSelect').value;
      const title = document.getElementById('unitSelect').options[document.getElementById('unitSelect').selectedIndex].text;
      document.getElementById('unitTitle').innerText = title;
      document.getElementById('theoryContent').innerHTML = physicsData[val] || "Theory content updating...";
    }

    function addCustomQuestion() {
      const q = document.getElementById('qInput').value;
      const a = document.getElementById('aInput').value;
      if(!q) return alert('කරුණාකර ප්‍රශ්නයක් ඇතුළත් කරන්න!');
      
      const newBox = document.createElement('div');
      newBox.style.cssText = "background:rgba(0,0,0,0.5); padding:10px; border-left:3px solid var(--neon-cyan); margin-top:8px; border-radius:4px;";
      newBox.innerHTML = `<b>Q: ${q}</b><br><span style="color:#aaa;">A: ${a}</span>`;
      document.querySelector('.qa-notes-section').appendChild(newBox);
      
      document.getElementById('qInput').value = '';
      document.getElementById('aInput').value = '';
    }

    function saveNotes() {
      localStorage.setItem('batman_physics_notes', document.getElementById('userNotes').value);
      alert('Notes Saved!');
    }

    function loadSavedNotes() {
      const saved = localStorage.getItem('batman_physics_notes');
      if(saved) document.getElementById('userNotes').value = saved;
    }

    function executeExitSequence() {
      document.getElementById('shatter-overlay').style.display = 'flex';
    }
  </script>
</body>
</html>
"""

components.html(html_code, height=1000, scrolling=True)