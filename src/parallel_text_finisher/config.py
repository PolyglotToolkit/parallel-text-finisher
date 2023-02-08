from pathlib import Path

from dynaconf import Dynaconf

settings_file = Path("configs/settings.toml")
secrets_file = Path("configs/.secrets.toml")
import os

print(settings_file, os.path.exists(settings_file))
print(secrets_file, os.path.exists(secrets_file))
print(os.listdir("."))
settings = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=[settings_file, secrets_file],
)

# `envvar_prefix` = export envvars with `export DYNACONF_FOO=bar`.
# `settings_files` = Load these files in the order.
