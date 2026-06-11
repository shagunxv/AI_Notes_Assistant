def chunk_text(text, chunk_size=1000):
    """Split long text into chunks"""

    word=text.split()
    chunks=[]
    for i in range(0, len(word),chunk_size):
        chunk=" ".join(word[i:i+chunk_size])
        chunks.append(chunk)
    return chunks