import streamlit as st
import pandas as pd
import numpy as np

from github import Github

# First create a Github instance:
g = Github("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") ## Personal access Token from GitHub
user = g.get_user()
st.write((user.login))
#repo1 = g.get_repo("AgamalARM/Dexcom_update1")         ## Repo name that create file in it

ver = st.__version__
print(ver)

file = f'admin.csv'                   ##'C:\\Users\Gamal\Dexcom_update\\admin.csv'
                   

@st.cache
def get_table(table_name:str, file_location:str):
    table_name = pd.read_csv(file_location)
    return table_name
    
    
df = get_table('df',file)

df = pd.read_csv(file)
#df['ref'][-1] = df['ref'].max()+1


st.write(f"Dataset before update")
st.write(df)

admin_name = "Admin Name"
admin_phone = "Admin Phone Number"
button_label = "Add Admin"   

with st.sidebar :
        form = st.form(key='form2', clear_on_submit=True) 
        add_name = form.text_input(label=f"{admin_name}")
        add_phone = form.text_input(label=f"{admin_phone}")
        #add_ref = df['ref'].max() + 1
        button_press = form.form_submit_button(label=f"{button_label}")
        
                                  ### 'ref':add_ref,
        if button_press :
            new_data = {'Admin_Name':add_name,'Admin_Phone':int(add_phone)}
            st.write(new_data)
            df = df.append(new_data, ignore_index=True)
            df.to_csv(file,index=False)
        else : 
            st.write("Please fill the form")
            
st.write(f"Dataset after update")
st.write(df)
df.to_csv(file,index=False)
#repo1.create_file("filesaved2.csv","Dexcom File Saved", "This is the content of df_student")

            
        
        
        
        
