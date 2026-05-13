import streamlit as st
import json
import os
from datetime import datetime

NOTES_FILE = os.path.join(os.path.dirname(__file__), "notes_data.json")

def _load_notes():
    if os.path.exists(NOTES_FILE):
        try:
            with open(NOTES_FILE, "r") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}

def _save_notes(notes):
    try:
        with open(NOTES_FILE, "w") as f:
            json.dump(notes, f, indent=2)
    except Exception:
        pass

def render_section_notes(section_id, section_label="this section"):
    if "all_notes" not in st.session_state:
        st.session_state.all_notes = _load_notes()

    notes = st.session_state.all_notes
    section_notes = notes.get(section_id, [])

    with st.expander(f"📝 Notes & Edits — {section_label} ({len(section_notes)} notes)", expanded=False):
        if section_notes:
            for i, note in enumerate(section_notes):
                col_note, col_del = st.columns([10, 1])
                with col_note:
                    st.markdown(f"**{note.get('author', 'Team')}** · {note.get('timestamp', '')}")
                    st.info(note.get("text", ""))
                with col_del:
                    if st.button("🗑️", key=f"del_{section_id}_{i}"):
                        section_notes.pop(i)
                        notes[section_id] = section_notes
                        st.session_state.all_notes = notes
                        _save_notes(notes)
                        st.rerun()
        else:
            st.caption("No notes yet. Add one below.")

        with st.form(key=f"form_{section_id}", clear_on_submit=True):
            col_author, col_text = st.columns([1, 3])
            with col_author:
                author = st.text_input("Your name", value="Kala", key=f"author_{section_id}")
            with col_text:
                new_note = st.text_area("Add a note, edit suggestion, or comment", key=f"note_{section_id}", height=80, placeholder="e.g., 'Update the numbers to reflect latest finance review...'")
            submitted = st.form_submit_button("💾 Save Note")
            if submitted and new_note.strip():
                entry = {
                    "author": author,
                    "text": new_note.strip(),
                    "timestamp": datetime.now().strftime("%b %d, %Y %I:%M %p")
                }
                section_notes.append(entry)
                notes[section_id] = section_notes
                st.session_state.all_notes = notes
                _save_notes(notes)
                st.rerun()
