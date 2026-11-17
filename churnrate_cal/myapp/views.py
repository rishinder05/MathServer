from django.shortcuts import render
def Churn_rate(request):
    IniCus = float(request.POST.get('initialCust', '0'))
    PreCus = float(request.POST.get('presentcust', '0'))
    churn = (IniCus/PreCus)*100   if request.method == 'POST' else 0
    print("Initial Customer =",IniCus)
    print("Present Customer =",PreCus)
    print("Churn Rate =",churn)
    return render(request, 'myapp/churn.html',{'IniCus': IniCus, 'PreCus': PreCus, 'churn': churn})