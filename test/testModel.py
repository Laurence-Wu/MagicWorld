from pathlib import Path
import os
from transformers import pipeline


# --- 1. Define your download ---
REPO_ID = "unsloth/DeepSeek-V3.1-GGUF"
SUBDIR_PATTERN = "Q4_K_M/*.gguf"    # The quant folder you want
CACHE_DIR = "/data/xwu488"
# ensure cache dir exists and set HF cache env vars so all HF tooling uses the same place
os.makedirs(CACHE_DIR, exist_ok=True)
os.environ["HF_HOME"] = CACHE_DIR
os.environ["TRANSFORMERS_CACHE"] = os.path.join(CACHE_DIR, "transformers")
os.environ["HF_DATASETS_CACHE"] = os.path.join(CACHE_DIR, "datasets")
os.environ["HF_MODULES_CACHE"] = os.path.join(CACHE_DIR, "modules")
os.environ["TORCH_HOME"] = os.path.join(CACHE_DIR, "torch")

# Use a pipeline as a high-level helper; explicitly pass cache_dir too
pipe = pipeline(
    "text-generation",
    model="deepseek-ai/DeepSeek-R1-Distill-Qwen-32B",
    cache_dir=CACHE_DIR,
    trust_remote_code=True,
)
messages = [
    {"role": "user", "content": "Who are you?"},
]
pipe(messages)