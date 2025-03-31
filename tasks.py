from invoke import task


@task
def vllm(
    c, 
    model:str = "microsoft/Phi-4-mini-instruct", 
    max_model_len:int = 10000, 
    half_precision:bool = False
):
    cmd = f"uv run vllm serve {model} --max-model-len {max_model_len}"
    if half_precision:
        cmd += " --dtype=half"
        
    c.run(cmd)