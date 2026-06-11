# 🤖 Sistem RAG Lokal Sederhana

Proyek ini adalah implementasi *Retrieval-Augmented Generation* (RAG) secara lokal menggunakan Python. Aplikasi ini memungkinkan pengguna untuk bertanya kepada AI (LLM) mengenai isi dari sebuah dokumen teks spesifik. Aplikasi sepenuhnya berjalan secara *offline* di komputer lokal sehingga menjamin privasi data.

## 🛠️ Teknologi yang Digunakan
*   **[Ollama](https://ollama.com/):** Untuk menjalankan model AI secara lokal.
*   **Model LLM:** `llama3.2:1b` (ringan dan cepat).
*   **Model Embedding:** `nomic-embed-text` (mengubah teks ke vektor).
*   **[LangChain](https://python.langchain.com/):** Mengatur *pipeline* dokumen, *vector store*, dan LLM.
*   **FAISS:** *Database Vector* untuk pencarian berbasis semantik (berjalan di CPU).
*   **Streamlit:** Untuk membangun antarmuka web (UI) interaktif.

## 📋 Persyaratan Sistem
1. Python 3.9 atau lebih baru sudah terinstal.
2. Ollama sudah terinstal dan berjalan di latar belakang.

## 🚀 Cara Instalasi

**1. Unduh Model Ollama**
Buka terminal/command prompt dan jalankan perintah berikut untuk mengunduh model LLM dan Embeddings:
```bash
ollama pull llama3.2:1b
ollama pull nomic-embed-text
```

**2. Siapkan Lingkungan Python (Virtual Environment)**
Sangat disarankan menggunakan *virtual environment*.
```bash
python -m venv rag_env
# Aktivasi di MacOS/Linux:
source rag_env/bin/activate
# Aktivasi di Windows:
rag_env\Scripts\activate
```

**3. Install Dependencies**
```bash
pip install langchain langchain-community langchain-ollama faiss-cpu streamlit
```

## 📂 Struktur Direktori
Pastikan struktur file Anda terlihat seperti ini:
```text
/rag_project
 ├── app.py       # File utama berisi logika RAG dan antarmuka Streamlit
 ├── dokumen.txt     # File teks berisi data yang akan dibaca oleh AI
 ├── README.md      # Dokumentasi proyek
 └── /rag_env        # Folder virtual environment (jangan di-upload/commit)
```

## ▶️ Cara Menjalankan Aplikasi
1. Pastikan `dokumen.txt` sudah diisi dengan data teks yang relevan.
2. Buka terminal, pastikan virtual environment aktif.
3. Jalankan perintah berikut:
```bash
streamlit run app.py
```
4. Buka *browser* pada alamat lokal yang tertera di terminal (biasanya `http://localhost:8501`).