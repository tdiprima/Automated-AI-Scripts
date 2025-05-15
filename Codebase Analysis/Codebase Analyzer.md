This repo is a local AI-powered **codebase analyzer**. It's designed to recursively scan a directory of code files, send them to a local language model (via Ollama), and get back summaries or answers about each code segment. Here's what it does and how to run it:

---

### 🚀 What it Does

1. **Scans a directory** for `.js`, `.py`, or `.java` files.
2. **Reads and sends** each file's code to a local Ollama model called `codebase-analyzer`.
3. **Asks a question** like: “What dependencies does this code use?”
4. **Prints the model's analysis** to the console.

---

### 🧠 What's Powering It

* It hits `http://localhost:11434/api/generate`, which is the Ollama API.
* It's using a **custom model** named `codebase-analyzer`, which you create with:

```bash
ollama create codebase-analyzer -f codebase_analyzer.txt
```

That `.txt` defines the model's role as a code analysis assistant.

---

### 🛠️ How to Run It

1. **Install Ollama** and make sure it's running locally.

   * [https://ollama.com](https://ollama.com)

2. **Create the custom model**:

```bash
ollama create codebase-analyzer -f codebase_analyzer.txt
```

3. **Update the script**:
   In `codebase_analyzer.js`, replace this line:

   ```js
   const codebaseDirectory = './path_to_codebase';
   ```

   with the actual path to the code you want to analyze.

4. **Run the script**:

   ```bash
   node codebase_analyzer.js
   ```

---

### 🧪 Example Output

You'll see something like:

```
Analyzing ./myproject/index.js...
Analysis Result:
This file sets up an Express server and depends on express and cors. It defines routes for user login.
```

---

Let me know if you want a CLI wrapper, directory ignore support (`.git`, `node_modules`), or a version that writes the output to a markdown report.

<br>
