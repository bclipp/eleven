import requests
import os
#from pydub import AudioSegment

# Import your ElevenLabs credentials from the config file
from elevenlabs_labs import API_KEY, VOICE_ID


def generate_audio_chunks():
    """
    Reads `script.txt`, splits on `####`, and calls the ElevenLabs API
    to generate individual MP3 files (1.mp3, 2.mp3, ...).
    Returns a list of the MP3 filenames created.
    """
    # 1. Read the script from script.txt
    with open("script.txt", "r", encoding="utf-8") as file:
        text = file.read()

    # 2. Split the text into chunks whenever we see "####"
    chunks = text.split("####")

    # Clean up whitespace around each chunk and ignore empty ones
    chunks = [chunk.strip() for chunk in chunks if chunk.strip()]

    # 3. Prepare headers for ElevenLabs API calls
    headers = {
        "xi-api-key": API_KEY,
        "Content-Type": "application/json"
    }

    # 4. Process each chunk, convert to speech, and save as mp3
    mp3_filenames = []
    for i, chunk in enumerate(chunks, start=1):
        # Build the request payload
        payload = {
            "text": chunk,
            "voice_settings": {
                "stability": 0.4,
                "similarity_boost": 0.75
            }
        }

        # ElevenLabs text-to-speech endpoint
        url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"

        print(f"Generating audio for chunk #{i}...")

        # Make the POST request
        response = requests.post(url, headers=headers, json=payload)

        if response.status_code == 200:
            # Save the response content (audio) to an MP3 file
            mp3_filename = f"{i}.mp3"
            with open(mp3_filename, "wb") as audio_file:
                audio_file.write(response.content)
            mp3_filenames.append(mp3_filename)
            print(f"Saved chunk #{i} to {mp3_filename}")
        else:
            print(f"Error generating audio for chunk #{i}: {response.text}")

    return mp3_filenames


def combine_audio_files(mp3_filenames, output_filename="combined.mp3"):
    """
    Combines all MP3 files in `mp3_filenames` into a single MP3 file
    named `output_filename`.

    Uses pydub to ensure high quality. By default, exports at 192 kbps.
    """
    if not mp3_filenames:
        print("No MP3 files to combine.")
        return

    print("Combining MP3 files into one file...")

    # Start with an empty AudioSegment
    combined = AudioSegment.empty()

    # Concatenate each MP3 file
    for mp3_file in mp3_filenames:
        audio_segment = AudioSegment.from_mp3(mp3_file)
        combined += audio_segment

    # Export the combined track at a high bitrate (e.g., 192 kbps).
    combined.export(output_filename, format="mp3", bitrate="320k")

    print(f"Saved combined audio to {output_filename}")


def main():
    # Generate each chunk as a separate MP3
    mp3_files = generate_audio_chunks()

    # (Optional) Combine them into one MP3 file
    #combine_audio_files(mp3_files, output_filename="combined.mp3")


if __name__ == "__main__":
    main()
