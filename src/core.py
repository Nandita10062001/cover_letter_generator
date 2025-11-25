from typing import Optional
import logging
import PyPDF2
import google.generativeai as genai
from src.scraper import scrape_job_posting, extract_text_from_manual_input

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def extract_pdf_text(pdf_file) -> Optional[str]:
    try:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        pdf_text = ""
        
        for page in pdf_reader.pages:
            pdf_text += page.extract_text() + "\n"
        
        logger.info(f"Extracted PDF text length: {len(pdf_text)}")
        return pdf_text.strip()
    
    except Exception as e:
        logger.error(f"Error extracting PDF text: {str(e)}")
        return None


def generate_cover_letter_with_gemini(
    model: genai.GenerativeModel,
    resume_text: str,
    job_description: str
) -> Optional[str]:
    """
    Single API call
    """
    try:
        prompt = f"""You are a professional looking for a job in the current job market. Generate a professional, compelling and genuinely human cover letter that follows these guidelines:
RESUME:
{resume_text}

JOB DESCRIPTION:
{job_description}

INSTRUCTIONS:
Write a cover letter that feels natural, warm, and genuinely written by a real person. Avoid overly formal language, dramatic phrasing, or heavy jargon. The goal is a clear, sincere, and confident letter that shows personality without losing professionalism.

Follow these guidelines:
1. Start with a strong but simple and sincere opening that shows real enthusiasm for the role and company (take from the job posting strictly).
2. Highlight 2–3 relevant experiences from my background, but explain them in a grounded, human way — not like bullet points or corporate jargon.
3. Use specific metrics or achievements only where they add clarity, and weave them naturally into the story.
4. Show a thoughtful understanding of the company/role based on the job description, but keep the tone conversational instead of formal.
5. Keep the letter concise (300–400 words).
6. End with a warm, confident call to action that sounds like something a real person would say.
7. Maintain a professional but friendly tone — avoid grand words like “profound,” “leveraging,” “transformative,” “cutting-edge,” “mission-driven,” etc.
8. DO NOT include placeholder text like [Your Name], [Date], or [Address].
9. Start directly with the greeting and end with “Sincerely,” followed by a blank line.
10. Most importantly: Make it feel human. It should read smoothly, simply, and authentically — like a motivated person explaining why they’re excited to join the team.
11. Generate ONLY the cover letter content, no additional commentary."""

        logger.info("Generating your cover letter...")
        
        response = model.generate_content(prompt)
        cover_letter = response.text.strip()
        
        logger.info(f"Generated cover letter length: {len(cover_letter)}")
        return cover_letter
    
    except Exception as e:
        logger.error(f"Error generating cover letter: {str(e)}")
        return None


def process_cover_letter_request(
    gemini_model: genai.GenerativeModel,
    pdf_file,
    job_source: str,
    job_url: Optional[str] = None,
    job_text: Optional[str] = None
) -> Optional[str]:
    """
    Main function
    """
    try:
        # Extract resume text
        logger.info("Step 1: Extracting resume text...")
        resume_text = extract_pdf_text(pdf_file)
        
        if not resume_text:
            logger.error("Failed to extract resume text")
            return None
        
        # Get job description
        logger.info("Step 2: Getting job description...")
        if job_source == 'url' and job_url:
            job_description = scrape_job_posting(job_url)
        elif job_source == 'text' and job_text:
            job_description = extract_text_from_manual_input(job_text)
        else:
            logger.error("No valid job source provided")
            return None
        
        if not job_description:
            logger.error("Failed to get job description")
            return None
        
        logger.info("Step 3: Generating cover letter")
        cover_letter = generate_cover_letter_with_gemini(
            gemini_model,
            resume_text,
            job_description
        )
        
        if not cover_letter:
            logger.error("Failed to generate cover letter")
            return None
        
        logger.info("Cover letter generated successfully!")
        return cover_letter
    
    except Exception as e:
        logger.error(f"Error in process_cover_letter_request: {str(e)}")
        return None