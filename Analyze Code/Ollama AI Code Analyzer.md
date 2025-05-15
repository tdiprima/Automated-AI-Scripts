This GitHub repo is setting up a **local AI code analysis tool** using [Ollama](https://ollama.com/) with a custom model and a couple of Node.js scripts to hit that model with different prompts.

### 🔍 What's it *doing*?

1. **Defines a custom AI model (`my-code-analyzer`)**:

   * Based on `llama3.2`
   * It's told to do:

     * 🔐 **Security checks**
     * 🛠️ **Refactoring suggestions**
     * 🧾 **Inline documentation**
   * Config defined in `modelfile.txt`.

2. **Has two client scripts that talk to this model**:

   * `analyze-with-codeqwen.js`: Uses a generic model called `codeqwen`.
   * `analyze-with-my-code-analyzer.js`: Uses your custom model `my-code-analyzer` defined in the modelfile.

3. **Both scripts** send code snippets to a local Ollama server (`http://localhost:11434/api/generate`) and stream the responses back to the terminal.

---

### 🚀 How to Run It

1. **Install Ollama** (if you haven't yet):
   [https://ollama.com/download](https://ollama.com/download)

2. **Set up your model**:

   ```bash
   ollama create my-code-analyzer -f modelfile.txt
   ```

3. **Install Node.js dependencies**:
   Make sure `axios` is available:

   ```bash
   npm install axios
   ```

4. **Run the script**:
   You can run either script, but `analyze-with-my-code-analyzer.js` is the one using your custom model:

   ```bash
   node analyze-with-my-code-analyzer.js
   ```

---

### 🧠 TL;DR

You're building a local AI-powered code review assistant using a fine-tuned Ollama model. You can feed it code, and it'll reply with vulnerability checks, refactors, or docs — depending on the task you pass in.

If you want to extend it: build a CLI around it or add a front-end UI, and you've got yourself a local Copilot clone.

Let me know if you want help making this repo more usable (like adding a README or turning it into an API or VSCode extension).

<br>
