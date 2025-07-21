# Ollama Structured Output Demo

A demonstration playground for generating **structured, deterministic JSON outputs** from Ollama's local LLMs using schema validation with Pydantic (Python) and Zod (JavaScript).

## Overview

This repository showcases how to extract structured data from natural language prompts and images using Ollama's local LLMs with enforced JSON schemas. All examples work with locally-hosted models like `llama3.2` and `llama3.2-vision`.

## Prerequisites

- **Ollama** server running locally at `http://localhost:11434`
- **Models**: `llama3.2`, `llama3.2-vision`, `llama3.1`
- **Python dependencies**: `ollama`, `pydantic`
- **Node.js dependencies**: `ollama`, `zod`, `zod-to-json-schema`

### Setup

#### Ollama Models
```bash
ollama pull llama3.2
ollama pull llama3.2-vision
ollama pull llama3.1
```

#### Python Dependencies
```bash
pip install ollama pydantic
```

#### Node.js Dependencies
```bash
npm install
```

## Scripts Overview

### Vision Analysis
- **`llama_vision.py`** - Analyzes images (`beach.jpg`) using `llama3.2-vision` to extract structured information including objects, scene description, colors, and time of day. Uses Pydantic for response validation.

### Text-to-JSON Extraction
- **`extract_data_with_schema.py`** - Python implementation using Pydantic schema validation to extract friend information from natural language
- **`extract_data_with_schema.js`** - JavaScript equivalent with basic JSON parsing
- **`Canada.js`** - Uses Zod schema validation to extract country information about Canada

### Pet Information Extraction
- **`structured_pet_info1.py`** - Pure Ollama + Pydantic approach for extracting pet details
- **`structured_pet_info.py`** - Alternative implementation using OpenAI-compatible client interface

### Simple Examples
- **`structured_output_demo.py`** - Basic book information extraction without strict schema validation
- **`testing.py`** - Simple hello-world test to verify Ollama connectivity

## Usage Examples

### Python
```bash
python llama_vision.py
python extract_data_with_schema.py
python structured_pet_info1.py
```

### JavaScript
```bash
node Canada.js
node extract_data_with_schema.js
```

## Key Features

- **Schema Validation**: Ensures consistent, predictable JSON outputs
- **Multi-modal**: Text and image processing capabilities
- **Local Deployment**: No external API dependencies
- **Deterministic Outputs**: Temperature settings for consistent results
- **Error Handling**: Robust parsing and validation workflows

## Architecture

The demos demonstrate two main approaches:

1. **Direct Ollama API** - Using the native ollama library with schema formatting
2. **OpenAI-Compatible Interface** - Using OpenAI client syntax with local Ollama backend

All examples emphasize practical applications of structured output generation for data extraction, content analysis, and information processing tasks.

<br>
