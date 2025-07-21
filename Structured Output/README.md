This repo is a **demo playground for structured output using Ollama's LLMs (like `llama3.2` and `llama3.2-vision`)**, focused on getting **deterministic, JSON-formatted responses** out of natural language using schema validation (Pydantic or Zod).

### 🧠 Core Idea:

Use Ollama + schema definition (Pydantic for Python, Zod for JS) to extract **structured data** from natural language or images.

---

### 🔧 What Each Script Does:

#### 📸 `llama_vision.py`

* Uses `llama3.2-vision` to analyze `beach.jpg`.
* Returns structured info like objects, scene, colors, time of day, etc.
* Uses **Pydantic** to validate the response structure.

#### 💬 `extract_data_with_schema.py` / `extract_data_with_schema.js`

* Input: "I have two friends..."
* Output: JSON list of friends with `name`, `age`, `is_available`.
* JS uses a plain JSON parser.
* Python uses **Pydantic** for strict schema enforcement.

#### 🇨🇦 `Canada.js`

* Uses **Zod + `zod-to-json-schema`** to define a country schema.
* Sends a prompt ("Tell me about Canada.") and validates the response.

#### 🐾 `structured_pet_info.py` / `structured_pet_info1.py`

* Same prompt about pets (Luna and Loki).
* Two versions:

  * `structured_pet_info.py`: Tries to use OpenAI client with local Llama.
  * `structured_pet_info1.py`: Pure Ollama + Pydantic.

#### 📚 `structured_output_demo.py`

* Pulls out title, author, and publication year from a book description.
* Simple JSON response extraction with no schema validation.

#### 👋 `testing.py`

* Just a hello-world ping to the LLM.

---

### ▶️ How to Run It:

#### 🔁 Dependencies

You'll need:

* Python: `ollama`, `pydantic`
* Node.js: `ollama`, `zod`, `zod-to-json-schema`
* Ollama server running locally at `http://localhost:11434` with models pulled (`llama3.2`, `llama3.2-vision`)

##### Python Setup

```bash
pip install ollama pydantic
```

##### JS Setup

```bash
npm install
```

#### 🧪 To Run:

Pick any script and run:

**Python:**

```bash
python llama_vision.py
# or
python extract_data_with_schema.py
```

**JavaScript:**

```bash
node Canada.js
# or
node extract_data_with_schema.js
```

---

### 🚨 Heads Up:

* Make sure `ollama` is running and you've pulled the models:

  ```bash
  ollama run llama3.2
  ollama run llama3.2-vision
  ```

* If you're using `structured_pet_info.py`, the OpenAI-style client needs proper setup or can be skipped in favor of the simpler `structured_pet_info1.py`.

---

### TL;DR:
You're building an Ollama-powered LLM playground that enforces structured outputs from text and images using schemas. Run locally, test prompts, get clean JSON back. Super helpful for apps that need reliable, formatted data from fuzzy input.

<br>
