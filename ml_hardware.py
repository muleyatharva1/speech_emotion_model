import os
import librosa
import numpy as np
from sklearn.svm import SVC
import pickle
import sounddevice as sd
from scipy.io.wavfile import write

# Function to extract audio features
def extract_features(audio, sr=22050):
    # Extracting features
    mfccs = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=13)
    chroma = librosa.feature.chroma_stft(y=audio, sr=sr)
    mel = librosa.feature.melspectrogram(y=audio, sr=sr)
    contrast = librosa.feature.spectral_contrast(y=audio, sr=sr)

    # Concatenating features
    features = np.concatenate([mfccs, chroma, mel, contrast], axis=0)
    return features

def record_audio(output_path, fs, duration):
    print("Recording...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype=np.int16)
    sd.wait() # Wait until recording is finished
    print("Recording finished.")
    write(output_path, fs, recording) # Save the audio to a WAV file

with open('speech_emotion_svm.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

# Specify the path to save the audio file
output_path = "/home/pi/Desktop/60.wav"

# Record audio and save it to the specified path
record_audio(output_path, 22050, 5)

audio, sr = librosa.load(output_path, sr=None)
input_features = extract_features(audio, sr)

print(input_features)

# Pad or truncate the input features
if input_features.shape[1] < max_len:
    padded_input = np.pad(input_features, ((0, 0), (0, max_len - input_features.shape[1])), mode='constant')
else:
    padded_input = input_features[:, :max_len]

predicted_emotion = loaded_model.predict(padded_input.reshape(1, -1))
print("Predicted Emotion:", predicted_emotion)