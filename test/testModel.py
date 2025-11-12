
import os
from openai import OpenAI
os.environ["HF_HOME"] = "/data/xwu488"
os.environ["TRANSFORMERS_CACHE"] = "/data/xwu488/transformers"
os.environ["HF_DATASETS_CACHE"] = "/data/xwu488/datasets"
os.environ["HF_MODULES_CACHE"] = "/data/xwu488/modules"
os.environ["TORCH_HOME"] = "/data/xwu488/torch"


client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.environ["HF_TOKEN"],
)

completion = client.chat.completions.create(
    model="moonshotai/Kimi-K2-Thinking:together",
    messages=[
        {
            "role": "user",
            "content": "What is the capital of France?"
        }
    ],
)

print(completion.choices[0].message)
