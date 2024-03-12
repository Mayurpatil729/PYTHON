#### Creating Templates 

1. Start project
2. Start application
3. Create templates folder in our main project folder
4. Add application in the settings. py
    import os
    BASE_DIR = Path(__file__).resolve().parent.parent
    BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    TEMPLATE_DIR=os.path.join(BASE_DIR,'templates')

    'DIRS': [TEMPLATE_DIR]

5. Define View function
6. Define Url pattern
7. Runserver
8. Send the request





demoproject1
    templates
        testapp1
            .results.html
            .html
        testapp2
            .html
    manage. py
    demoproject
        init
        sesttings
        urls


#### Notes

Python related business code -- > View.py
HTML related Presentation Logic--> Temp1ate


























