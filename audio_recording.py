import pyaudio
import wave
import logging

def record_audio():
    chunk = 1024
    sample_format = pyaudio.paInt16
    channels = 1
    rate = 44100
    record_seconds = 10
    wave_output_filename = "output.wav"

    p = pyaudio.PyAudio()

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=rate,
                    input=True,
                    frames_per_buffer=chunk)

    logging.info("audio recording")

    frames = []

    for i in range(int(rate / chunk * record_seconds)):
        data = stream.read(chunk)
        frames.append(data)

    logging.info("done audio recording")

    stream.stop_stream()
    stream.close()
    p.terminate()
