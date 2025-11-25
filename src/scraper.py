import logging
from typing import Optional
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def scrape_job_posting(url: str) -> Optional[str]:
    try:
        from firecrawl import Firecrawl
        
        api_key = os.getenv('FIRECRAWL_API_KEY')
        if not api_key:
            logger.error("FIRECRAWL_API_KEY not set")
            return None
        
        logger.info(f"Attempting to scrape: {url}")
        

        app = Firecrawl(api_key=api_key)
        
        result = app.scrape(url, formats=['markdown', 'html'])

        logger.info(f"Result type: {type(result)}")
        
        job_text = None
        
        if result:
            if hasattr(result, 'markdown') and result.markdown:
                job_text = result.markdown
                logger.info(f"Got markdown content: {len(job_text)} chars")
      
            if not job_text or len(job_text.strip()) < 50:
                if hasattr(result, 'html') and result.html:
                    from bs4 import BeautifulSoup
                    soup = BeautifulSoup(result.html, 'html.parser')
                    job_text = soup.get_text(separator='\n', strip=True)
                    logger.info(f"Converted HTML to text: {len(job_text)} chars")
                elif hasattr(result, 'content') and result.content:
                    job_text = result.content
                    logger.info(f"Got content field: {len(job_text)} chars")
        
        if not job_text:
            logger.error("No content extracted from result")
            return None
        
        lines = [line.strip() for line in job_text.splitlines() if line.strip()]
        cleaned_text = '\n'.join(lines)
        
        logger.info(f"Successfully scraped {len(cleaned_text)} characters")

        if len(cleaned_text) > 15000:
            cleaned_text = cleaned_text[:15000]
            logger.warning("Content truncated to 15000 characters")
        
        return cleaned_text
        
    except ImportError:
        logger.error("firecrawl-py not installed. Run: pip install firecrawl-py")
        return None
    except Exception as e:
        logger.error(f"Scraping error: {str(e)}")
        return None


def extract_text_from_manual_input(text: str) -> str:
    """
    Clean up manually pasted job description
    """
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    return '\n'