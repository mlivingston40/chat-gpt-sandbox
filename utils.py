import os
from typing import List, Any, Optional, NoReturn
import logging


# def set_env_vars(vars_to_set: List[str]) -> NoReturn:
#     for var in vars_to_set:
#         try:
#             var = os.getenv(var)
#         except Exception as e:
#             print(f'[err] error loading env var: {var}, message: {e}')
