
"""
#Reference: https://github.com/krishnaik06/Dockers/blob/master/app1.py
https://blog.jcharistech.com/2021/01/21/how-to-save-uploaded-files-to-directory-in-streamlit-apps/  --- save file in a directory

Web app to upload CSV files via a web form 
and view the prediction result (health of machine condition in the next 24 hrs) on the image in the browser.
"""
import argparse
from distutils.log import debug
from fileinput import filename
import io
import os # For File Manipulations like get paths, rename
import pandas as pd
import numpy as np

# from flask import Flask, render_template, request, redirect, flash, send_from_directory, url_for
import pickle
# from werkzeug.utils import secure_filename
# from Final_case_study_1 import final_fun_1 

import streamlit as st
import joblib

model = joblib.load('webapp_model.sav')
# model = joblib.load('Extra_clf.pkl')

# classifier = pickle.load(open('webapp_model.sav', 'rb'))

def web_app():

    st.write(""" # Machine health Predictor Web App """)
    st.text(" [Check the machine health in the next 24 hours.]")
    st.subheader("Please fill the Machine Details below:")

    rotate_max_24h = st.number_input("rotate_max_24h")
    volt_mean_24h = st.number_input("volt_mean_24h")
    error1count = st.number_input("error1count",0,100)
    error2count = st.number_input("error2count",0,100)
    error3count = st.number_input("error3count",0,100)
    error4count = st.number_input("error4count",0,100)
    error5count = st.number_input("error5count",0,100)

    # input_data=[rotate_max_24h,volt_mean_24h,error1count, error2count, error3count,error4count,error5count]
    input_data=[[rotate_max_24h,volt_mean_24h,error1count, error2count, error3count,error4count,error5count]]
    input_data= np.array(input_data)
    
    if st.button("Press here to make Prediction"):
        result = model.predict(input_data)
        # result = model.predict([input_data])
        if result == ['none']:
            result = "The machine will be OK in next 24 hrs."
        elif result == ['comp1']:
            result = "'comp1' of the machine may fail in next 24 hrs."
        elif result == ['comp2']:
            result = "'comp2' of the machine may fail in next 24 hrs."
        elif result == ['comp3']:
            result = "'comp3' of the machine may fail in next 24 hrs."
        elif result == ['comp4']:
            result = "'comp4' of the machine may fail in next 24 hrs."
        # else: 
        #     result = "Please check your input"
        
        st.text_area(label='Machine condition in next 24-hrs: ',value = result , height= 100)
         
run = web_app()






# def save_uploadedfile(uploadedfile):
#      with open(os.path.join("tempDir",uploadedfile.name),"wb") as f:
#          f.write(uploadedfile.getbuffer())
#      return st.success("Saved File:{} to tempDir".format(uploadedfile.name))

# st.success('Machine condition (Model output) in the next 24-hrs  = {}'.format(result))
# #     if st.button("Meaning of the model output: "):
# #         st.text("['none'] = The machine will be OK in next 24 hrs.")
# #         st.text("['comp1'] = 'comp1' of the machine may fail in next 24 hrs.")
# #         st.text("['comp2'] = 'comp2' of the machine may fail in next 24 hrs.")
# #         st.text("['comp3'] = 'comp3' of the machine may fail in next 24 hrs.")
# #         st.text("['comp4'] = 'comp4' of the machine may fail in next 24 hrs.")


# def predict_note_authentication(rotate_max_24h,volt_mean_24h, error1count, error2count, error3count, error4count, error5count):
    
#     """Let's Authenticate the Banks Note 
#     This is using docstrings for specifications.
#     ---
#     description: The output values
        
#     """
#     prediction=classifier.predict([[rotate_max_24h,volt_mean_24h, error1count, error2count, error3count, error4count, error5count]])
#     print(prediction)
#     return prediction


# def main():
#     st.title("Bank Authenticator")
#     html_temp = """
#     <div style="background-color:tomato;padding:10px">
#     <h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML App </h2>
#     </div>
#     """
#     st.markdown(html_temp,unsafe_allow_html=True)
#     rotate_max_24h = st.text_input("rotate_max_24h","Type Here")
#     volt_mean_24h = st.text_input("volt_mean_24h","Type Here")
#     error1count = st.text_input("error1count","Type Here")
#     error2count = st.text_input("error2count","Type Here")
#     error3count = st.text_input("error3count","Type Here")
#     error4count = st.text_input("error4count","Type Here")
#     error5count = st.text_input("error5count","Type Here")
    
#     result=""
#     if st.button("Predict"):
#         result=predict_note_authentication(rotate_max_24h,volt_mean_24h, error1count, error2count, error3count, error4count, error5count)
#     st.success('The output is {}'.format(result))
#     if st.button("About"):
#         st.text("Lets LEarn")
#         st.text("Built with Streamlit")

# if __name__=='__main__':
#     main()




# def main():
#     st.title("Predictive analysis")
#     html_temp = """
#     <div style="background-color:tomato;padding:10px">
#     <h2 style="color:white;text-align:center;">Streamlit Machine health Predictor </h2>
#     </div>
#     """
#     st.markdown(html_temp,unsafe_allow_html=True)

#     finalized_model = st.file_uploader(label='Upload finalized_model.sav')
#     #Saving upload
#     if finalized_model is not None:
#         file_details = {"FileName":finalized_model.name,"FileType":finalized_model.type}
#         save_uploadedfile(finalized_model)

#     PdM_errors = st.file_uploader(label='Upload PdM_errors.csv')
#     #Saving upload
#     if PdM_errors is not None:
#         file_details = {"FileName":PdM_errors.name,"FileType":PdM_errors.type}
#         save_uploadedfile(PdM_errors)

#     PdM_machines = st.file_uploader(label='Upload PdM_machines.csv')
#     #Saving upload
#     if PdM_machines is not None:
#         file_details = {"FileName":PdM_machines.name,"FileType":PdM_machines.type}
#         save_uploadedfile(PdM_machines)

#     PdM_maint = st.file_uploader(label='Upload PdM_maint.csv')
#     #Saving upload
#     if PdM_maint is not None:
#         file_details = {"FileName":PdM_maint.name,"FileType":PdM_maint.type}
#         save_uploadedfile(PdM_maint)

#     PdM_telemetry = st.file_uploader(label='Upload PdM_telemetry.csv')
#     #Saving upload
#     if PdM_telemetry is not None:
#         file_details = {"FileName":PdM_telemetry.name,"FileType":PdM_telemetry.type}
#         save_uploadedfile(PdM_telemetry)


#     #Final function
#     finalized_model = (os.getcwd() + "/tempDir/finalized_model.sav")#'finalized_model.sav'
#     PdM_errors = (os.getcwd() + "/tempDir/PdM_errors.csv")#'PdM_errors.csv'
#     # print(PdM_errors)
#     PdM_machines = (os.getcwd() + "/tempDir/PdM_machines.csv")#'PdM_machines.csv'
#     PdM_maint = (os.getcwd() + "/tempDir/PdM_maint.csv")#'PdM_maint.csv'
#     PdM_telemetry = (os.getcwd() + "/tempDir/PdM_telemetry.csv")#'PdM_telemetry.csv'
#     result= final_fun_1(PdM_telemetry, PdM_errors, PdM_maint, PdM_machines, finalized_model)
#     # print(result)


#     result=""
#     if st.button("Click to Predict Machine condition in next 24 hrs"):
#         result=final_fun_1(PdM_telemetry, PdM_errors, PdM_maint, PdM_machines, finalized_model)
#     st.success('Machine condition (Model output) in the next 24-hrs  = {}'.format(result))
#     if st.button("Meaning of the model output: "):
#         st.text("['none'] = The machine will be OK in next 24 hrs.")
#         st.text("['comp1'] = 'comp1' of the machine may fail in next 24 hrs.")
#         st.text("['comp2'] = 'comp2' of the machine may fail in next 24 hrs.")
#         st.text("['comp3'] = 'comp3' of the machine may fail in next 24 hrs.")
#         st.text("['comp4'] = 'comp4' of the machine may fail in next 24 hrs.")


# if __name__=='__main__':
#     main()






# # app = Flask(__name__)

# path = os.getcwd() # Get the current working directory (CWD)
# # file Upload
# UPLOAD_FOLDER = os.path.join(path, 'uploads')

# if not os.path.isdir(UPLOAD_FOLDER):
#     os.mkdir(UPLOAD_FOLDER)

# # app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# ALLOWED_EXTENSIONS = set(['csv', 'sav'])

# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# @app.route('/')
# def home():
#     return render_template ('index.html')

# @app.route("/", methods=["GET", "POST"])
# # @app.route('/predict', methods=['POST'])
# def predict():
#     if request.method == "POST":
#         file1 = request.files["file1"]
#         if file1 and allowed_file(file1.filename):
#             filename = secure_filename(file1.filename)
#             file1.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
#         file2 = request.files["file2"]
#         if file2 and allowed_file(file2.filename):
#             filename = secure_filename(file2.filename)
#             file2.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
#         file3 = request.files["file3"]
#         if file3 and allowed_file(file3.filename):
#             filename = secure_filename(file3.filename)
#             file3.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

#         file4 = request.files["file4"]
#         if file4 and allowed_file(file4.filename):
#             filename = secure_filename(file4.filename)
#             file4.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

#         file5 = request.files["file5"]
#         if file5 and allowed_file(file5.filename):
#             filename = secure_filename(file5.filename)
#             file5.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
#         #Final function
#         finalized_model = (os.getcwd() + "/uploads/finalized_model.sav")#'finalized_model.sav'
#         PdM_errors = (os.getcwd() + "/uploads/PdM_errors.csv")#'PdM_errors.csv'
#         # print(PdM_errors)
#         PdM_machines = (os.getcwd() + "/uploads/PdM_machines.csv")#'PdM_machines.csv'
#         PdM_maint = (os.getcwd() + "/uploads/PdM_maint.csv")#'PdM_maint.csv'
#         PdM_telemetry = (os.getcwd() + "/uploads/PdM_telemetry.csv")#'PdM_telemetry.csv'
#         result= final_fun_1(PdM_telemetry, PdM_errors, PdM_maint, PdM_machines, finalized_model)
#         # print(result)

#         ##Final function _read file from local machine
#         # PdM_telemetry = r"C:\Users\medinikb\AAIC\Case_study#1\PdM_telemetry.csv"#'PdM_telemetry.csv'
#         # PdM_errors = r"C:\Users\medinikb\demo1\uploads\PdM_errors.csv"#'PdM_errors.csv'
#         # PdM_maint = r"C:\Users\medinikb\demo1\uploads\PdM_maint.csv"#'PdM_maint.csv'
#         # PdM_machines = r"C:\Users\medinikb\demo1\uploads\PdM_machines.csv"#'PdM_machines.csv'
#         # finalized_model = r"C:\Users\medinikb\demo1\uploads\web_model.sav"#'finalized_model.sav'
#         # result= final_fun_1(PdM_telemetry, PdM_errors, PdM_maint, PdM_machines, finalized_model)
#         # print(result)

#     return render_template("output.html", prediction_text='Machine condition (Model output) in the next 24-hrs  = {}'.format(result))


# if __name__ == "__main__":
#     app.run(host='127.0.0.1', port=5000, debug=False, threaded=True)