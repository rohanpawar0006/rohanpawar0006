<div align="center">

  <!-- ================================================================= -->
  <!-- 1. ANIMATED HERO HEADER                                           -->
  <!-- ================================================================= -->
  <a href="https://github.com/rohanpawar0006">
    <img src="assets/header.svg" alt="Rohan Pawar - AI/ML Engineer in the Making" width="100%" />
  </a>

  <br/>

  <!-- ================================================================= -->
  <!-- 2. TYPING INTRO DYNAMIC BANNER                                   -->
  <!-- ================================================================= -->
  <a href="https://git.io/typing-svg">
    <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=20&pause=1200&color=00E5FF&center=true&vCenter=true&width=650&height=45&lines=RAG+Systems+Engineered+From+First+Principles;Real-Time+Computer+Vision+%26+Edge+Inference;Autonomous+Agents+%26+Deterministic+Pipelines;Actively+Seeking+AI%2FML+Internships" alt="Typing SVG" />
  </a>

  <br/>
  <img src="assets/divider.svg" width="100%" alt="divider" />
  <br/>

</div>

<!-- ================================================================= -->
<!-- 3. ABOUT ME (FROSTED GLASS CARD)                                  -->
<!-- ================================================================= -->
<div align="center">
  <img src="assets/about-card.svg" width="100%" alt="About Rohan Pawar" />
</div>

<br/>

> 💡 **Core Philosophy:** *Anyone can `pip install` a monolithic wrapper. Real engineering means understanding chunking dynamics, loss surfaces, embedding distances, latency ceilings, and grounding guarantees.*

<br/>
<div align="center">
  <img src="assets/divider.svg" width="100%" alt="divider" />
</div>
<br/>

<!-- ================================================================= -->
<!-- 4. FEATURED PROJECTS                                             -->
<!-- ================================================================= -->
## ⚡ Featured Production Projects

<table>
  <tr>
    <td>
      <!-- Project 1: VaultMind-RAG -->
      <a href="https://github.com/rohanpawar0006/vaultmind-rag">
        <img src="assets/project-vaultmind.svg" width="100%" alt="VaultMind-RAG Project Card" />
      </a>
      <p align="center">
        <a href="https://github.com/rohanpawar0006/vaultmind-rag">
          <img src="https://img.shields.io/badge/Repository-VaultMind--RAG-00E5FF?style=for-the-badge&logo=github&logoColor=0B0F1A" alt="VaultMind Repo" />
        </a>
      </p>
      <details>
        <summary><b>🔍 Deep-Dive: Architecture &amp; Mechanics (Click to Expand)</b></summary>
        <br/>
        <ul>
          <li><b>Zero LangChain / LlamaIndex:</b> Built purely using raw Python, ChromaDB, and Google GenAI SDK to ensure full control over chunking and retrieval behavior.</li>
          <li><b>Sanitization &amp; Chunking:</b> Cleans Markdown metadata, code fences, and wikilinks using a custom sliding-window chunker with dynamic overlap.</li>
          <li><b>Local Dense Embeddings:</b> Uses <code>sentence-transformers/all-MiniLM-L6-v2</code> running locally to generate 384-dimensional dense vectors.</li>
          <li><b>Threshold Cosine Fallback:</b> Calculates cosine similarity scores; if top-k matches fall below threshold (&lt; 0.70), it safely refuses to hallucinate and alerts the user.</li>
          <li><b>Obsidian Native UX:</b> Streamlit frontend themed with Obsidian Dark palette, returning responses with clickable source note links (<code>[[note#header]]</code>).</li>
        </ul>
        <div align="center">
          <a href="https://github.com/rohanpawar0006/vaultmind-rag">
            <img src="assets/screenshots/vaultmind-preview.svg" width="85%" alt="VaultMind UI Screenshot" />
          </a>
        </div>
      </details>
    </td>
  </tr>
  <tr>
    <td>
      <br/>
      <!-- Project 2: SignBridge AI -->
      <a href="https://github.com/rohanpawar0006/SignBridge-AI">
        <img src="assets/project-signbridge.svg" width="100%" alt="SignBridge AI Project Card" />
      </a>
      <p align="center">
        <a href="https://github.com/rohanpawar0006/SignBridge-AI">
          <img src="https://img.shields.io/badge/Repository-SignBridge--AI-7C4DFF?style=for-the-badge&logo=github&logoColor=FFFFFF" alt="SignBridge Repo" />
        </a>
        &nbsp;
        <a href="https://sign-bridge-ai-alpha.vercel.app/">
          <img src="https://img.shields.io/badge/Live_App-sign--bridge--ai.vercel.app-00E5FF?style=for-the-badge&logo=vercel&logoColor=0B0F1A" alt="SignBridge Live App" />
        </a>
      </p>
      <details>
        <summary><b>🔍 Deep-Dive: Architecture &amp; Mechanics (Click to Expand)</b></summary>
        <br/>
        <ul>
          <li><b>Two-Way Dialogue:</b> Complete bidirectional bridge — converts physical ISL signs into synthetic audio speech, and spoken voice into animated sign gestures.</li>
          <li><b>Vision Pipeline:</b> Real-time landmark extraction via MediaPipe Hand Mesh, normalized and passed into a PyTorch Bidirectional LSTM (Bi-LSTM).</li>
          <li><b>Vocabulary Scale:</b> Recognizes 16 continuous dynamic ISL gestures plus an on-device 36-class classifier for static alphabets and digits.</li>
          <li><b>Sub-40ms Edge Latency:</b> Highly optimized client-side landmark preprocessing with asynchronous backend inference deployed on Render.</li>
          <li><b>Full Suite:</b> Includes an interactive ISL digital dictionary and a gamified practice mode to help non-signers learn Indian Sign Language.</li>
        </ul>
        <div align="center">
          <a href="https://sign-bridge-ai-alpha.vercel.app/">
            <img src="assets/screenshots/signbridge-preview.svg" width="85%" alt="SignBridge UI Screenshot" />
          </a>
        </div>
      </details>
    </td>
  </tr>
  <tr>
    <td>
      <br/>
      <!-- Project 3: Next Deployment Slot -->
      <a href="https://github.com/rohanpawar0006">
        <img src="assets/project-placeholder.svg" width="100%" alt="Upcoming Project Card" />
      </a>
    </td>
  </tr>
</table>

<br/>
<div align="center">
  <img src="assets/divider.svg" width="100%" alt="divider" />
</div>
<br/>

<!-- ================================================================= -->
<!-- 5. TECH STACK / SKILL BADGES GRID                                -->
<!-- ================================================================= -->
## 🛠️ Technical Weaponry

<div align="center">

<!-- Row 1: Languages -->
### Languages
<p>
  <img src="https://img.shields.io/badge/Python-0B0F1A?style=for-the-badge&logo=python&logoColor=00E5FF" alt="Python" />
  <img src="https://img.shields.io/badge/JavaScript-0B0F1A?style=for-the-badge&logo=javascript&logoColor=F7DF1E" alt="JavaScript" />
  <img src="https://img.shields.io/badge/C%2B%2B-0B0F1A?style=for-the-badge&logo=c%2B%2B&logoColor=00599C" alt="C++" />
  <img src="https://img.shields.io/badge/SQL-0B0F1A?style=for-the-badge&logo=postgresql&logoColor=3D8BFF" alt="SQL" />
</p>

<!-- Row 2: AI & Machine Learning -->
### AI & Machine Learning
<p>
  <img src="https://img.shields.io/badge/PyTorch-0B0F1A?style=for-the-badge&logo=pytorch&logoColor=EE4C2C" alt="PyTorch" />
  <img src="https://img.shields.io/badge/Scikit--Learn-0B0F1A?style=for-the-badge&logo=scikit-learn&logoColor=F7931E" alt="scikit-learn" />
  <img src="https://img.shields.io/badge/MediaPipe-0B0F1A?style=for-the-badge&logo=google&logoColor=00E5FF" alt="MediaPipe" />
  <img src="https://img.shields.io/badge/Hugging_Face-0B0F1A?style=for-the-badge&logo=huggingface&logoColor=FFD21E" alt="Hugging Face" />
  <img src="https://img.shields.io/badge/ChromaDB-0B0F1A?style=for-the-badge&logo=databricks&logoColor=7C4DFF" alt="ChromaDB" />
  <img src="https://img.shields.io/badge/Gemini_API-0B0F1A?style=for-the-badge&logo=googlegemini&logoColor=00E5FF" alt="Gemini API" />
  <img src="https://img.shields.io/badge/OpenCV-0B0F1A?style=for-the-badge&logo=opencv&logoColor=5C3EE8" alt="OpenCV" />
</p>

<!-- Row 3: Data Analytics & Engineering -->
### Data Analytics & Engineering
<p>
  <img src="https://img.shields.io/badge/Pandas-0B0F1A?style=for-the-badge&logo=pandas&logoColor=150458" alt="Pandas" />
  <img src="https://img.shields.io/badge/NumPy-0B0F1A?style=for-the-badge&logo=numpy&logoColor=013243" alt="NumPy" />
  <img src="https://img.shields.io/badge/Matplotlib-0B0F1A?style=for-the-badge&logo=python&logoColor=00E5FF" alt="Matplotlib" />
  <img src="https://img.shields.io/badge/Power_BI-0B0F1A?style=for-the-badge&logo=powerbi&logoColor=F2C811" alt="Power BI" />
</p>

<!-- Row 4: Web & Deployment -->
### Web & Deployment
<p>
  <img src="https://img.shields.io/badge/React-0B0F1A?style=for-the-badge&logo=react&logoColor=61DAFB" alt="React" />
  <img src="https://img.shields.io/badge/Vite-0B0F1A?style=for-the-badge&logo=vite&logoColor=646CFF" alt="Vite" />
  <img src="https://img.shields.io/badge/Streamlit-0B0F1A?style=for-the-badge&logo=streamlit&logoColor=FF4B4B" alt="Streamlit" />
  <img src="https://img.shields.io/badge/FastAPI-0B0F1A?style=for-the-badge&logo=fastapi&logoColor=009688" alt="FastAPI" />
  <img src="https://img.shields.io/badge/Vercel-0B0F1A?style=for-the-badge&logo=vercel&logoColor=FFFFFF" alt="Vercel" />
  <img src="https://img.shields.io/badge/Render-0B0F1A?style=for-the-badge&logo=render&logoColor=46E3B7" alt="Render" />
</p>

<!-- Row 5: Developer Tools -->
### Developer Workflow
<p>
  <img src="https://img.shields.io/badge/Git-0B0F1A?style=for-the-badge&logo=git&logoColor=F05032" alt="Git" />
  <img src="https://img.shields.io/badge/GitHub-0B0F1A?style=for-the-badge&logo=github&logoColor=FFFFFF" alt="GitHub" />
  <img src="https://img.shields.io/badge/VS_Code-0B0F1A?style=for-the-badge&logo=visualstudiocode&logoColor=007ACC" alt="VS Code" />
  <img src="https://img.shields.io/badge/Obsidian-0B0F1A?style=for-the-badge&logo=obsidian&logoColor=7C3AED" alt="Obsidian" />
</p>

</div>

<br/>
<div align="center">
  <img src="assets/divider.svg" width="100%" alt="divider" />
</div>
<br/>

<!-- ================================================================= -->
<!-- 6. GITHUB STATS CARDS (CONSISTENT GLASS THEME)                    -->
<!-- ================================================================= -->
## 📊 Telemetry &amp; Activity

<div align="center">
  <!-- Note: Themed to #0B0F1A with Cyan & Violet accents to seamlessly blend with the glass background -->
  <!-- In case github-readme-stats is rate-limited by GitHub API, streak-stats acts as fallback -->
  <table>
    <tr>
      <td align="center">
        <img src="https://github-readme-stats.vercel.app/api?username=rohanpawar0006&show_icons=true&bg_color=0B0F1A&title_color=00E5FF&text_color=E2E8F0&icon_color=7C4DFF&border_color=1E293B&border_radius=12&hide_border=false" alt="Rohan's GitHub Stats" />
      </td>
      <td align="center">
        <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=rohanpawar0006&layout=compact&bg_color=0B0F1A&title_color=00E5FF&text_color=E2E8F0&border_color=1E293B&border_radius=12&hide_border=false" alt="Top Languages" />
      </td>
    </tr>
    <tr>
      <td colspan="2" align="center">
        <img src="https://streak-stats.demolab.com/?user=rohanpawar0006&theme=dark&background=0B0F1A&border=1E293B&stroke=7C4DFF&ring=00E5FF&fire=00E5FF&currStreakNum=00E5FF&sideNums=E2E8F0&sideLabels=94A3B8&dates=64748B&border_radius=12" alt="Streak Stats" />
      </td>
    </tr>
  </table>
</div>

<br/>
<div align="center">
  <img src="assets/divider.svg" width="100%" alt="divider" />
</div>
<br/>

<!-- ================================================================= -->
<!-- 7. CONTRIBUTION SNAKE                                             -->
<!-- ================================================================= -->
## 🐍 Contribution Velocity

<div align="center">
  <img src="https://raw.githubusercontent.com/rohanpawar0006/rohanpawar0006/output/github-contribution-grid-snake-dark.svg" alt="GitHub Contribution Snake" width="100%" />
</div>

<br/>
<div align="center">
  <img src="assets/divider.svg" width="100%" alt="divider" />
</div>
<br/>

<!-- ================================================================= -->
<!-- 8. CONNECT & OPPORTUNITY STATUS                                   -->
<!-- ================================================================= -->
## 🌐 Let's Build Together

<p align="center">
  <b>I am actively seeking AI/ML Engineer and Data Analyst Internships (Summer &amp; Fall 2026).</b><br/>
  <i>Have a team solving hard problems in AI, computer vision, or intelligent data workflows? Let's connect.</i>
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/rohan-pawar-bba78b290/">
    <img src="https://img.shields.io/badge/LinkedIn-0B0F1A?style=for-the-badge&logo=linkedin&logoColor=00E5FF&labelColor=0B0F1A" alt="LinkedIn" />
  </a>
  &nbsp;&nbsp;
  <a href="mailto:rohanpawar0006@gmail.com">
    <img src="https://img.shields.io/badge/Email-rohanpawar0006@gmail.com-0B0F1A?style=for-the-badge&logo=gmail&logoColor=7C4DFF&labelColor=0B0F1A" alt="Email" />
  </a>
  &nbsp;&nbsp;
  <a href="https://github.com/rohanpawar0006">
    <img src="https://img.shields.io/badge/GitHub-rohanpawar0006-0B0F1A?style=for-the-badge&logo=github&logoColor=00E5FF&labelColor=0B0F1A" alt="GitHub" />
  </a>
</p>

<br/>

<!-- ================================================================= -->
<!-- 9. FOOTER & VISITOR TELEMETRY                                     -->
<!-- ================================================================= -->
<div align="center">

  <a href="https://github.com/rohanpawar0006">
    <img src="https://komarev.com/ghpvc/?username=rohanpawar0006&label=PROFILE+VIEWS&style=for-the-badge&color=7C4DFF" alt="Profile views" />
  </a>

  <br/><br/>

  <img src="assets/footer.svg" width="100%" alt="Footer" />

</div>
