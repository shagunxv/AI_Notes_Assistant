import streamlit as st
from codess.pdf import extract_pdf
from codess.chunks import chunk_text
from codess.summarize import generate_summary
st.set_page_config(page_title="AI Notes Assistant", layout="wide")
st.title("📚 AI Notes Assistant")
upload=st.file_uploader("Upload your PDF notes here(No image should be inside PDF.)", type=["pdf"])
if upload:
    with st.spinner("Reading PDF..."):
        text=extract_pdf(upload)
        st.write("Characters extracted:", len(text))
        # st.write(text[:1000])
    st.success("PDF extracted successfully!")
    st.subheader("Preview")
    st.write(text[:1000])
    if st.button("Generate Summary"):
        with st.spinner("Generating summary..."):
            chunks=chunk_text(text)
            summary=generate_summary(chunks)

        st.subheader("Summary")
        st.write(summary)