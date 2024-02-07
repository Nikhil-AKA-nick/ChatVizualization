
import os
import warnings
warnings.filterwarnings("ignore")

os.environ["OPENAI_API_KEY"] = "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"

import streamlit as st

from utils import get_data
from tools import handle_openai_query 

# from key_check import key_check
st.set_option("deprecation.showPyplotGlobalUse", False)

st.title("Chat2Viz")

df = get_data()

if df is not None:
    col_names = ", ".join(df.columns)
    handle_openai_query(df, column_names=col_names)
    