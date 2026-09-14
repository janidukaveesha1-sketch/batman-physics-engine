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

    /* 1. START LANDING SCREEN */
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
      display: flex; justify-content: center; align-items: center;
    }

    .power-btn:hover {
      transform: scale(1.1);
      box-shadow: 0 0 55px var(--neon-cyan);
      border-color: var(--neon-cyan);
    }

    /* 2. DYNAMIC LOADING SCREEN */
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

    @keyframes pulseBg {
      0% { opacity: 0.3; } 100% { opacity: 0.8; }
    }

    .fan-container {
      width: 120px; height: 120px;
      border: 6px solid #222; border-radius: 50%;
      position: relative; display: flex;
      justify-content: center; align-items: center;
      box-shadow: 0 0 25px var(--neon-cyan);
    }

    .fan-blades {
      width: 100%; height: 100%; position: absolute;
      border-radius: 50%;
      background: conic-gradient(from 0deg, var(--neon-cyan) 0deg 45deg, transparent 45deg 90deg, var(--neon-cyan) 90deg 135deg, transparent 135deg 180deg, var(--neon-cyan) 180deg 225deg, transparent 225deg 270deg, var(--neon-cyan) 270deg 315deg, transparent 315deg 360deg);
      animation: spinFan 0.15s linear infinite;
    }

    @keyframes spinFan { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }

    .piston-block {
      display: none; width: 220px; height: 140px;
      position: relative; border: 2px solid var(--danger-red);
      background: rgba(20, 0, 0, 0.85); border-radius: 8px;
      box-shadow: 0 0 30px var(--danger-red); padding: 10px;
    }

    .piston-chamber {
      display: flex; justify-content: space-around;
      align-items: flex-end; height: 100%;
    }

    .piston {
      width: 35px; height: 60px;
      background: linear-gradient(180deg, #fff, #888, #333);
      border-radius: 4px 4px 0 0;
      animation: pistonMove 0.2s infinite alternate ease-in-out;
    }

    .piston:nth-child(2) { animation-delay: 0.1s; }
    .piston:nth-child(3) { animation-delay: 0.05s; }

    @keyframes pistonMove {
      0% { transform: translateY(0px); background: linear-gradient(180deg, var(--danger-red), #888); }
      100% { transform: translateY(-45px); background: linear-gradient(180deg, #fff, var(--gold-primary)); }
    }

    /* 3. FIXED SINGLE VIDEO BACKGROUND */
    #bg-video {
      position: fixed; right: 0; bottom: 0;
      min-width: 100%; min-height: 100%;
      width: auto; height: auto; z-index: -2;
      object-fit: cover;
    }

    /* 4. MAIN UI WORKSPACE */
    .app-container {
      display: flex; height: 100vh;
      background: rgba(0, 0, 0, 0.75);
    }

    .sidebar {
      width: 280px; background: rgba(10, 10, 15, 0.95);
      padding: 20px; border-right: 2px solid #222;
      display: flex; flex-direction: column; gap: 15px;
    }

    .sidebar h2 { color: var(--gold-primary); margin-top: 0; font-size: 1.3rem; }

    .lang-option {
      display: flex; align-items: center; gap: 10px;
      margin: 8px 0; cursor: pointer; font-weight: bold;
    }

    .content-area {
      flex: 1; padding: 25px; display: flex; gap: 20px;
      overflow-y: auto; height: calc(100vh - 100px);
    }

    .card {
      background: rgba(15, 15, 22, 0.85);
      border: 1px solid #333; border-radius: 10px;
      padding: 20px; box-shadow: 0 0 15px rgba(0,0,0,0.5);
    }

    .question-section { flex: 2; display: flex; flex-direction: column; gap: 15px; }
    .notes-section { flex: 1; display: flex; flex-direction: column; gap: 10px; }

    .btn-action {
      background: linear-gradient(45deg, var(--gold-secondary), var(--gold-primary));
      color: #000; font-weight: bold; border: none;
      padding: 10px 15px; border-radius: 5px; cursor: pointer;
      transition: transform 0.2s;
    }
    .btn-action:hover { transform: scale(1.03); }

    textarea {
      width: 95%; height: 250px; background: rgba(0, 0, 0, 0.6);
      border: 1px solid var(--neon-cyan); color: #fff;
      padding: 10px; border-radius: 5px; font-family: monospace;
      resize: vertical;
    }

    /* FOOTER BRANDING & CONTROLS */
    .footer-left { position: fixed; bottom: 15px; left: 15px; z-index: 100; }

    .exit-btn {
      background: linear-gradient(45deg, #400, var(--danger-red));
      color: #fff; border: 1px solid var(--danger-red);
      padding: 10px 18px; font-weight: bold; cursor: pointer;
      box-shadow: 0 0 12px rgba(255,0,51,0.6);
      border-radius: 4px; transition: 0.2s;
    }

    .exit-btn:hover { transform: scale(1.05); }

    .footer-right { position: fixed; bottom: 15px; right: 15px; text-align: right; z-index: 100; }

    .lv-monogram {
      color: var(--gold-secondary); font-weight: bold;
      text-shadow: 0 0 8px rgba(212,175,55,0.8); line-height: 1.2;
    }

    .gemini-power {
      color: var(--neon-cyan); font-size: 0.75rem;
      letter-spacing: 1px; text-shadow: 0 0 6px var(--neon-cyan);
      margin-top: 5px; font-weight: bold;
    }

    /* SHATTER EXIT SCREEN */
    #shatter-overlay {
      position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
      background: #000; display: none;
      justify-content: center; align-items: center;
      flex-direction: column; z-index: 10000;
      animation: shatterEffect 0.4s ease-out forwards;
    }

    @keyframes shatterEffect {
      0% { transform: scale(1.3); opacity: 0; filter: blur(10px); }
      100% { transform: scale(1); opacity: 1; filter: blur(0); }
    }
  </style>
</head>
<body>

  <!-- Single Fixed Background Video Path -->
  <video id="bg-video" autoplay muted loop src="file:///C:/Users/Kavee/OneDrive/Documents/physics/assets/dark-batman-shadow-portrait-live-wallpaper.mp4"></video>

  <!-- Start Screen -->
  <div id="start-screen">
    <button class="power-btn" onclick="initializeEngine()">START</button>
  </div>

  <!-- Dynamic Loading Screen -->
  <div id="loading-screen">
    <div class="server-blur-bg"></div>
    <div id="fan-anim" class="fan-container"><div class="fan-blades"></div></div>
    <div id="piston-anim" class="piston-block">
      <div class="piston-chamber">
        <div class="piston"></div><div class="piston"></div><div class="piston"></div>
      </div>
    </div>
    <p id="loading-text" style="margin-top:25px; font-weight:bold; letter-spacing:2px; color:var(--neon-cyan);">ENGINE INITIALIZING...</p>
  </div>

  <!-- Workspace -->
  <div class="app-container">
    <div class="sidebar">
      <h2>⚙️ ENGINE CONTROLS</h2>
      <div>
        <p style="color:#aaa; font-size:0.85rem;">Language / භාෂාව</p>
        <label class="lang-option"><input type="radio" name="lang" value="en" checked onclick="triggerReLoad()"> 🇬🇧 ENGLISH</label>
        <label class="lang-option"><input type="radio" name="lang" value="si" onclick="triggerReLoad()"> 🇱🇰 SINHALA</label>
      </div>
      <hr style="border-color:#333; margin:10px 0;">
      <label style="cursor:pointer; font-weight:bold; color:var(--gold-primary); font-size:0.9rem;">
        <input type="checkbox" id="superPerfToggle" onchange="triggerReLoad()"> 🔥 Super Performance
      </label>
    </div>

    <div class="content-area">
      <div class="card question-section">
        <h2 style="color:var(--gold-primary); margin:0;">🦇 PHYSICS QUESTION SOLVER</h2>
        <p style="color:#aaa; margin-top:-5px;">විෂය නිර්දේශයේ ගැටලු සහ ප්‍රශ්න මෙතැනින් පෙන්වයි.</p>
        
        <div style="background:rgba(0,0,0,0.4); padding:15px; border-left:4px solid var(--gold-primary); border-radius:4px;">
          <h4 style="margin:0 0 8px 0; color:var(--neon-cyan);">Question #01: චලිතය (Mechanics)</h4>
          <p style="margin:0; font-size:0.95rem; color:#ddd;">
            තලයක තබා ඇති $m$ ස්කන්ධයක් සහිත වස්තුවක් මත $F$ බලයක් යෙදූ විට එහි ත්වරණය $a$ වේ. වස්තුවේ ස්කන්ධය දෙගුණ කළ විට ඇතිවන අලුත් ත්වරණය කොපමණද?
          </p>
        </div>

        <div>
          <button class="btn-action" onclick="alert('Solution: F = ma අනුව ත්වරණය a\' = a/2 වේ.')">💡 View Solution (විසඳුම බලන්න)</button>
        </div>
      </div>

      <div class="card notes-section">
        <h3 style="color:var(--neon-cyan); margin:0;">📝 QUICK NOTES PAD</h3>
        <p style="color:#aaa; font-size:0.8rem; margin-top:-5px;">පාඩම් කරන අතරතුර මතක සටහන් ලියාගන්න.</p>
        <textarea id="userNotes" placeholder="Write your Physics notes or formulas here..."></textarea>
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
      👑<br>
      JK<br>
      JANIDU KAVEESHA<br>
      <span style="font-size:0.6rem; letter-spacing:1px; color:#fff;">✦ LUXURY EDITION ✦</span>
    </div>
    <div class="gemini-power">
      ⚡ ☠ POWERED BY GEMINI AI ☠ ⚡
    </div>
  </div>

  <div id="shatter-overlay">
    <div class="lv-monogram" style="font-size: 2.5rem; text-align: center;">
      👑<br>
      JK<br>
      JANIDU KAVEESHA<br>
      <span style="font-size:1rem; color:#fff;">✦ LUXURY EDITION ✦</span>
    </div>
  </div>

  <script>
    const audioCtx = new (window.AudioContext || window.webkitAudioContext)();

    // REALISTIC AUDIO ENGINE
    function playSynthesizedSound(type) {
      if (audioCtx.state === 'suspended') audioCtx.resume();
      
      const now = audioCtx.currentTime;

      if (type === 'fan') {
        // High-velocity Wind / Mechanical Fan noise
        const bufferSize = audioCtx.sampleRate * 3.5;
        const buffer = audioCtx.createBuffer(1, bufferSize, audioCtx.sampleRate);
        const data = buffer.getChannelData(0);
        for (let i = 0; i < bufferSize; i++) data[i] = Math.random() * 2 - 1;

        const noise = audioCtx.createBufferSource();
        noise.buffer = buffer;

        const filter = audioCtx.createBiquadFilter();
        filter.type = 'bandpass';
        filter.frequency.value = 400;

        const gain = audioCtx.createGain();
        gain.gain.setValueAtTime(0.08, now);

        noise.connect(filter);
        filter.connect(gain);
        gain.connect(audioCtx.destination);
        noise.start(now);
        return { osc: noise };

      } else if (type === 'piston') {
        // Deep V8 Mechanical Piston Engine Thump
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        osc.type = 'sawtooth';
        
        // Low Frequency Rumble
        osc.frequency.setValueAtTime(32, now);
        osc.frequency.linearRampToValueAtTime(45, now + 3.5);

        gain.gain.setValueAtTime(0.2, now);
        osc.connect(gain);
        gain.connect(audioCtx.destination);
        osc.start(now);
        return { osc };

      } else if (type === 'shatter') {
        // Real Metallic Glass Crack Sharp Impulses
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        osc.type = 'square';
        osc.frequency.setValueAtTime(800, now);
        osc.frequency.exponentialRampToValueAtTime(30, now + 0.35);
        gain.gain.setValueAtTime(0.4, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.35);

        osc.connect(gain);
        gain.connect(audioCtx.destination);
        osc.start(now);
        return { osc };
      }
    }

    function initializeEngine() {
      if (navigator.vibrate) navigator.vibrate(100);
      document.getElementById('start-screen').style.display = 'none';
      document.getElementById('bg-video').play();
      runLoadingSequence();
      loadSavedNotes();
    }

    function runLoadingSequence() {
      const loader = document.getElementById('loading-screen');
      const isSuperMode = document.getElementById('superPerfToggle').checked;
      const fanAnim = document.getElementById('fan-anim');
      const pistonAnim = document.getElementById('piston-anim');

      loader.style.display = 'flex';
      let activeSound;
      if (isSuperMode) {
        fanAnim.style.display = 'none'; pistonAnim.style.display = 'block'; 
        activeSound = playSynthesizedSound('piston');
      } else {
        pistonAnim.style.display = 'none'; fanAnim.style.display = 'block'; 
        activeSound = playSynthesizedSound('fan');
      }

      setTimeout(() => {
        if (activeSound && activeSound.osc) activeSound.osc.stop();
        loader.style.display = 'none';
      }, 3500);
    }

    function triggerReLoad() { runLoadingSequence(); }

    function executeExitSequence() {
      playSynthesizedSound('shatter');
      document.getElementById('shatter-overlay').style.display = 'flex';
    }

    function saveNotes() {
      const notes = document.getElementById('userNotes').value;
      localStorage.setItem('batman_physics_notes', notes);
      alert('Notes Saved Successfully! (සටහන් සාර්ථකව සුරැකිණි)');
    }

    function loadSavedNotes() {
      const savedNotes = localStorage.getItem('batman_physics_notes');
      if(savedNotes) {
        document.getElementById('userNotes').value = savedNotes;
      }
    }
  </script>
</body>
</html>
"""

components.html(html_code, height=1000, scrolling=True)