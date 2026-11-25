import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

st.set_page_config(page_title="MBPC SRAM PPA Optimizer", layout="wide")
st.title("128-bit MBPC SRAM — PPA Comparison & Optimization Dashboard")

baseline = pd.read_csv("baseline_data.csv")
ppa_data = pd.read_csv("synthesized_ppa.csv")

st.subheader("1. Conventional SRAM vs. MBPC SRAM Baseline")
st.dataframe(baseline, use_container_width=True)

col1, col2, col3 = st.columns(3)
for ax_col, metric in zip([col1, col2, col3], ["Area", "Delay_ps", "Total_Power_W"]):
    with ax_col:
        fig, ax = plt.subplots()
        ax.bar(baseline["Architecture"], baseline[metric])
        ax.set_title(metric)
        st.pyplot(fig)

st.subheader("2. 128-bit Bank Configurations & PPA Results")
st.dataframe(ppa_data, use_container_width=True)
