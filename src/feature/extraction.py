import os
import librosa
import matplotlib.pyplot as plt
import sys
import pathlib

def generate_mel_spectrogram(folder_path,track_name):
    if track_name.endswith('.mp3'):
        x, sr = librosa.load(folder_path/track_name)
        hop_length = 256
        S = librosa.feature.melspectrogram(x,sr=sr,n_fft=4096,hop_length=hop_length)
        logS = librosa.power_to_db(abs(S))
        plt.figure(figsize=(15,5))
        librosa.display.specshow(logS,sr,hop_length=hop_length,x_axis='time',y_axis='mel')
        plt.colorbar(format='%+2.0f dB')
        plt.savefig(folder_path/'Spectrogram'/os.path.splitext(track_name)[0]+'.png')

def get_tracks_spectrogram(folder_path):
    if not os.path.exists(folder_path/'Spectrogram'):
        os.makedirs(folder_path/'Spectrogram')
    for track_name in os.listdir(str(folder_path)):
        generate_mel_spectrogram(folder_path,track_name)

if __name__ == "__main__":
    root_path = pathlib.Path().absolute() / sys.argv[1]
    for folders in os.listdir(str(root_path)):
        get_tracks_spectrogram(root_path / folders)