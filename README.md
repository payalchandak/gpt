# An interface to query OpenAI's GPT 4 model

The `GPT` class provides functionality to query GPT 4 in a chat interface with the following features. Demos for using `GPT` can be found in `run.py` and `run.ipynb`. 

- **Ask** GPT has a `ask` function which can be used to interact with GPT 
- **Chat interface** The `store_chat_history` argument allows you to track messages and replies  
- **Configuration** A file called `gpt.yaml` that is used to initialize GPT with your OpenAI API key, GPT temperature, etc...
- **Retry** The`tenacity` library automatically retries GPT when encountering RateLimitErrors from OpenAI
- **Logging** The `hydra` library creates a new logging directory each time GPT is initialized and logs each query made to GPT 4 

## Getting Started 

```bash
pip install openai
pip install tenacity
pip install hydra-core --upgrade
```

:exclamation: Note, that you will need to fill in the `gpt.yaml` file with your OpenAI information such as the API key. 

```YAML
gpt: 
  _target_: gpt4.GPT
  openai_api_type:  
  openai_api_base: 
  openai_api_version: 
  openai_api_key: 
  engine: largeGPT4
  temperature: 0.7
  system_prompt: You are a helpful assistant.
  log_dir: ${hydra:run.dir}
```

## Demo for Python script 

```python
import hydra
from omegaconf import DictConfig, OmegaConf

@hydra.main(version_base=None, config_path=".", config_name="gpt")
def experiment(cfg): 
    gpt = hydra.utils.instantiate(cfg.gpt)
    _ = gpt.ask('What year is it?', verbose=True)

if __name__ == "__main__":
    experiment()
```

## Demo for Jupyter notebook 

```python
import os
import hydra 
from omegaconf import OmegaConf
from gpt4 import GPT 

with hydra.initialize(version_base=None, config_path="."):
    cfg = hydra.compose(con fig_name="gpt", return_hydra_config=True, overrides=["gpt.log_dir=${hydra.run.dir}"])
    os.makedirs(cfg.gpt.log_dir, exist_ok=True)

gpt = hydra.utils.instantiate(cfg.gpt)
```
