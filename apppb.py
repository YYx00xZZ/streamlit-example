import os
from numpy.lib.npyio import save
import streamlit as st
import altair as alt
import pandas as pd
import numpy as np


def main():
	# Once we have the dependencies, add a selector for the app mode on the sidebar.
	with st.sidebar.header('1. Upload your CSV data'):
		# Select alg
		# classifier = st.sidebar.selectbox("Select model", ("---", "Random Forest", "KNN"))
		# print(classifier)
		uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv", "xlsx"])
		# if uploaded_file is not None:
		load_saved_file = save_uploadedfile(uploaded_file) if uploaded_file is not None else st.info(
			'upload file first')
		print(load_saved_file)
		print(type(load_saved_file))
		# print(dir(load_saved_file))
	# if 'uploaded_file_path' not in st.session_state & :
	# st.session_state['uploaded_file_path'] = load_saved_file

	with st.sidebar.header('2. Set Parameters'):
		with st.form('Form1'):
			st.selectbox('Select flavor', ['Vanilla', 'Chocolate'], key=1)
			st.slider(label='Select intensity', min_value=0, max_value=100, key=4)

			st.sidebar.slider('Data split ratio (% for Training Set)', 10, 90, 80, 5, key="split_size")

			st.sidebar.slider('n_neighbors', 0, 20, 5, 1, key="parameter_n_neighbors")
			st.sidebar.select_slider('weights', options=['uniform', 'distance'], key="parameter_weights")
			st.sidebar.selectbox('Select algorithm', ['auto', 'ball_tree', 'kd_tree', 'brute'],
								 key="parameter_algorithm")
			st.sidebar.slider('leaf_size', 0, 120, 30, 5, key="parameter_leaf_size")
			# parameter_p ???kjj
			st.sidebar.select_slider('Number of jobs to run in parallel (n_jobs)', options=[1, -1],
									 key="parameter_n_jobs")

			submitted1 = st.form_submit_button('Submit 1')
			if submitted1:
				st.write('values of form access')
				st.write(st.session_state)
	run_app()


def run_app():
	# f_path=st.session_state['uploaded_file_path']
	# df = pd.read_csv(f_path)
	# st.dataframe(df)
	default_columns = ["AF3", "F7", "F3", "F5", "T7", "P7", "O1", "O2", "P8", "T8", "FC6", "F4", "F8", "AF4", "EventId"]


# df = df[default_columns]
# st.write(st.session_state['uploaded_file_path'])
from pathlib import Path
def save_uploadedfile(uploadedfile):
	dname = os.path.dirname(os.path.abspath(__file__))
	dname = os.path.join(dname, "tempDir")
	# os.mkdir (dname)

	print(Path(dname).mkdir(parents=True, exist_ok=True))
	print(dname)
	print(os.getcwd())
	with open(os.path.join(dname, uploadedfile.name), "wb") as f:
		f.write(uploadedfile.getbuffer())
	return os.path.join(dname, uploadedfile.name)


# return st.success("Saved File:{} to tempDir".format(uploadedfile.name))

@st.cache()
def load_uploaded_file(uploaded_file):
	return pd.read_csv(uploaded_file)


if __name__ == "__main__":
	main()
