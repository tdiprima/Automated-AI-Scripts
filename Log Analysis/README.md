This GitHub repo is a **local AI-based log analyzer** using a custom Ollama model. Here's the breakdown of what it's doing and how to run it:

---

### 🧠 What's It Doing?

1. **Defines a custom Ollama model** called `log-analyzer` based on `llama3.2`:

   * The prompt file (`log_analyzer.txt`) sets up the system role as a *log analysis assistant*.

2. **Node.js script (`log_analyzer.js`) does the following**:

   * Reads a file called `server_logs.txt` (you'll need to create this).
   * Sends its content to a local Ollama instance running the `log-analyzer` model.
   * Parses the streamed JSON response to print an analysis of the logs.

---

### 🚀 How to Run It

#### 1. **Install Requirements**

Make sure Node.js is installed. Then install `axios`:

```bash
npm install axios
```

#### 2. **Start Ollama & Create the Model**

Make sure Ollama is installed and running, then run:

```bash
ollama create log-analyzer -f log_analyzer.txt
```

This registers your custom `log-analyzer` model using the prompt in `log_analyzer.txt`.

#### 3. **Prepare Your Logs**

Create a file called `server_logs.txt` with the logs you want analyzed. Example content:

```
[ERROR] DB connection failed: timeout after 5000ms
[INFO] Retrying connection...
[ERROR] DB connection failed: timeout after 5000ms
```

#### 4. **Run the Script**

Now just run:

```bash
node log_analyzer.js
```

It'll stream the analysis to your terminal.

---

### 🛠️ TL;DR

You're piping a log file into a local Ollama model with a structured prompt, getting back AI-generated diagnoses and fixes. It's a DIY AI log guru.

Let me know if you want help making this work with stdin, a web UI, or integrating into a broader toolchain.

---

<br>

## Log File

Absolutely. Here's a realistic and longer `server_logs.txt` that simulates a microservices web app under some strain. It mixes `INFO`, `WARN`, `ERROR`, and `DEBUG` level logs across different services (auth, API, DB, cache).

### 💡 Why this makes sense for AI analysis:

* **Recurring DB errors**: The AI should spot the timeouts and recommend DB failover or timeout tuning.
* **Auth issue**: Token signing failure might trigger a recommendation around JWT handling.
* **Performance warnings**: Memory pressure, slow queries, and cache evictions should all be flagged.
* **Good mix of noise vs signal**: Real logs include a lot of chatter—let the model separate signal from noise.

You can copy this into your `server_logs.txt` and run `node log_analyzer.js` to see what your local LLM thinks. Let me know if you want the logs themed for something else (IoT, mobile app, etc.).

<br>
