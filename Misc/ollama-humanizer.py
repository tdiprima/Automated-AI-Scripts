#!/usr/bin/env python3
"""
File Humanizer Script
Reads various file formats and uses Ollama to rewrite them in a more human style.

# Basic usage with a text file
python humanizer.py document.txt

# Use a different model
python humanizer.py document.md -m mistral

# Save output to a file
python humanizer.py report.docx -o humanized_report.txt

# Use a custom Ollama host
python humanizer.py file.txt -H http://192.168.1.100:11434
"""

import sys
import os
import argparse
import requests
import json
from pathlib import Path

# Optional imports for docx support
try:
    from docx import Document
    DOCX_SUPPORT = True
except ImportError:
    DOCX_SUPPORT = False
    print("Warning: python-docx not installed. Install with 'pip install python-docx' for .docx support")


def read_file(filepath):
    """Read content from various file formats."""
    file_path = Path(filepath)
    
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {filepath}")
    
    # Get file extension
    ext = file_path.suffix.lower()
    
    try:
        if ext == '.docx':
            if not DOCX_SUPPORT:
                raise ValueError("python-docx is required for .docx files. Install with: pip install python-docx")
            return read_docx(filepath)
        elif ext in ['.txt', '.md', '.markdown']:
            return read_text(filepath)
        else:
            # Try to read as text for unknown extensions
            return read_text(filepath)
    except Exception as e:
        raise Exception(f"Error reading file: {str(e)}")


def read_text(filepath):
    """Read plain text or markdown file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()


def read_docx(filepath):
    """Read content from a .docx file."""
    doc = Document(filepath)
    full_text = []
    for paragraph in doc.paragraphs:
        if paragraph.text.strip():
            full_text.append(paragraph.text)
    return '\n'.join(full_text)


def call_ollama(content, model='llama3.2', host='http://localhost:11434'):
    """Send content to Ollama for humanization."""
    prompt = f"Write this like a human:\n\n{content}"
    
    try:
        response = requests.post(
            f"{host}/api/generate",
            json={
                "model": model,
                "prompt": prompt,
                "stream": False
            },
            timeout=60
        )
        response.raise_for_status()
        
        result = response.json()
        return result.get('response', '')
    
    except requests.exceptions.ConnectionError:
        raise Exception(f"Could not connect to Ollama at {host}. Make sure Ollama is running.")
    except requests.exceptions.Timeout:
        raise Exception("Request to Ollama timed out. The text might be too long.")
    except Exception as e:
        raise Exception(f"Error calling Ollama: {str(e)}")


def main():
    parser = argparse.ArgumentParser(description='Humanize text files using Ollama')
    parser.add_argument('file', help='Path to the file to humanize')
    parser.add_argument('-m', '--model', default='llama3.2', help='Ollama model to use (default: llama3.2)')
    parser.add_argument('-H', '--host', default='http://localhost:11434', help='Ollama host URL (default: http://localhost:11434)')
    parser.add_argument('-o', '--output', help='Output file path (optional)')
    
    args = parser.parse_args()
    
    try:
        # Read the file
        print(f"Reading file: {args.file}")
        content = read_file(args.file)
        
        if not content.strip():
            print("Error: File is empty or contains only whitespace")
            sys.exit(1)
        
        # Call Ollama
        print(f"Sending to Ollama ({args.model})...")
        humanized = call_ollama(content, model=args.model, host=args.host)
        
        if not humanized:
            print("Error: Ollama returned empty response")
            sys.exit(1)
        
        # Output results
        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(humanized)
            print(f"\nHumanized text saved to: {args.output}")
        else:
            print("\n--- Humanized Text ---\n")
            print(humanized)
            print("\n--- End ---")
    
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
