from django.shortcuts import render
from .models import FindMedicine


def find_medicine_form(request):
    """
        This method is used to display find medicine form.


        :param request: it's a HttpResponse from user.


        :type request: HttpResponse.


        :return: this method returns a html page. It returns the find medicine form.


        :rtype: HttpResponse.
        """
    return render(request, 'find_med_form.html')


def search_medicine(request):
    """
          This method is used to search medicine by generic name , it search all
          the records in the data base for the medicine and display the medicine.


          :param request: it's a HttpResponse from user.


          :type request: HttpResponse.


          :return: this method returns a html page that display of the search medicine from data base.


          :rtype: HttpResponse.
          """
    query = request.GET['query']
    similar_med = FindMedicine.objects.filter(generic=query)

    return render(request, 'search_med.html', {'results': similar_med})

