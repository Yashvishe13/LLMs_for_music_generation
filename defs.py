# Function to process each file
import os
import subprocess

# Input and output folder paths
input_folder = "ChMusic/Musics"
output_folder = "Separated_Tracks"

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

def process_file(file):
    """
    Process a single audio file to separate vocals and instruments using Demucs.
    """
    if file.endswith(".wav"):  # Process only .wav files
        input_file = os.path.join(input_folder, file)
        output_path = os.path.join(output_folder, file.replace(".wav", ""))
        
        print(f"Processing {file}...")
        subprocess.run([
            "demucs",
            "-o", output_folder,  # Output directory
            "--two-stems", "vocals",  # Separate vocals from the rest
            input_file
        ])
        print(f"Finished processing {file}")