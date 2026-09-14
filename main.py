import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="BATMAN PHYSICS MASTER", layout="wide")

# HTML / CSS / JavaScript Full Master Engine
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

    /* CSS Pure Power Button (No External Image Needed) */
    .power-btn {
      width: 120px; height: 120px;
      border-radius: 50%;
      background: radial-gradient(circle, #ff0033 0%, #300 70%, #000 100%);
      border: 4px solid var(--danger-red);
      color: #fff; font-size: 2.5rem; font-weight: bold;
      cursor: pointer;
      box-shadow: 0 0 30px var(--danger-red);
      transition: transform 0.2s, box-shadow 0.2s;
      display: flex; justify-content: center; align-items: center;
    }

    .power-btn:hover {
      transform: scale(1.1);
      box-shadow: 0 0 50px var(--neon-cyan);
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

    /* Cooling Fan Animation */
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
      animation: spinFan 0.2s linear infinite;
    }

    @keyframes spinFan { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }

    /* CSS Live 3D Piston Engine Animation */
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
      animation: pistonMove 0.25s infinite alternate ease-in-out;
    }

    .piston:nth-child(2) { animation-delay: 0.12s; }
    .piston:nth-child(3) { animation-delay: 0.06s; }

    @keyframes pistonMove {
      0% { transform: translateY(0px); background: linear-gradient(180deg, var(--danger-red), #888); }
      100% { transform: translateY(-45px); background: linear-gradient(180deg, #fff, var(--gold-primary)); }
    }

    /* 3. ULTRA HD VIDEO BACKGROUND */
    #bg-video {
      position: fixed; right: 0; bottom: 0;
      min-width: 100%; min-height: 100%;
      width: auto; height: auto; z-index: -2;
      object-fit: cover;
    }

    /* 4. MAIN UI LAYOUT */
    .app-container {
      display: flex; height: 100vh;
      background: rgba(0, 0, 0, 0.7);
    }

    .sidebar {
      width: 320px; background: rgba(10, 10, 15, 0.95);
      padding: 20px; border-right: 2px solid #222;
      display: flex; flex-direction: column; gap: 15px;
    }

    .sidebar h2 { color: var(--gold-primary); margin-top: 0; }

    .lang-option {
      display: flex; align-items: center; gap: 10px;
      margin: 10px 0; cursor: pointer; font-weight: bold;
    }

    /* FOOTER BRANDING & EXIT */
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

  <!-- Ultra HD Video Engine -->
  <video id="bg-video" autoplay muted loop></video>

  <!-- Start Overlay Screen -->
  <div id="start-screen">
    <button class="power-btn" onclick="initializeEngine()">POWER</button>
  </div>

  <!-- Dynamic Loading Overlay -->
  <div id="loading-screen">
    <div class="server-blur-bg"></div>
    
    <!-- Fan Animation -->
    <div id="fan-anim" class="fan-container">
      <div class="fan-blades"></div>
    </div>

    <!-- Live 3D Piston Animation -->
    <div id="piston-anim" class="piston-block">
      <div class="piston-chamber">
        <div class="piston"></div>
        <div class="piston"></div>
        <div class="piston"></div>
      </div>
    </div>

    <p id="loading-text" style="margin-top:25px; font-weight:bold; letter-spacing:2px; color:var(--neon-cyan);">ENGINE INITIALIZING...</p>
  </div>

  <!-- Main Application Workspace -->
  <div class="app-container">
    <div class="sidebar">
      <h2>⚙️ ENGINE CONTROLS</h2>
      <div>
        <p style="color:#aaa; font-size:0.9rem;">Language / භාෂාව</p>
        <label class="lang-option">
          <input type="radio" name="lang" value="en" checked onclick="triggerReLoad()"> 🇬🇧 ENGLISH
        </label>
        <label class="lang-option">
          <input type="radio" name="lang" value="si" onclick="triggerReLoad()"> 🇱🇰 SINHALA
        </label>
      </div>

      <hr style="border-color:#333; margin:15px 0;">

      <label style="cursor:pointer; font-weight:bold; color:var(--gold-primary);">
        <input type="checkbox" id="superPerfToggle" onchange="triggerReLoad()"> 🔥 Super Performance Mode
      </label>
    </div>

    <div style="flex:1; padding:30px;">
      <h1 style="color:var(--gold-primary);">🦇 BATMAN PHYSICS MASTER (A/L ENGINE)</h1>
      <p style="color:#ccc;">විෂය නිර්දේශයේ සියලුම පාඩම් වල රූප සටහන් සහ AI Logic Solver මෙතැනින් ක්‍රියාත්මක වේ.</p>
    </div>
  </div>

  <!-- Footer Branding & Controls -->
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

  <!-- Shatter Exit Screen -->
  <div id="shatter-overlay">
    <div class="lv-monogram" style="font-size: 2.5rem; text-align: center;">
      👑<br>
      JK<br>
      JANIDU KAVEESHA<br>
      <span style="font-size:1rem; color:#fff;">✦ LUXURY EDITION ✦</span>
    </div>
  </div>

  <script>
    // Direct Streamable Ultra HD Online Video CDN URLs
    const bgVideos = [
      'https://assets.mixkit.co/videos/preview/mixkit-tunnel-of-futuristic-lights-41552-large.mp4',
      'https://assets.mixkit.co/videos/preview/mixkit-red-and-orange-background-of-abstract-lines-41555-large.mp4',
      'https://assets.mixkit.co/videos/preview/mixkit-abstract-fast-flashing-lines-41548-large.mp4'
    ];

    // Web Audio Synthesizer (Real-time Generated Sound)
    const audioCtx = new (window.AudioContext || window.webkitAudioContext)();

    function playSynthesizedSound(type) {
      if (audioCtx.state === 'suspended') audioCtx.resume();
      
      const osc = audioCtx.createOscillator();
      const gain = audioCtx.createGain();
      osc.connect(gain);
      gain.connect(audioCtx.destination);

      if (type === 'fan') {
        osc.type = 'sawtooth';
        osc.frequency.setValueAtTime(80, audioCtx.currentTime);
        gain.gain.setValueAtTime(0.05, audioCtx.currentTime);
      } else if (type === 'piston') {
        osc.type = 'square';
        osc.frequency.setValueAtTime(40, audioCtx.currentTime);
        gain.gain.setValueAtTime(0.15, audioCtx.currentTime);
      } else if (type === 'shatter') {
        osc.type = 'triangle';
        osc.frequency.setValueAtTime(300, audioCtx.currentTime);
        osc.frequency.exponentialRampToValueAtTime(40, audioCtx.currentTime + 0.3);
        gain.gain.setValueAtTime(0.3, audioCtx.currentTime);
      }

      osc.start();
      return { osc, gain };
    }

    function setRandomBgVideo() {
      const selected = bgVideos[Math.floor(Math.random() * bgVideos.length)];
      const videoElem = document.getElementById('bg-video');
      videoElem.src = selected;
    }

    function initializeEngine() {
      if (navigator.vibrate) navigator.vibrate(100);
      document.getElementById('start-screen').style.display = 'none';
      runLoadingSequence();
    }

    function runLoadingSequence() {
      const loader = document.getElementById('loading-screen');
      const isSuperMode = document.getElementById('superPerfToggle').checked;
      const fanAnim = document.getElementById('fan-anim');
      const pistonAnim = document.getElementById('piston-anim');

      loader.style.display = 'flex';

      let activeSound;
      if (isSuperMode) {
        fanAnim.style.display = 'none';
        pistonAnim.style.display = 'block';
        activeSound = playSynthesizedSound('piston');
      } else {
        pistonAnim.style.display = 'none';
        fanAnim.style.display = 'block';
        activeSound = playSynthesizedSound('fan');
      }

      setTimeout(() => {
        if (activeSound) activeSound.osc.stop();
        loader.style.display = 'none';
        setRandomBgVideo();
      }, 3500);
    }

    function triggerReLoad() {
      runLoadingSequence();
    }

    function executeExitSequence() {
      playSynthesizedSound('shatter');
      const shatterScreen = document.getElementById('shatter-overlay');
      shatterScreen.style.display = 'flex';
    }
  </script>
</body>
</html>
"""

components.html(html_code, height=1000, scrolling=True)