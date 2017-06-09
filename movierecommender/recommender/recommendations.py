import httplib, urllib, base64
from django.shortcuts import render
from django.template import loader
from django.template import Context

from django.conf import settings

import urllib2
import json 

#def recommend(request):
def recommend(request):

    if request.method == 'POST':
        user_id = str(request.POST.get('user_id',''))
        movie_name=str(request.POST.get('movie_name',''))
        movie_id=str(request.POST.get('movie_id',''))





        data =  {

            "Inputs": {

                    "input1":
                    {
                        "ColumnNames": ["userId", "movieId", "rating"],
                        "Values": [ [ user_id, movie_id, "0" ],  ]
                    },
                    "input2":
                    {
                        "ColumnNames": ["movieId", "title", "genres"],
                        "Values": [ [ movie_id, movie_name, "" ],  ]
                    },        },
                "GlobalParameters": {
               }
        }

        body = str.encode(json.dumps(data))

        url = 'https://ussouthcentral.services.azureml.net/workspaces/80b0369fe0df48308d956e2ddce52806/services/6379155db28f4c91b84e78d268a927f9/execute?api-version=2.0&details=true'
        api_key = "QM46xQupU1HHcA4T3aCyOr9Mohw5kztliXR7AcU5hqZvqIpREZ0GZmIklllje4gjXrM5KKd1boDYpaHVeIP+Ww==" # Replace this with the API key for the web service
        headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

        req = urllib2.Request(url, body, headers) 

        try:
            response = urllib2.urlopen(req)

            # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
            # req = urllib.request.Request(url, body, headers) 
            # response = urllib.request.urlopen(req)

            result = response.read()
            print(result) 
        except urllib2.HTTPError, error:
            print("The request failed with status code: " + str(error.code))

            # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
            print(error.info())

            print(json.loads(error.read())) 

        output=json.loads(result)


        output2= output['Results']

        output3=output2['output1']
        output4=output3['value']


        output_items=output4['ColumnNames']
        output5=output4['Values']
        #print output_movies
        output_movies=0
        for i in output5:
            output_movies=i

    
        for i in range(len(output_items)):

            print output_items[i],output_movies[i]

        finalresult=zip(output_items,output_movies)
 



        return render(request, 'recommender/recommendations.html', {
            'output': finalresult
        })
    return render(request, 'recommender/recommendations.html')

