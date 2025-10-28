import streamlit as st
import json
import os
from datetime import datetime
import random
from difflib import SequenceMatcher
import hashlib
import base64

# Page Configuration
st.set_page_config(
    page_title="My Education Tube",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS Styling
st.markdown("""
<style>
    .video-card {
        background: #343434;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        transition: transform 0.2s;
    }
    .video-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    .notes-section {
        background: #fff3cd;
        padding: 15px;
        border-radius: 8px;
        border-left: 4px solid #ffc107;
        margin: 10px 0;
        color: #343434;
    }
    .search-box {
        font-size: 18px;
        padding: 10px;
    }
    .stat-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        margin: 10px 0;
    }
    .login-container {
        max-width: 400px;
        margin: 100px auto;
        padding: 40px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    }
    .login-title {
        color: white;
        text-align: center;
        font-size: 32px;
        margin-bottom: 30px;
    }
</style>
""", unsafe_allow_html=True)

# Data Files
DATA_FILE = "videos_data.json"
NOTES_FILE = "video_notes.json"

# =====================================================
# TRICKY PASSWORD AUTHENTICATION SYSTEM
# =====================================================

# Initialize session state for authentication
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "login_attempts" not in st.session_state:
    st.session_state.login_attempts = 0

# Confusing variable names and complex logic to hide the real password
def quantum_flux_capacitor(input_stream):
    """Don't try to understand this - it's quantum physics!"""
    temporal_matrix = [ord(c) for c in str(input_stream)]
    return temporal_matrix

def neural_network_processor(data_points):
    """AI-powered authentication algorithm"""
    synapse_weights = sum(data_points)
    return synapse_weights

def blockchain_validator(hash_value):
    """Distributed ledger verification"""
    merkle_root = hash_value % 997  # Prime number for security
    return merkle_root

def cryptographic_hash_generator(raw_input):
    """Military-grade encryption"""
    phase_1 = hashlib.sha256(str(raw_input).encode()).hexdigest()
    phase_2 = int(phase_1[:8], 16)
    phase_3 = phase_2 % 1000000
    return phase_3

def fibonacci_sequence_matcher(value):
    """Mathematical pattern recognition"""
    fib_series = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584]
    distance_metric = min([abs(value - fib) for fib in fib_series])
    return distance_metric

def reverse_entropy_calculator(numeric_data):
    """Thermodynamic password analysis"""
    entropy_level = sum([int(d) for d in str(numeric_data)])
    return entropy_level

def prime_factorization_engine(number):
    """Number theory cryptanalysis"""
    factors = []
    d = 2
    while d * d <= number:
        while number % d == 0:
            factors.append(d)
            number //= d
        d += 1
    if number > 1:
        factors.append(number)
    return sum(factors) if factors else 0

def astronomical_coordinate_system(input_val):
    """Celestial navigation authentication"""
    latitude = int(str(input_val)[:2]) if len(str(input_val)) >= 2 else 0
    longitude = int(str(input_val)[2:]) if len(str(input_val)) > 2 else 0
    return latitude, longitude

def dna_sequence_analyzer(code):
    """Genetic algorithm verification"""
    nucleotide_pairs = {'A': 1, 'T': 2, 'G': 3, 'C': 4}
    sequence = str(code).replace('0', 'A').replace('1', 'T').replace('2', 'G').replace('7', 'C')
    genetic_score = sum([nucleotide_pairs.get(n, 0) for n in sequence])
    return genetic_score

def machine_learning_predictor(features):
    """Deep learning classification model"""
    layer_1 = [f * 1.337 for f in features]
    layer_2 = sum(layer_1) / len(layer_1) if layer_1 else 0
    activation_function = int(layer_2 * 42) % 1000
    return activation_function

def validate_access_credentials(user_input):
    """
    Ultra-secure multi-layered authentication system
    Using advanced cryptographic algorithms and AI
    """
    # Phase 1: Quantum processing
    quantum_data = quantum_flux_capacitor(user_input)
    neural_output = neural_network_processor(quantum_data)
    
    # Phase 2: Blockchain validation
    blockchain_hash = blockchain_validator(neural_output)
    crypto_signature = cryptographic_hash_generator(user_input)
    
    # Phase 3: Pattern matching
    fibonacci_match = fibonacci_sequence_matcher(int(user_input) if user_input.isdigit() else 0)
    entropy_score = reverse_entropy_calculator(user_input)
    
    # Phase 4: Advanced cryptanalysis
    prime_sum = prime_factorization_engine(int(user_input) if user_input.isdigit() else 1)
    lat, lon = astronomical_coordinate_system(user_input)
    
    # Phase 5: Genetic verification
    dna_score = dna_sequence_analyzer(user_input)
    ml_prediction = machine_learning_predictor(quantum_data)
    
    # Phase 6: Multi-dimensional security matrix
    security_vector = [
        blockchain_hash,
        fibonacci_match,
        entropy_score,
        prime_sum,
        lat + lon,
        dna_score % 100,
        ml_prediction
    ]
    
    # Phase 7: Final authentication gate
    # The REAL password check (hidden in plain sight!)
    magic_number = lat * 100 + lon  # This is actually just the input number!
    
    # Decoy checks to confuse code readers
    if crypto_signature > 999999:
        magic_number -= 1
    if sum(security_vector) % 2 == 0:
        magic_number += 0
    if blockchain_hash < 500:
        magic_number *= 1
    
    # The actual password is 2710
    # lat = 27, lon = 10, so magic_number = 2710
    return magic_number == 2710

# =====================================================
# END OF TRICKY PASSWORD SYSTEM
# =====================================================

# Data Load/Save Functions
def load_data(filename):
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def save_data(filename, data):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def load_videos():
    data = load_data(DATA_FILE)
    return data if "categories" in data else {"categories": {}}

def load_notes():
    return load_data(NOTES_FILE)

# Extract YouTube Video ID
def extract_video_id(url):
    if "youtu.be/" in url:
        return url.split("youtu.be/")[1].split("?")[0]
    elif "youtube.com/watch?v=" in url:
        return url.split("v=")[1].split("&")[0]
    return None

# Search Score Calculation (fuzzy matching)
def calculate_search_score(query, text):
    query = query.lower()
    text = text.lower()
    
    # Exact match
    if query in text:
        return 100
    
    # SequenceMatcher score
    ratio = SequenceMatcher(None, query, text).ratio()
    
    # Word-based matching
    query_words = query.split()
    text_words = text.split()
    word_matches = sum(1 for word in query_words if word in text_words)
    word_score = (word_matches / len(query_words)) * 100 if query_words else 0
    
    # Combined score
    return max(ratio * 100, word_score)

# Search Function
def search_videos(query, videos_data, top_k=20):
    results = []
    
    for category, videos in videos_data["categories"].items():
        for video in videos:
            title_score = calculate_search_score(query, video["title"])
            desc_score = calculate_search_score(query, video.get("description", "")) * 0.5
            category_score = calculate_search_score(query, category) * 0.3
            
            total_score = title_score + desc_score + category_score
            
            if total_score > 20:  # Threshold
                results.append({
                    "video": video,
                    "category": category,
                    "score": total_score
                })
    
    results.sort(key=lambda x: x["score"], reverse=True)
    return results[:top_k]

# =====================================================
# LOGIN PAGE
# =====================================================

if not st.session_state.authenticated:
    st.markdown("""
    <div class="login-container">
        <div class="login-title">🔐 Education Tube</div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("### 🔑 Enter Access Code")
        
        password_input = st.text_input("Password:", type="password", key="password_field")
        
        col_btn1, col_btn2 = st.columns(2)
        with col_btn1:
            if st.button("🚀 Login", use_container_width=True):
                if validate_access_credentials(password_input):
                    st.session_state.authenticated = True
                    st.session_state.login_attempts = 0
                    st.success("✅ Authentication Successful!")
                    st.balloons()
                    st.rerun()
                else:
                    st.session_state.login_attempts += 1
                    st.error(f"❌ Invalid credentials! Attempt {st.session_state.login_attempts}")
        
        with col_btn2:
            if st.button("ℹ️ Help", use_container_width=True):
                st.info("Contact administrator for access code.")
        
        if st.session_state.login_attempts >= 3:
            st.warning("⚠️ Multiple failed attempts detected!")
    
    st.stop()  # Stop execution here if not authenticated

# =====================================================
# MAIN APPLICATION (After Authentication)
# =====================================================

# Session state initialization
if "current_video" not in st.session_state:
    st.session_state.current_video = None
if "show_video_page" not in st.session_state:
    st.session_state.show_video_page = False

# Sidebar
with st.sidebar:
    st.title("🎓 Education Tube")
    
    # Logout button
    if st.button("🚪 Logout"):
        st.session_state.authenticated = False
        st.rerun()
    
    st.markdown("---")
    
    page = st.radio("Navigation:", 
                    ["🏠 Home", "➕ Add Video", "📊 All Videos"],
                    label_visibility="collapsed")
    
    st.markdown("---")
    
    # Add Video Form
    if page == "➕ Add Video":
        st.subheader("Add New Video")
        
        with st.form("add_video_form"):
            category = st.text_input("📚 Category")
            video_title = st.text_input("📝 Video Title")
            video_url = st.text_input("🔗 YouTube Link")
            description = st.text_area("📄 Description")
            tags = st.text_input("🏷️ Tags (comma separated)")
            
            submit = st.form_submit_button("✅ Add Video")
            
            if submit:
                if category and video_title and video_url:
                    video_id = extract_video_id(video_url)
                    if video_id:
                        data = load_videos()
                        
                        if category not in data["categories"]:
                            data["categories"][category] = []
                        
                        data["categories"][category].append({
                            "title": video_title,
                            "url": video_url,
                            "video_id": video_id,
                            "description": description,
                            "tags": tags,
                            "added_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        })
                        
                        save_data(DATA_FILE, data)
                        st.success(f"✅ '{video_title}' added successfully!")
                        st.balloons()
                    else:
                        st.error("❌ Please provide a valid YouTube link!")
                else:
                    st.warning("⚠️ Category, Title and Link are required!")
    
    # Statistics
    data = load_videos()
    total_videos = sum(len(videos) for videos in data["categories"].values())
    total_categories = len(data["categories"])
    
    st.markdown("---")
    st.metric("📊 Total Videos", total_videos)
    st.metric("📚 Total Categories", total_categories)

# Main Content
data = load_videos()

# Home Page
if page == "🏠 Home" and not st.session_state.show_video_page:
    st.title("🏠 My Educational Video Platform")
    
    # Search Bar
    col1, col2 = st.columns([4, 1])
    with col1:
        search_query = st.text_input("🔍 Search videos...", 
                                      placeholder="Type video title, category or tags",
                                      key="search_box",
                                      label_visibility="collapsed")
    
    st.markdown("---")
    
    # Search Results
    if search_query:
        st.subheader(f"🔍 Search Results for: '{search_query}'")
        results = search_videos(search_query, data)
        
        if results:
            st.caption(f"Found {len(results)} result(s)")
            
            cols = st.columns(3)
            for idx, result in enumerate(results):
                with cols[idx % 3]:
                    video = result["video"]
                    category = result["category"]
                    score = result["score"]
                    
                    with st.container():
                        st.markdown(f"**{video['title']}**")
                        st.caption(f"📚 {category} | ⭐ {score:.1f}% match")
                        st.image(f"https://img.youtube.com/vi/{video['video_id']}/mqdefault.jpg", 
                                use_container_width=True)
                        
                        if st.button("▶️ Watch", key=f"search_{idx}"):
                            st.session_state.current_video = {
                                "video": video,
                                "category": category
                            }
                            st.session_state.show_video_page = True
                            st.rerun()
                        
                        st.markdown("---")
        else:
            st.info("😔 No results found. Try searching something else.")
    
    # Random Video Display
    else:
        st.subheader("🎲 Videos for You")
        
        if data["categories"]:
            # Collect all videos
            all_videos = []
            for cat, videos in data["categories"].items():
                for video in videos:
                    all_videos.append({"video": video, "category": cat})
            
            # Random shuffle
            random.shuffle(all_videos)
            
            # Display first 12
            display_videos = all_videos[:12]
            
            cols = st.columns(3)
            for idx, item in enumerate(display_videos):
                with cols[idx % 3]:
                    video = item["video"]
                    category = item["category"]
                    
                    with st.container():
                        st.markdown(f"**{video['title']}**")
                        st.caption(f"📚 {category}")
                        st.image(f"https://img.youtube.com/vi/{video['video_id']}/mqdefault.jpg", 
                                use_container_width=True)
                        
                        if st.button("▶️ Watch", key=f"home_{idx}"):
                            st.session_state.current_video = {
                                "video": video,
                                "category": category
                            }
                            st.session_state.show_video_page = True
                            st.rerun()
                        
                        st.markdown("---")
        else:
            st.info("📝 No videos added yet. Add videos from the sidebar.")

# Video Play Page (Separate Landing Page)
elif st.session_state.show_video_page and st.session_state.current_video:
    video = st.session_state.current_video["video"]
    category = st.session_state.current_video["category"]
    video_id = video["video_id"]
    
    # Back Button
    if st.button("⬅️ Back to Home"):
        st.session_state.show_video_page = False
        st.session_state.current_video = None
        st.rerun()
    
    st.markdown("---")
    
    # Video and Notes Side by Side
    col_video, col_notes = st.columns([2, 1])
    
    with col_video:
        st.title(video["title"])
        st.caption(f"📚 Category: {category}")
        
        # YouTube Video
        st.video(video["url"])
        
        if video.get("description"):
            with st.expander("📄 Description"):
                st.write(video["description"])
        
        if video.get("tags"):
            st.write(f"🏷️ **Tags:** {video['tags']}")
        
        st.caption(f"📅 Added on: {video['added_date']}")
    
    with col_notes:
        st.subheader("📝 My Notes")
        
        # Load Notes
        notes_data = load_notes()
        video_notes = notes_data.get(video_id, {"notes": []})
        
        # Add New Note
        with st.form(f"note_form_{video_id}"):
            new_note = st.text_area("Write a new note:", height=100)
            submit_note = st.form_submit_button("💾 Save Note")
            
            if submit_note and new_note:
                if video_id not in notes_data:
                    notes_data[video_id] = {"notes": [], "video_title": video["title"]}
                
                notes_data[video_id]["notes"].append({
                    "text": new_note,
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                })
                
                save_data(NOTES_FILE, notes_data)
                st.success("✅ Note saved!")
                st.rerun()
        
        st.markdown("---")
        
        # Display All Notes
        if video_notes["notes"]:
            st.subheader(f"📚 Total Notes: {len(video_notes['notes'])}")
            
            for idx, note in enumerate(reversed(video_notes["notes"])):
                with st.container():
                    st.markdown(f"""
                    <div class="notes-section">
                        <p style="margin: 0;">{note['text']}</p>
                        <p style="margin-top: 10px; font-size: 12px; color: #666;">
                            📅 {note['timestamp']}
                        </p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Delete Button
                    if st.button(f"🗑️ Delete", key=f"del_note_{idx}"):
                        notes_data[video_id]["notes"].pop(len(video_notes["notes"]) - 1 - idx)
                        save_data(NOTES_FILE, notes_data)
                        st.rerun()
        else:
            st.info("📝 No notes yet for this video.")

# All Videos Page
elif page == "📊 All Videos":
    st.title("📊 All Videos")
    
    if data["categories"]:
        # Category Filter
        categories = ["Show All"] + list(data["categories"].keys())
        selected_cat = st.selectbox("Filter by Category:", categories)
        
        st.markdown("---")
        
        for cat, videos in data["categories"].items():
            if selected_cat == "Show All" or selected_cat == cat:
                st.header(f"📚 {cat} ({len(videos)} videos)")
                
                cols = st.columns(3)
                for idx, video in enumerate(videos):
                    with cols[idx % 3]:
                        st.markdown(f"**{video['title']}**")
                        st.image(f"https://img.youtube.com/vi/{video['video_id']}/mqdefault.jpg",
                                use_container_width=True)
                        
                        col_btn1, col_btn2 = st.columns(2)
                        with col_btn1:
                            if st.button("▶️ Watch", key=f"all_{cat}_{idx}"):
                                st.session_state.current_video = {
                                    "video": video,
                                    "category": cat
                                }
                                st.session_state.show_video_page = True
                                st.rerun()
                        
                        with col_btn2:
                            if st.button("🗑️", key=f"del_{cat}_{idx}"):
                                data["categories"][cat].pop(idx)
                                if not data["categories"][cat]:
                                    del data["categories"][cat]
                                save_data(DATA_FILE, data)
                                st.rerun()
                        
                        st.markdown("---")
                
                st.markdown("<br>", unsafe_allow_html=True)
    else:
        st.info("📝 No videos added yet.")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray; padding: 20px;'>
    <p>🎓 <strong>My Education Tube</strong> | Advanced Educational Platform</p>
    <p style='font-size: 12px;'>Powered by Streamlit ❤️</p>
</div>
""", unsafe_allow_html=True)
