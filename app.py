import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
from src.core import process_cover_letter_request

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    st.error("GEMINI_API_KEY not found in .env file!")
    st.stop()

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-2.5-flash')


def main():
    st.set_page_config(
        page_title="AI Cover Letter Generator",
        page_icon="📝",
        layout="wide"
    )
    
    st.title("📝 AI Cover Letter Generator")
    st.markdown("Upload your resume and provide job details to generate a personalized cover letter")
    
    with st.sidebar:
        st.header("ℹ️ How to Use")
        st.markdown("""
        1. **Upload Resume**: Upload your resume in PDF format
        2. **Job Details**: Choose to either:
           - Paste the job URL (Indeed, Naukri, company sites)
           - Or manually paste the job description
        3. **Generate**: Click the button and wait
        4. **Download**: Copy or download your cover letter
        
        ---
        
        ### 💡 Tips
        - **URLs work for most sites** including LinkedIn, Indeed, Naukri
        - If URL fails, use the paste text option
        - Ensure your resume PDF is text-based (not scanned images)
        """)
        
        st.markdown("---")
        st.caption("Powered by Google Gemini 2.5 Flash")

    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("📄 Upload Resume")
        uploaded_file = st.file_uploader(
            "Choose your resume PDF",
            type=["pdf"],
            help="Upload a PDF version of your resume"
        )
    
    with col2:
        st.subheader("💼 Job Details")
        
        job_input_method = st.radio(
            "How would you like to provide job details?",
            ["Paste Job URL", "Paste Job Description Text"],
            help="URLs work for most job sites. Use text paste for LinkedIn or if URL doesn't work."
        )
        
        if job_input_method == "Paste Job URL":
            job_url = st.text_input(
                "Job Posting URL",
                placeholder="https://www.linkedin.com/jobs/view/... or Indeed/Naukri URL",
                help="Works with LinkedIn, Indeed, Naukri, and most job sites!"
            )
            job_text = None
            job_source = "url"
        else:
            job_text = st.text_area(
                "Job Description",
                placeholder="Paste the complete job description here...",
                height=200,
                help="Copy and paste the entire job posting text"
            )
            job_url = None
            job_source = "text"

    st.markdown("---")
    
    if st.button("✨ Generate Cover Letter", type="primary", use_container_width=True):
        
        if not uploaded_file:
            st.error("❌ Please upload your resume PDF")
            return
        
        if job_source == "url" and not job_url:
            st.error("❌ Please provide a job posting URL")
            return
        
        if job_source == "text" and not job_text:
            st.error("❌ Please paste the job description")
            return
 
        with st.spinner("🔄 Processing... This may take 30-60 seconds"):
            try:
                progress_container = st.container()
                
                with progress_container:
                    with st.status("Generating your cover letter...", expanded=True) as status:
                        st.write("📄 Reading your resume...")
                        st.write("💼 Analyzing job requirements...")
                        st.write("✍️ Crafting personalized cover letter...")
                        

                        cover_letter = process_cover_letter_request(
                            gemini_model=model,
                            pdf_file=uploaded_file,
                            job_source=job_source,
                            job_url=job_url,
                            job_text=job_text
                        )
                        
                        if cover_letter:
                            status.update(label="✅ Cover letter generated successfully!", state="complete")
                        else:
                            status.update(label="❌ Failed to generate cover letter", state="error")
                
                if cover_letter:
                    st.success("🎉 Your personalized cover letter is ready!")
                    
            
                    st.markdown("---")
                    
                    tab1, tab2 = st.tabs(["📄 Preview", "📋 Copy & Download"])
                    
                    with tab1:
                        st.markdown("### Your Cover Letter")
                        st.markdown(cover_letter)
                    
                    with tab2:
                        st.text_area(
                            "Copy your cover letter",
                            value=cover_letter,
                            height=400,
                            help="Click inside and press Ctrl+A then Ctrl+C to copy"
                        )
                        
                        col1, col2, col3 = st.columns([1, 1, 2])
                        
                        with col1:
                            st.download_button(
                                label="📥 Download as TXT",
                                data=cover_letter,
                                file_name="cover_letter.txt",
                                mime="text/plain",
                                use_container_width=True
                            )
                        
                        with col2:
                            # Optional: Add DOCX download if needed
                            st.info("💡 Tip: Copy to Word/Docs for formatting")
                else:
                    st.error("❌ Failed to generate cover letter. Please check the logs and try again.")
                    st.info("💡 Try using 'Paste Job Description Text' instead of URL if you're having issues.")
            
            except Exception as e:
                st.error(f"❌ An error occurred: {str(e)}")
                st.info("💡 Troubleshooting tips:")
                st.markdown("""
                - Try pasting the job description instead of using URL
                - Ensure your PDF is not password protected
                """)
   
    st.markdown("---")
    st.caption("Built with Streamlit❤️ • Powered by Google Gemini API")


if __name__ == "__main__":
    main()