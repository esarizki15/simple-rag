import streamlit as st
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings, OllamaLLM
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
import warnings
warnings.filterwarnings("ignore")

# Gunakan cache agar database & model tidak di-reload setiap kali user mengetik/menekan tombol
@st.cache_resource
def inisialisasi_rag():
    # 1. Memuat dokumen
    loader = TextLoader("dokumen.txt")
    docs = loader.load()

    # 2. Memecah teks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    splits = text_splitter.split_documents(docs)

    # 3. Membuat Vector Store
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    vectorstore = FAISS.from_documents(documents=splits, embedding=embeddings)

    # 4. Menyiapkan LLM
    llm = OllamaLLM(model="llama3.2:1b", temperature=0.1)

    # 5. Membuat Prompt Template Bahasa Indonesia
    template_indo = """Gunakan potongan informasi berikut untuk menjawab pertanyaan di akhir. 
    Jika kamu tidak tahu jawabannya berdasarkan informasi ini, katakan saja bahwa kamu tidak tahu, jangan mencoba mengarang jawaban.

    Konteks: {context}

    Pertanyaan: {question}
    Jawaban:"""
    
    QA_CHAIN_PROMPT = PromptTemplate.from_template(template_indo)

    # 6. Membangun Chain RAG
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vectorstore.as_retriever(search_kwargs={"k": 2}),
        chain_type_kwargs={"prompt": QA_CHAIN_PROMPT}
    )
    return qa_chain

# Konfigurasi Halaman Web Streamlit
st.set_page_config(page_title="Tugas RAG Lokal", page_icon="🤖", layout="centered")

st.title("🤖 Sistem RAG Lokal Sederhana")
st.caption("Dibuat menggunakan Python, Streamlit, LangChain, FAISS, dan Ollama")
st.write("---")

try:
    # Memanggil fungsi RAG dengan animasi loading
    with st.spinner("Sedang memuat dokumen dan menyiapkan model AI (proses ini hanya berjalan sekali)..."):
        qa_chain = inisialisasi_rag()
    
    # Form Input Pertanyaan
    pertanyaan = st.text_input(
        "Tanyakan sesuatu tentang dokumen.txt:",
        placeholder="Contoh: Kapan Fakultas Ilmu Komputer didirikan dan apa nama gedungnya?"
    )

    # Jika user menekan Enter atau mengisi teks
    if pertanyaan:
        with st.spinner("AI sedang berpikir mencari jawaban di dokumen..."):
            hasil = qa_chain.invoke(pertanyaan)
            
            # Menampilkan hasil jawaban
            st.markdown("### 📝 Jawaban AI:")
            st.success(hasil['result'])

except Exception as e:
    st.error(f"Terjadi kesalahan: {e}")
    st.info("Tips: Pastikan aplikasi Ollama sudah aktif di komputer Anda dan dokumen.txt sudah ada di folder yang sama.")