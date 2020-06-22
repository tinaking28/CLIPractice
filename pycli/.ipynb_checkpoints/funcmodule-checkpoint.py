def my_function():
    import json

    with open('pycli/campaigndata.json') as j:
      campaign_data = json.load(j)

    print(campaign_data)
    print('text from my_function :: {}'.format(campaign_data['name']))
    
    h = open('body.html','w')

    message = """
     <html>
        <body>
        <!-- beginning of standard header section -->
        …
            <!-- Logo and sign in button table -->
            <table border="0" cellpadding="0" cellspacing="0" class="table90" width="670">
        ...                                        
            </table>
        <!-- end of standard header section -->
        <!-- beginning of custom body section -->



        <!-- end of custom body section -->
        <!-- beginning of standard footer section -->
            <!-- prevent gmail app from auto-resizing email -->
            <table width="700" border="0" cellpadding="0" cellspacing="0" class="hide" id="spacer-700" style="width:700px;max-width:700px;min-width:700px; bgcolor:#ffffff;">
        …
            </table>
        <!-- end of standard footer section -->
        </body>
    </html>"""

    h.write(message)
    h.close()
    
    

