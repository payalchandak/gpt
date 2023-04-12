# An interface to query OpenAI's GPT model

Need a YAML file called `gpt.yaml` with the `openai` information filled in. This file is not provided to protect API keys. 

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
The `GPT` class provides functionality to query GPT 4 in a chat interface while logging all conversations. A demo for using `GPT` is provided in `run.py`.
