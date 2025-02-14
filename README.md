Here’s a **README.md** file explaining how to set up and use the script with **Miniconda**. It includes step-by-step instructions for installing dependencies, configuring the environment, and running the script.  

---

### 📄 **README.md**

```markdown
# 🎙️ ElevenLabs Text-to-Speech Script

This Python script reads a text file (`script.txt`), splits it into sections using `####` as a delimiter, and converts each section into an MP3 file using the **ElevenLabs** API. Optionally, it can merge all generated audio files into a single high-quality MP3 file.

---

## 🚀 **Setup Instructions Using Miniconda**
This guide assumes you're using **Windows** and have **Miniconda** installed. If not, download and install it from [Miniconda Download](https://docs.conda.io/en/latest/miniconda.html).

### **1️⃣ Create & Activate a Virtual Environment**
Open **Command Prompt** or **Anaconda Prompt** and run:

```sh
conda create -n elevenlabs_env python=3.10 -y
conda activate elevenlabs_env
```

---

### **2️⃣ Install Dependencies**
Install the required Python packages inside the activated environment:

```sh
pip install --upgrade pip
pip install requests pydub
```

---
### if you want to combine audio files
### **3️⃣ Install FFmpeg (Required for pydub)**
#### **Windows (Recommended Method)**
1. Download FFmpeg from:  
   👉 [FFmpeg Builds](https://www.gyan.dev/ffmpeg/builds/)
2. Extract it to `C:\FFmpeg`
3. Add `C:\FFmpeg\bin` to your **System PATH**:
   - Search **"Environment Variables"** in Windows.
   - Click **"Edit the system environment variables"** → **"Environment Variables"**.
   - Under **"System variables"**, find **"Path"**, click **Edit** → **New**.
   - Add: `C:\FFmpeg\bin`
   - Click **OK** and restart your terminal.

4. Verify installation:
   ```sh
   ffmpeg -version
   ```
   If it prints version details, FFmpeg is correctly installed.

---

### **4️⃣ Configure API Key**
Before running the script, create a file named **`elevenlabs_labs.py`** in the same directory and add:

```python
API_KEY = "your-elevenlabs-api-key"
VOICE_ID = "your-voice-id"
```
Replace `"your-elevenlabs-api-key"` and `"your-voice-id"` with your actual **ElevenLabs API credentials**.

---

### **5️⃣ Prepare Your Script File**
Create a **`script.txt`** file in the same directory. Format it as follows:

```
This is the first section.
####
This is the second section.
####
This is the last section.
```
The script splits the text whenever `####` appears.

---

### **6️⃣ Run the Script**
To generate the audio files, run:

```sh
python generate_audio.py
```

By default, the script will:
✅ Convert each text section into an MP3 file (`1.mp3`, `2.mp3`, etc.).  
✅ Optionally combine them into **one single MP3 file** (`combined.mp3`).  

---

## **🔄 Re-activate the Environment (After Restart)**
If you close the terminal and want to run the script later, reactivate the environment:

```sh
conda activate elevenlabs_env
```

Then, rerun the script:

```sh
python generate_audio.py
```

---

## **🐛 Troubleshooting**
### **1️⃣ "ModuleNotFoundError: No module named 'pydub'"**
Ensure pydub is installed:
```sh
pip install pydub
```

### **2️⃣ "Could not find ffmpeg"**
Make sure FFmpeg is installed and added to **System PATH** (Step 3).

### **3️⃣ ElevenLabs API Errors**
- Ensure your **API Key** is correct in `elevenlabs_labs.py`.
- Check if your **voice ID** is correct.
- If you run out of API credits, check your ElevenLabs account.

---

## 🎯 **Conclusion**
You now have a fully working **text-to-speech automation** using **ElevenLabs**, powered by Python and Miniconda! 🚀 Enjoy high-quality MP3 generation from your text scripts.

For more details, visit the [ElevenLabs API Docs](https://docs.elevenlabs.io/).
```

---

### 🔥 **Key Features in this README**
✅ **Step-by-step environment setup** using Miniconda.  
✅ **How to install dependencies** (`pydub`, `requests`, `ffmpeg`).  
✅ **How to format `script.txt`** for correct processing.  
✅ **How to run the script and handle common errors**.  

Would you like any modifications to fit your use case better? 🚀
