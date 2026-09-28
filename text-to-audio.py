from gtts import gTTS

text = "hello, how are you today?"

tts = gTTS(
    text=text,
    lang="en",
    slow=False
)

tts.save("english_audio.mp3")

print("Audio saved: english_audio.mp3")