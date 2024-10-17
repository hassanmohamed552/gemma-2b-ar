import gradio as gr
from llama_cpp import Llama
from langchain_community.llms import LlamaCpp
from langchain.chains import LLMChain
from langchain_core.callbacks import CallbackManager, StreamingStdOutCallbackHandler
from langchain_core.prompts import PromptTemplate
import time 
import os

model_path = "gemma-2-2b-ar-final-q4_k_m.gguf\\gemma-2-2b-ar-final-q4_k_m.gguf"  # Update to your model path

# Check if the model exists
if not os.path.exists(model_path):
    # Download the model from Hugging Face Hub
    llm = Llama.from_pretrained(
       repo_id="hassan123mohamed/Gemma-2-2b-ar-final-Q4_K_M-GGUF",
       filename="gemma-2-2b-ar-final-q4_k_m.gguf",
       cache_dir=model_path, # Add this line to specify the directory
  	 	)

    
callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])

llm = LlamaCpp(model_path=(model_path+'/models--hassan123mohamed--Gemma-2-2b-ar-final-Q4_K_M-GGUF/snapshots/84369276871cdb64897c831a5b6ebb982c848c43/gemma-2-2b-ar-final-q4_k_m.gguf'),max_tokens=512,
                  temperature=0.7,     # Sampling temperature
                  top_p=0.9,           # Nucleus sampling (top-p)
                  top_k=50,            # Top-k sampling
                  repeat_penalty=1.3,
                  callback_manager=callback_manager,
                  verbose=True,   # Penalty for repeating tokens
                  )  # type: ignore

template = """Question: {question}

Answer: {Answer}"""





with gr.Blocks(title='Gemmma-2b-ar') as codellama_demo:
    chatbot = gr.Chatbot([], elem_id="Chatbot", height=500)
    user_input = gr.Textbox(placeholder="Type your message here...")
    clear_button = gr.ClearButton([user_input, chatbot])

    def generate_response(query):
        prompt = PromptTemplate(template=template, input_variables=['question', 'Answer'])
        chain = LLMChain(prompt=prompt, llm=llm)
        response = chain.run({'question': query, 'Answer': ''})
        return response
    
    def chat_with_bot(message, chat_history):
        bot_message = generate_response(message)
        chat_history.append((message, bot_message))
        time.sleep(1)  # Adjusted to 1 second for a more responsive feel
        return "", chat_history  # Return empty string for user input and updated history

    user_input.submit(chat_with_bot, [user_input, chatbot], [user_input, chatbot])

codellama_demo.launch()



