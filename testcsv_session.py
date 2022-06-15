import pandas as pd
import streamlit as st

# url of template data csv file
# web location for csv file, 'df.csv'
data_src = r'https://raw.githubusercontent.com/clueple/free_resources/master/df.csv'
# web location for csv file, 'dfc.csv'
data_src1 = r'https://raw.githubusercontent.com/clueple/free_resources/master/dfc.csv'

# """ Background functions   """

# convert to dataframe from upload or url in csv format
def get_data(src):
	return pd.read_csv(src)

# convert to downloadable csv
def convert_df(df):
   return df.to_csv(index=False).encode('utf-8')


# """ Preprocessed Data  """
# downloaable template from web
temp_data = get_data(src=data_src1)

# unwant col name
unwant_col = r'Unnamed: 0'

# """ get_default_columns  """
def_col = temp_data.columns


# Download template if you don't have any data at all
st.download_button(
	label = 'Download Template',
	data = convert_df(temp_data),
	file_name = 'dfc.csv',
	mime = 'text/csv',
	key = 'tempdata'
	)

# Upload your on-going data to begin 
upload_data = st.file_uploader(
	label = 'Upload Data',
	type = 'csv',
	key = 'uploaddata',
	help = 'This is the on-going data file from your last input session'
	)

# initiate session state of 'df_result' for the dataframe to be updated
if 'df_result' not in st.session_state:
	st.session_state['df_result'] = pd.DataFrame(columns = def_col)

# if form submit button is clicked
# def onAddRow(add_data):
# 	st.session_state['df_result'] = st.session_state['df_result'].append(add_data, ignore_index=True)


def main():
	if upload_data is not None:

		st.header('Before Update')
		st.session_state['df_result'] = st.session_state['df_result'].append(pd.read_csv(upload_data), ignore_index=True)
		st.session_state['df_result']

		with st.sidebar.form(key = 'input'):
			add_col1 = st.number_input(key = 'add_col1', label='Add Item 1', min_value=0.00 )
			add_col2 = st.number_input(key = 'add_col2', label='Add Item 2', min_value=0.00 )
			add_col3 = st.number_input(key = 'add_col3', label='Add Item 3', min_value=0.00 )

			add_data = {
			'col1':add_col1,
			'col2':add_col2,
			'col3':add_col3
			}
			
			# submit = st.form_submit_button('Submit',on_click=onAddRow(add_data))
			submit = st.form_submit_button('submit')
			if submit:
				st.session_state['df_result'] = st.session_state['df_result'].append(add_data, ignore_index=True)

		st.header('After Update')
		st.session_state['df_result']

		st.session_state



if __name__ == "__main__":
	main()




# # "st.session_state object:", st.session_state

# if "df_result" not in st.session_state:
#     st.session_state['df_result'] = pd.DataFrame(columns=['h1','h2'])


# # st.write(st.session_state)

# def onAddRow():
#     data = {
#             'h1':"something",
#             'h2':"something",
#         }
#     st.session_state['df_result'] = st.session_state['df_result'].append(data, ignore_index=True)

# st.button("Add row", on_click = onAddRow)



# @st.cache
# def convert_df(df):
#    return df.to_csv().encode('utf-8')
# st.download_button(
#     "Press to Download",
#     convert_df(st.session_state.df_result),
#     "file.csv",
#     "text/csv",
#     key='download-csv'
# )
# st.dataframe(st.session_state['df_result'])

# # additional
# st.header('The session state')

# st.write(st.session_state)
