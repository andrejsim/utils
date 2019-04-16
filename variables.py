import os


# load an environment variable or exit
def load_environment(header, environment_var, value=None):
    env_var_name = header+"_"+environment_var
    os_env_var = os.getenv(env_var_name)
    if os_env_var is None:
        raise Exception(env_var_name+" env variable required. \\n\nexport "+env_var_name+"="+value+"\n")
    return os_env_var
