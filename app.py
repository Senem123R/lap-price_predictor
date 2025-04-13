from flask import Flask, render_template, request
import pickle
import numpy as np 

# setup application
app = Flask(__name__,template_folder="C:/Users/Risni Maleesha/Desktop/project/website/tamplate")

def prediction(lst):
    filename = 'model/predictor.pickle'
    with open(filename, 'rb') as file:
        modle = pickle.load(file)
    pred_value = modle.predict([lst])
    return pred_value

@app.route('/', methods =['POST','GET'])
def index():
    pred_value = 0
    if request.method == 'POST':
        ram = request.form['ram']
        weight = request.form['weight']
        company = request.form['company']
        typename = request.form['typename']
        opSys = request.form['opsys']
        cpu = request.form['cpuname']
        gpu = request.form['gpuname']
        touchscreen = request.form.getlist('touchscreen')
        ips = request.form.getlist('ips')

        feature_list = []
        feature_list.append(int(ram))
        feature_list.append(float(weight))
        feature_list.append(len(touchscreen))
        feature_list.append(len(ips))

        company_list = ['acer','apple','asus','dell','hp','lenovo','msi','other','toshiba']
        typename_list = ['2in1convertible','gaming','netbook','notebook','ultrabook','workstation']
        opsys_list = ['linux','mac','other','windows']
        cpu_list = ['amd','intelcorei3','intelcorei5','intelcorei7','other']
        gpu_list = ['amd','intel','nvidia']

         # for item in company_list:
        #     if item == company:
        #         feature_list.append(1)
        #     else:
        #         feature_list.append(0)

        def taverse_list(lst, value):
            for item in lst:
                if item == value:
                    feature_list.append(1)
                else:
                    feature_list.append(0)
        
        taverse_list(company_list, company)
        taverse_list(typename_list, typename)
        taverse_list(opsys_list, opSys)
        taverse_list(cpu_list, cpu)
        taverse_list(gpu_list, gpu)

        pred_value = prediction(feature_list)
        pred_value = np.round(pred_value[0],2)*221


    return render_template("index1.html",  pred_value=pred_value)


if __name__ == '__main__':
    app.run(debug=True)
