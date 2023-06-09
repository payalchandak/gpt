# An interface to query OpenAI's GPT 4 model

The `GPT` class provides functionality to query GPT 4 in code with the following features:

- **Ask** `GPT` has a `ask` function which can be used to interact with GPT 4  
- **Chat interface** The `store_chat_history` parameter in `ask` allows you to track messages history  
- **Configuration** A file called `gpt.yaml` that is used to initialize `GPT` with your API key, temperature, etc...
- **Retry** The`tenacity` library automatically retries the query when encountering RateLimitErrors from OpenAI
- **Logging** The `hydra` library creates a new logging directory each time `GPT` is initialized and logs conversations by date

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

## Usage and Tutorials 

### Python
```python
import hydra
from omegaconf import DictConfig, OmegaConf
from gpt4 import GPT 

@hydra.main(version_base=None, config_path=".", config_name="gpt")
def experiment(cfg): 
    gpt = hydra.utils.instantiate(cfg.gpt)
    reply = gpt.ask('What year is it?', verbose=True, store_chat_history=False)

if __name__ == "__main__":
    experiment()
```

### Jupyter notebook 

```python
import os
import hydra 
from omegaconf import OmegaConf
from gpt4 import GPT 

with hydra.initialize(version_base=None, config_path="."):
    cfg = hydra.compose(config_name="gpt", return_hydra_config=True, overrides=["gpt.log_dir=${hydra.run.dir}"])
    os.makedirs(cfg.gpt.log_dir, exist_ok=True)

gpt = hydra.utils.instantiate(cfg.gpt)
reply = gpt.ask('What year is it?', verbose=True, store_chat_history=False)
```
