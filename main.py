import gradio as gr
import openai
import config

from tts import play_audio_message

openai.api_key_path = config.API_KEY_PATH

messages=[
    {"role": "system", "content":"You are an assistant that communicates in Brazillian Portuguese"},
]

def transcribe(audio_file_path):
    global messages

    audio_file = open(audio_file_path, "rb")

    transcript = openai.Audio.transcribe(model="whisper-1", file=audio_file)["text"]

    messages.append({"role": "user", "content": transcript})

    print(transcript)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    system_message = response["choices"][0]["message"]["content"]

    play_audio_message(system_message)

    messages.append({"role": "assistant", "content": system_message})

    response_buffer = ""


    for message in messages:
        if message["role"] != "system":
            response_buffer += "Resposta da Ia:\n" if message["role"] == "assistant" else "Voce:\n"
            response_buffer += message["content"] + "\n\n"

    return response_buffer


ui = gr.Interface(
        fn=transcribe,
        inputs=gr.Audio(source="microphone", type="filepath"),
        outputs="text"
    )

ui.launch()
