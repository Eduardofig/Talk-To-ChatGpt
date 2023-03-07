from gtts import gTTS
from io import BytesIO
import pygame

def play_audio_message(message):
    # Create a gTTS object with the message
    tts = gTTS(message, lang="pt-br")

    # Save the audio to a BytesIO object
    fp = BytesIO()
    tts.write_to_fp(fp)

    # Rewind the BytesIO object to the beginning
    fp.seek(0)

    # Initialize pygame mixer for playing the audio
    pygame.mixer.init()

    # Load the BytesIO object as an audio file
    pygame.mixer.music.load(fp)

    # Play the audio
    pygame.mixer.music.play()

    # Wait until the audio has finished playing
    while pygame.mixer.music.get_busy():
        pygame.time.wait(100)

    # Clean up the pygame mixer
    pygame.mixer.quit()
