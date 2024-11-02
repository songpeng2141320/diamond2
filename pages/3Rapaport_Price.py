import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
st.set_page_config(page_title="diamond",layout="wide")

RAP = "Rap.pkl"

@st.cache_data
def get_data(FILENAME):
    df = pd.read_pickle(FILENAME)
    df = df[df["clarity"]!="FL"]
    return df


def price(tmp,s3):
	fig,ax = plt.subplots(figsize=(10,9),dpi=100)

	tmp2 = pd.pivot(data=tmp,index="color",columns="clarity",values="price")
	tmp2 = tmp2[["IF","VVS1","VVS2","VS1","VS2","SI1","SI2"]]
	sns.heatmap(tmp2,annot=True,fmt=".0f",linewidths=2,cmap="Blues",cbar=False)  # Wistia
	ax.xaxis.set_ticks_position('top')
	plt.title(s3,fontsize=18)
	plt.xlabel("")
	plt.ylabel("")
	# plt.xlabel("Clarity",fontsize=16)
	# plt.ylabel("Color",fontsize=16)
	return fig

def main():
	df = get_data(RAP)

	dates = df.date.dt.strftime("%Y-%m-%d").unique().tolist()
	with st.sidebar:
		st.write("### Select:")
		s1 = st.selectbox(label="日期：",options=dates)
		s2 = st.selectbox(label="Size:",options=df["size"].unique())

	st.write("## Rapaport Price \n"+s1)

	tmp = df[(df["date"]==s1)&(df["size"]==s2)]
	fig = price(tmp,s2)
	st.pyplot(fig)


if __name__ == '__main__':
	main()