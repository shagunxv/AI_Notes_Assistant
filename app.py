import streamlit as st
from codess.pdf import extract_pdf
from codess.chunks import chunk_text
from codess.summarize import generate_summary
st.set_page_config(page_title="AI Notes Assistant", layout="wide")
st.title("📚 AI Notes Assistant")
upload=st.file_uploader("Upload your PDF notes here(No image should be inside PDF.)", type=["pdf"])
if upload:
    with st.spinner("Reading PDF..."):
        try:
            text = extract_pdf(upload)

        except ValueError as e:
            st.error(str(e))
            st.stop()
        if not text.strip():
            st.warning(
                "No readable text was found in this PDF. "
                "Please upload a text-based PDF."
            )
            st.stop()
    st.metric("Characters extracted", f"{len(text):,}")
    st.success("PDF extracted successfully!")
    st.subheader("Preview")
    st.write(text[:1000])
    if st.button("Generate Summary"):

        try:
            with st.spinner("Generating summary..."):
                chunks = chunk_text(text)
                summary = generate_summary(chunks)

            st.subheader("📝 Summary")
            st.markdown(summary)
            st.download_button(label="Download", data = summary, file_name="AI_NotesSummary.txt",mime="text/plain")

        except Exception:
            st.error(
                "Unable to generate the summary. Please try again."
            )