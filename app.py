from langchain.prompts import PromptTemplate
from transformers import pipeline  # Using transformers directly for translation
import gradio as gr
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Step 2: Load the translation pipeline from Hugging Face
translator = pipeline("translation_en_to_fr", model="Helsinki-NLP/opus-mt-en-fr")

# Step 3: Create a prompt template for translation
prompt_template = PromptTemplate(
    input_variables=["text"],
    template="Translate the following English text to French: {text}"
)

# Step 4: Function to translate text
def translate_to_french(english_text):
    # Use the translator pipeline directly
    translation_result = translator(english_text, max_length=40)
    return translation_result[0]['translation_text']

# Step 5: Create Gradio interface
def translate_interface(english_text):
    french_translation = translate_to_french(english_text)
    return french_translation

# Step 6: Set up Gradio Blocks
with gr.Blocks() as demo:
    gr.Markdown("<h1>English to French Translator</h1>")
    with gr.Row():
        english_input = gr.Textbox(label="Enter English Text", placeholder="Type here...")
        french_output = gr.Textbox(label="French Translation", interactive=False)
    translate_button = gr.Button("Translate")
    
    translate_button.click(fn=translate_interface, inputs=english_input, outputs=french_output)

# Step 7: Launch the Gradio app
if __name__ == "__main__":
    demo.launch()
