from pathlib import Path
import os

import streamlit as st

l = st.logger.get_logger("pp")

def save_uploadedfile(uploadedfile):
	dname = os.path.dirname(os.path.abspath(__file__))
	dname = os.path.join(dname, "tempDir")

	st.write(Path(dname).mkdir(parents=True, exist_ok=True))
	st.write(dname)
	st.write(os.getcwd())
	with open(os.path.join(dname, uploadedfile.name), "wb") as f:
		f.write(uploadedfile.getbuffer())
	return os.path.join(dname, uploadedfile.name)


# return st.success("Saved File:{} to tempDir".format(uploadedfile.name))

@st.cache()
def load_uploaded_file(uploaded_file):
	return "dataframe"
	# return pd.read_csv(uploaded_file)


add_selectbox = st.sidebar.selectbox(
	"How would you like to be contacted?",
	("Email", "Home phone", "Mobile phone")
)
uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv", "xlsx"])
# if uploaded_file is not None:
load_saved_file = save_uploadedfile(uploaded_file) if uploaded_file is not None else st.info(
	'upload file first')
