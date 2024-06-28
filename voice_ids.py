

from pyht import Client, TTSOptions, Format
import simpleaudio as sa

def getvoiceid(name):
    if name == 'Optimus Prime':
        options = TTSOptions(
        # this voice id can be one of our prebuilt voices or your own voice clone id, refer to the`listVoices()` method for a list of supported voices.
        voice="s3://voice-cloning-zero-shot/08d78651-9f07-49e0-abd9-75f6230080f7/original/manifest.json",

        # you can pass any value between 8000 and 48000, 24000 is default
        sample_rate=44_100,
    
        # the generated audio encoding, supports 'raw' | 'mp3' | 'wav' | 'ogg' | 'flac' | 'mulaw'
        format=Format.FORMAT_MP3,

        # playback rate of generated speech
        speed=0.9,
        )
    elif name == 'Morgan Freeman':
        options = TTSOptions(
        # this voice id can be one of our prebuilt voices or your own voice clone id, refer to the`listVoices()` method for a list of supported voices.
        voice="s3://voice-cloning-zero-shot/a8224524-05e6-4cd4-9542-786e666a3690/original/manifest.json",

        # you can pass any value between 8000 and 48000, 24000 is default
        sample_rate=44_100,
    
        # the generated audio encoding, supports 'raw' | 'mp3' | 'wav' | 'ogg' | 'flac' | 'mulaw'
        format=Format.FORMAT_MP3,

        # playback rate of generated speech
        speed=0.9,
        )
    elif name == 'Priyanka Chopra':
        options = TTSOptions(
        # this voice id can be one of our prebuilt voices or your own voice clone id, refer to the`listVoices()` method for a list of supported voices.
        voice="s3://voice-cloning-zero-shot/64eea456-f123-4422-9ef8-921db30cb01f/original/manifest.json",

        # you can pass any value between 8000 and 48000, 24000 is default
        sample_rate=44_100,
    
        # the generated audio encoding, supports 'raw' | 'mp3' | 'wav' | 'ogg' | 'flac' | 'mulaw'
        format=Format.FORMAT_MP3,

        # playback rate of generated speech
        speed=0.9,
        )
    elif name == 'Shashi Tharoor':
        options = TTSOptions(
        # this voice id can be one of our prebuilt voices or your own voice clone id, refer to the`listVoices()` method for a list of supported voices.
        voice="s3://voice-cloning-zero-shot/4a4352b9-6563-4e44-b1f1-b9be6cd45c90/original/manifest.json",

        # you can pass any value between 8000 and 48000, 24000 is default
        sample_rate=44_100,
    
        # the generated audio encoding, supports 'raw' | 'mp3' | 'wav' | 'ogg' | 'flac' | 'mulaw'
        format=Format.FORMAT_MP3,

        # playback rate of generated speech
        speed=0.7,
        )
    elif name == 'R Madhvan':
        options = TTSOptions(
        # this voice id can be one of our prebuilt voices or your own voice clone id, refer to the`listVoices()` method for a list of supported voices.
        voice="s3://voice-cloning-zero-shot/450ad8fb-87bc-4dcf-8709-73cd0c185dda/original/manifest.json",

        # you can pass any value between 8000 and 48000, 24000 is default
        sample_rate=44_100,
    
        # the generated audio encoding, supports 'raw' | 'mp3' | 'wav' | 'ogg' | 'flac' | 'mulaw'
        format=Format.FORMAT_MP3,

        # playback rate of generated speech
        speed=0.9,
        )
    return options