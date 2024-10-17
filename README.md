# gemma-2b-ar
## Arabic Writing Assistant Model
## Table of Contents:
- [Overview](#overview) <br>
- [Features](features) <br>
- [Requirements](requirements)<br>
- [Installation](installation) <br>
- [Technical details](technical-details) <br>
- [Contributing](contributing) <br>
- [License](license) <br>
- [Acknowledgemnt](acknowledgement) <br>

### Overview
This project provides a writing assistant model fine-tuned on the Gemma-2B dataset, which consists of a diverse range of Arabic articles. The model is designed to assist users in generating, editing, and enhancing Arabic text through an intuitive chat-based user interface (UI).

### Features
-  Fine-tuned Language Model : Built on the Gemma-2B dataset for high-quality Arabic language understanding and generation.
-  Chat UI : User-friendly interface for real-time interactions with the writing assistant.-
-  Text Generation: Generate coherent and contextually relevant Arabic text.
-  Text Enhancement: Improve existing text with suggestions and edits.
-  Customization: Tailor responses based on user preferences and writing styles.
### Requirements
-  Python 3.8 or higher
-  Required libraries:
-  llama-cpp-python
-  gradio
-  langchain 
   Other dependencies listed in requirements.txt
### Installation
Clone the repository:

``` 
$ git clone .git

$ cd arabic-writing-assistant
```
#### Install the required dependencies:

```
Copy code
pip install -r requirements.txt
```

#### Usage
Start the chat server:
```
first try.py
```
Open your web browser and navigate to:

http://localhost:5000
Interact with the writing assistant through the chat interface.

Example Interaction
User: "اكتب مقال عن الرياضة " Assistant: "رياضة هو ما يجعل الإنسان قويا ً ومرتاحا ً ومستعدا ً للعمل . الرياضة هي أيضا ً مصدر إلهامة وتفكير جديد ، فهي تساعد على تطوير العقل والقدرة على حل المشكلات . كما أنها تمنحنا الثقة بالنفس والتميز في العمل.يلرياضة هي جزء من حياتنا اليومية ، فهي تساعد على التخلص من الضغوط والتوتر . كما أنها تمنحنا الطاقة والمعرفة التي نحتاجها في الحياة "
### Technical Details
- Model Architecture: this is a finetuned model using QLoRa technique to shorten the amount of time needed and based on Gemma2-2b which can be easy to load it on local cpu and use it as a loca ai assistant.
- Data Source: The Arabic Pile is a comprehensive dataset meticulously designed to parallel the structure of The Pile and The Nordic Pile. Focused on the Arabic language, the dataset encompasses a vast array of linguistic nuances, incorporating both Modern Standard Arabic (MSA) and various Levantine, North African, and Egyptian dialects. Tailored for the training and fine-tuning of large language models, the dataset consists of 13 subsets, each uniquely crafted to cater to different linguistic domains.(https://huggingface.co/datasets/premio-ai/TheArabicPile_Articles)
### Contributing
Contributions are welcome! Please follow these steps to contribute:

Fork the repository.
Create a new branch:
```
git checkout -b feature/YourFeature
```
Make your changes and commit them:
```
git commit -m "Add your message here"
```
Push to your branch:
```
git push origin feature/YourFeature
Create a pull request.
```
### License
 See the LICENSE file for details.

### Acknowledgments

Special thanks to the open-source community for their contributions to the development of language models.
