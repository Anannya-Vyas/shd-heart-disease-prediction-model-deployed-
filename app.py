import os
from openai import OpenAI
import gradio as gr

NVIDIA_API_KEY = os.environ.get("NVIDIA_API_KEY")
if not NVIDIA_API_KEY:
    raise EnvironmentError(
        "NVIDIA_API_KEY is required. Set it in your Hugging Face Space secrets."
    )

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=NVIDIA_API_KEY,
)

PROMPT_TEMPLATE = """
You are a compassionate Heart Health AI Assistant.
Use the patient data below to provide a clear, supportive analysis of heart disease risk factors, next steps, and lifestyle advice.

Patient data:
{data}

Write:
- a short summary of the risk profile
- the most important findings
- one actionable recommendation
- a friendly closing note
"""


def analyze_heart_data(patient_notes: str) -> str:
    prompt = PROMPT_TEMPLATE.format(data=patient_notes.strip())
    try:
        completion = client.chat.completions.create(
            model="google/gemma-2-2b-it",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.2,
            top_p=0.7,
            max_tokens=1024,
        )
        return completion.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {e}"


def build_example_input():
    return (
        "Age: 58\n"
        "Sex: Male\n"
        "Chest pain: moderate\n"
        "Resting blood pressure: 145\n"
        "Cholesterol: 240\n"
        "Fasting blood sugar > 120 mg/dL: yes\n"
        "Resting ECG: ST-T wave abnormality\n"
        "Max heart rate: 150\n"
        "Exercise induced angina: no\n"
        "ST depression: 1.5\n"
        "Slope: flat\n"
        "Major vessels colored: 0\n"
        "Thalassemia: normal\n"
        "Lifestyle: occasional smoking, low activity, high stress\n"
    )


demo = gr.Interface(
    fn=analyze_heart_data,
    inputs=gr.Textbox(
        lines=15,
        label="Patient health summary",
        placeholder="Enter age, symptoms, vitals, lifestyle, and any other relevant heart health details.",
        value=build_example_input(),
    ),
    outputs=gr.Textbox(label="Heart Health Analysis"),
    title="Heart Disease Risk Assistant",
    description="Paste patient data or heart health details and get a friendly analysis with next-step guidance.",
    examples=[
        [build_example_input()],
    ],
    allow_flagging="never",
)

demo.launch()
