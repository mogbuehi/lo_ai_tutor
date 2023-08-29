## The Final Version of the backend code is located in the `Final AI Backend` folder
This project is also hosted on HuggingFaces if you'd like to test it out yourself (without HTML parser): [https://huggingface.co/spaces/mogbuehi/LO_AI_Tutor](https://huggingface.co/spaces/mogbuehi/LO_AI_Tutor)

# AI Tutor Backend

## Overview
The AI Tutor Backend is designed to power an AI Tutor application that assists students answering questions on the Statascratch website. It uses multiple libraries to handle different aspects of the application, such as user interface, data manipulation, and interaction with OpenAI services.

## Requirements
- Python 3.11 (3.6+ should be ok)
- Gradio
- Pandas
- os
- OpenAI
- Altair (optional)
- Matplotlib (optional)
- dotenv

### Data Files
- `final_updated_cleaned_SS_questions.xlsx`: Excel file containing questions for the AI tutor
- `tool bot sys content.txt`: Text file containing context for the tool bot
- `ai tutor sys content.txt`: Text file containing context for the AI chat bot

## Installation

1. Clone the repository.
2. Navigate to the project directory.
3. Install the required Python packages:
    ```
    pip install gradio pandas openai python-dotenv
    ```
    (Optional: `pip install altair matplotlib`)

## Usage
1. Make sure you have the required data files (`final_updated_cleaned_SS_questions.xlsx` and `tool bot sys content.txt` and `ai tutor sys content.txt`) in your project directory.
2. Run the script:
    ```
    python AI_Tutor_Backend.py
    ```
3. Open the displayed Gradio interface URL in your web browser.

4. Navigate to [https://platform.stratascratch.com/coding/coding?code](https://platform.stratascratch.com/coding?code_type=2)(https://platform.stratascratch.com/coding?code_type=2) and select a question. Only 100 questions are in the excel database of this app, so pick one of the questions on the first 2 pages.

5. Once you have selected a question, select the URL 
## Contributing
If you would like to contribute to this project, please fork the repository and submit a pull request.

## License
This project is open source, under the MIT License.

