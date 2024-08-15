import streamlit as st 

import pickle 

import numpy as np 

r=open("salary_model.pkl","rb") 

reg=pickle.load(r) 

exp=st.number_input("Experience in Years:",0,42,1) 

exp=np.array(exp).reshape(1,-1) 

prediction=reg.predict(exp)[0] 

if st.button("Salary Prediction"): 

    st.write(f"{prediction}") 

 