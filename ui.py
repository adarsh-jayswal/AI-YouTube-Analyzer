import streamlit as st
import traceback
import re
from youtube_analyzer import build_youtube_agent

# ------------------------------------------------------------------------------
# Page Configuration
# ------------------------------------------------------------------------------
st.set_page_config(
    page_title="AI YouTube Analyzer",
    page_icon="🎥",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ------------------------------------------------------------------------------
# Editorial CSS - Pure Typography & Dividers (YouTube Red Accent)
# ------------------------------------------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    /* Target 1000px Content Width & Clean Spacing */
    .block-container {
        max-width: 1000px !important;
        padding-top: 2rem !important;
        padding-bottom: 3rem !important;
        padding-left: 1.5rem !important;
        padding-right: 1.5rem !important;
    }

    .stApp {
        background-color: #0B0B0F;
        color: #F5F5F5;
    }

    /* Hide default Streamlit header bar */
    header[data-testid="stHeader"] {
        background: transparent !important;
    }

    /* Top Navigation Bar */
    .nav-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding-bottom: 1rem;
        border-bottom: 1px solid rgba(255, 255, 255, 0.08);
        margin-bottom: 2.5rem;
    }

    .nav-brand {
        font-size: 1.1rem;
        font-weight: 700;
        color: #F5F5F5;
        display: flex;
        align-items: center;
        gap: 8px;
    }

    .nav-tech {
        font-size: 0.875rem;
        color: #A1A1AA;
        font-weight: 500;
    }

    /* Left-Aligned Editorial Hero */
    .hero-section {
        margin-bottom: 2.5rem;
    }

    .hero-eyebrow {
        font-size: 0.75rem;
        font-weight: 700;
        color: #FF0033;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        margin-bottom: 0.5rem;
    }

    .hero-title {
        font-size: 2.2rem;
        font-weight: 800;
        color: #F5F5F5;
        letter-spacing: -0.02em;
        line-height: 1.2;
        margin-bottom: 0.75rem;
    }

    .hero-sub {
        font-size: 1.05rem;
        color: #A1A1AA;
        line-height: 1.5;
        margin-bottom: 0.75rem;
        max-width: 680px;
    }

    .hero-powered {
        font-size: 0.85rem;
        color: #71717A;
    }

    /* Analyzer Area */
    .analyzer-section {
        margin-bottom: 2.5rem;
    }

    .analyzer-heading {
        font-size: 1.25rem;
        font-weight: 700;
        color: #F5F5F5;
        margin-bottom: 0.25rem;
    }

    .analyzer-sub {
        font-size: 0.9rem;
        color: #A1A1AA;
        margin-bottom: 1rem;
    }

    /* Inputs & Buttons - Side by Side */
    .stTextInput > label {
        display: none !important;
    }

    .stTextInput > div > div > input {
        background-color: #111116 !important;
        color: #F5F5F5 !important;
        border: 1px solid rgba(255, 255, 255, 0.12) !important;
        border-radius: 8px !important;
        padding: 0.75rem 1rem !important;
        font-size: 0.95rem !important;
    }

    .stTextInput > div > div > input:focus {
        border-color: #FF0033 !important;
        box-shadow: 0 0 0 2px rgba(255, 0, 51, 0.2) !important;
    }

    .stButton > button {
        width: 100% !important;
        background-color: #FF0033 !important;
        color: #FFFFFF !important;
        font-weight: 600 !important;
        font-size: 0.95rem !important;
        border-radius: 8px !important;
        border: none !important;
        padding: 0.75rem 1.25rem !important;
        transition: background-color 0.15s ease !important;
        cursor: pointer !important;
    }

    .stButton > button:hover {
        background-color: #E6002E !important;
    }

    /* Empty State */
    .empty-state {
        padding: 2.5rem 0;
        border-top: 1px solid rgba(255, 255, 255, 0.08);
        margin-top: 1rem;
    }

    .empty-title {
        font-size: 1.05rem;
        font-weight: 600;
        color: #F5F5F5;
        margin-bottom: 0.25rem;
        display: flex;
        align-items: center;
        gap: 8px;
    }

    .empty-sub {
        font-size: 0.875rem;
        color: #A1A1AA;
    }

    /* Results Document Layout */
    .results-section {
        margin-top: 2rem;
    }

    .results-main-title {
        font-size: 1.1rem;
        font-weight: 800;
        letter-spacing: 0.06em;
        text-transform: uppercase;
        color: #F5F5F5;
        padding-bottom: 0.75rem;
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 1.75rem;
    }

    .doc-section {
        margin-bottom: 2.25rem;
    }

    .doc-section-title {
        font-size: 1rem;
        font-weight: 700;
        letter-spacing: 0.04em;
        text-transform: uppercase;
        color: #F5F5F5;
        padding-bottom: 0.4rem;
        border-bottom: 1px solid rgba(255, 255, 255, 0.06);
        margin-bottom: 1rem;
    }

    .doc-section-content {
        font-size: 0.95rem;
        color: #D4D4D8;
        line-height: 1.6;
    }

    /* Timeline Monospace Timestamps */
    .ts-mono {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.875rem;
        font-weight: 600;
        color: #FF0033;
        display: inline-block;
        margin-right: 8px;
    }

    /* Alerts */
    .alert-warn {
        background: rgba(245, 158, 11, 0.08);
        border-left: 3px solid #F59E0B;
        color: #FDE047;
        padding: 0.75rem 1rem;
        font-size: 0.9rem;
        margin-bottom: 1.25rem;
    }

    .alert-err {
        background: rgba(239, 68, 68, 0.08);
        border-left: 3px solid #EF4444;
        color: #FCA5A5;
        padding: 0.75rem 1rem;
        font-size: 0.9rem;
        margin-bottom: 1.25rem;
    }

    /* Footer */
    .footer-section {
        text-align: center;
        padding-top: 1.75rem;
        margin-top: 4rem;
        border-top: 1px solid rgba(255, 255, 255, 0.08);
        color: #71717A;
        font-size: 0.825rem;
    }
</style>
""", unsafe_allow_html=True)


# ------------------------------------------------------------------------------
# Agent Cache Initialization
# ------------------------------------------------------------------------------
@st.cache_resource
def get_agent():
    return build_youtube_agent()

agent = get_agent()


# ------------------------------------------------------------------------------
# Header & Hero Renderers
# ------------------------------------------------------------------------------
def render_header():
    st.markdown("""
    <div class="nav-bar">
        <div class="nav-brand">🎥 AI YouTube Analyzer</div>
        <div class="nav-tech">Agno · Gemini</div>
    </div>
    """, unsafe_allow_html=True)


def render_hero():
    st.markdown("""
    <div class="hero-section">
        <div class="hero-eyebrow">AI VIDEO ANALYZER</div>
        <div class="hero-title">Turn YouTube Videos Into Useful Insights.</div>
        <div class="hero-sub">Paste a video link. Get the important ideas, key moments and takeaways in seconds.</div>
        <div class="hero-powered">Powered by Agno + Gemini</div>
    </div>
    """, unsafe_allow_html=True)


def render_empty_state():
    st.markdown("""
    <div class="empty-state">
        <div class="empty-title">🎬 Ready to analyze</div>
        <div class="empty-sub">Paste a YouTube video above to get started.</div>
    </div>
    """, unsafe_allow_html=True)


def render_footer():
    st.markdown("""
    <div class="footer-section">
        AI YouTube Analyzer &bull; Built with Streamlit &middot; Agno &middot; Gemini
    </div>
    """, unsafe_allow_html=True)


# ------------------------------------------------------------------------------
# Editorial Document Results Parser
# ------------------------------------------------------------------------------
def render_results(content: str):
    st.markdown("""
    <div class="results-section">
        <div class="results-main-title">VIDEO ANALYSIS</div>
    </div>
    """, unsafe_allow_html=True)

    # Split markdown by headings
    sections = re.split(r'\n(?=#{1,3}\s+)', content)

    if len(sections) <= 1:
        st.markdown('<div class="doc-section"><div class="doc-section-content">', unsafe_allow_html=True)
        st.markdown(content)
        st.markdown('</div></div>', unsafe_allow_html=True)
        return

    for section in sections:
        section = section.strip()
        if not section:
            continue

        first_line = section.split('\n')[0]
        header_title = re.sub(r'^#{1,3}\s+', '', first_line).strip()
        body = '\n'.join(section.split('\n')[1:]).strip()

        st.markdown('<div class="doc-section">', unsafe_allow_html=True)
        st.markdown(f'<div class="doc-section-title">{header_title}</div>', unsafe_allow_html=True)
        st.markdown('<div class="doc-section-content">', unsafe_allow_html=True)
        
        if body:
            st.markdown(body)
            
        st.markdown('</div></div>', unsafe_allow_html=True)


# ------------------------------------------------------------------------------
# Main Application Flow
# ------------------------------------------------------------------------------
render_header()
render_hero()

# Analyzer Section Header
st.markdown("""
<div class="analyzer-section">
    <div class="analyzer-heading">Analyze a video</div>
    <div class="analyzer-sub">Paste a public YouTube URL below.</div>
</div>
""", unsafe_allow_html=True)

# Side-by-side desktop layout for input and button
col_input, col_btn = st.columns([3.5, 1])

with col_input:
    video_url = st.text_input(
        label="YouTube Video URL",
        placeholder="https://www.youtube.com/watch?v=...",
        key="youtube_url_input"
    )

with col_btn:
    button = st.button("▶ Analyze")

# Execution & State Handling
if button:
    if not video_url or not video_url.strip():
        st.markdown(
            '<div class="alert-warn">Please enter a YouTube video URL.</div>',
            unsafe_allow_html=True
        )
        render_empty_state()
    else:
        try:
            with st.spinner("Analyzing video..."):
                response = agent.run(f"Analyze this video: {video_url.strip()}")

            if hasattr(response, 'content') and response.content:
                render_results(response.content)
            else:
                st.markdown(
                    '<div class="alert-warn">Unable to analyze this video. Please check the URL and try again.</div>',
                    unsafe_allow_html=True
                )
        except Exception as e:
            traceback.print_exc()
            st.markdown(
                '<div class="alert-err">Unable to analyze this video. Please check the URL and try again.</div>',
                unsafe_allow_html=True
            )
else:
    render_empty_state()

render_footer()