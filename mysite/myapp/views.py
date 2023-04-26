from cProfile import Profile
from django.shortcuts import render 
import pandas as pd
from .forms import CSVUploadForm, LoginForm, UserRegistrationForm
from . models import CSVData,Profile
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import Profile
from io import BytesIO

# calculates unit_price
def upload_file(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST,request.FILES)
        if form.is_valid():
            #read the contents of the file using pandas
            df = pd.read_csv(request.FILES['csv_file'])
            df['unit_price'] = df['CIF Value']/df['Stat Quantity']
            
            grouped = df.groupby('M2_Declaration_Number')
            
            for M2_Declaration_Number , M2_Declaration_Number_df in grouped:
                  print(M2_Declaration_Number)
                  print(M2_Declaration_Number_df)
 
            group_averages = grouped['unit_price'].mean()
            print(group_averages)
            def check_price(row):
                group_avg = group_averages[row['M2_Declaration_Number']]
                group_avg_p = (group_avg*10)/100
                group_avg_pl = group_avg - group_avg_p
                group_avg_o = group_avg + group_avg_p
                if row['unit_price'] < group_avg_pl:
                    return "Undervalue"
                elif row['unit_price'] > group_avg_o:
                    return "Overvalue"
                else :
                    return "Expected"
            
            df['Test'] = df.apply(check_price, axis=1)
            
        
        # Function comapre string
            def check_price2(row):
            
                expected_words = row['GOODS_DESCRIPTION'].split()
                print(expected_words)  
                commodity_desc = row['COMMODITY_DESC'].upper()
                print(commodity_desc)
                
                for word in expected_words:
                    print(f"Is '{word}' in '{commodity_desc}'? {word in commodity_desc}")
                commodity_contains_expected = any(word in commodity_desc for word in expected_words)
                print(commodity_contains_expected)
                
                if commodity_contains_expected == True:
                      
                    print("one or more expected word")
                    return "True"
                    
                else:
                    print(f"Item is an expected import/export.")
                    return "False"

            df['Test2'] = df.apply(lambda row: check_price2(row), axis=1)
            df = df.drop(['Unnamed: 0','Unnamed: 9','Unnamed: 10'], axis=1)
            return render(request,'myapp/data.html',{'data':df.to_html()})        
    else:
        form = CSVUploadForm()
    return render(request,'myapp/upload_csv.html',{'form':form})

#  login function
def user_login(request):
    if request.method == "POST":
       form = LoginForm(request.POST)
       if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
               request,username=data['username'],password=data['password'])
            if user is not None:
                login(request,user)
                return render(request,'upload.html')
            else:
                return HttpResponse('Invalid credentials')
    else:
        form  = LoginForm()
    return render(request,'myapp/login.html',{'form':form})

# register function
def register(request):
    if request.method =='POST':
       user_form =  UserRegistrationForm(request.POST)
       if user_form.is_valid():
           new_user = user_form.save(commit = False)
           new_user.set_password(user_form.cleaned_data['password'])
           new_user.save()
           Profile.objects.create(user=new_user)
           return render(request,'myapp/login.html')
       
    else:
        user_form = UserRegistrationForm()
    return render(request,'register.html',{'user_form': user_form})

def download_excel(request):
    data = CSVData.objects.all().values()
    df = pd.DataFrame(data)  # retrieve data from database or create DataFrame
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet1')
    writer.save()
    filename = 'file.xlsx'
    response = HttpResponse(output.getvalue(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename={filename}'
    return response

