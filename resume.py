# Importing Required Libraries
import streamlit as st
import PyPDF2
import re

# Function to Extract Text from PDF
def read_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for i in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[i]
        text += page.extract_text()
    return text

# Function to Parse Resume Sections
def parse_section(text, keyword):
    keyword = keyword.lower()
    text = text.lower()
    try:
        section = re.search(f"{keyword}:(.*)", text).group(1)
        return section.strip().split("\n")[0]
    except:
        return "Not found"

# Streamlit App
st.title("Resume Parser")

uploaded_file = st.file_uploader("Upload your Resume in PDF", type="pdf")

if uploaded_file is not None:
    # Extract Text from PDF
    extracted_text = read_pdf(uploaded_file)

    # Display Text
    st.write("### Extracted Resume Text:")
    st.write(extracted_text)

    st.write("### Parsed Information:")

    # Parse and Display Information
    st.write("Education: ", parse_section(extracted_text, "Education"))
    st.write("Experience: ", parse_section(extracted_text, "Experience"))
    st.write("Skills: ", parse_section(extracted_text, "Skills"))
