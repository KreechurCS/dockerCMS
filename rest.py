import os

selection = 0
id = 0
while selection != 13:
    print("==========MENU===========")
    print("=Enter a value to select=")
    print("= 1. Get all Containers =")
    print("= 2. Get all running con=")
    print("= 3. Get all images     =")
    print("= 4. Inspect an image   =")
    print("= 5. Delete all con     =")
    print("= 6. Delete a container =")
    print("= 7. Delete all images  =")
    print("= 8. Delete an image    =")
    print("= 9. Create a container =")
    print("= 10. Create an image   =")
    print("= 11. Update Container  =")
    print("= 12. Update and image  =")
    print("= 13. Exit              =")
    print("=========================")
    selection = int(raw_input("select an option"))
    if selection == 13:
        break
    elif selection == 1:
        # Get all containers
        os.system("curl -s -X GET -H 'Accept: application/json' http://35.187.185.180:8080/containers | python -mjson.tool")
    elif selection == 2:
        # get all running containers
        os.system("curl -s -X GET -H 'Accept: application/json' http://35.187.185.180:8080/containers?state=running | python -mjson.tool")
    elif selection == 3:
        # get all images
        os.system("curl -s -X GET -H 'Accept: application/json' http://35.187.185.180:8080/images | python -mjson.tool")
    elif selection == 4:
        # inspect an image
        id = raw_input("Select an image id")
        os.system("curl -s -X GET -H 'Accept: application/json' http://35.187.185.180:8080/containers/%s | python -mjson.tool" % id)
    elif selection == 5:
        # Delete all containers
        os.system("curl -s -X DELETE -H 'Accept: application/json' http://35.187.185.180:8080/containers")
    elif selection == 6:
        #Delete a specific container
        id = raw_input("Select a container to delete")
        os.system("curl -s -X DELETE -H 'Accept: application/json' http://35.187.185.180:8080/containers/%s" % id)
    elif selection == 7:
        #delete all images
        os.system("curl -s -X DELETE -H 'Accept: application/json' http://35.187.185.180:8080/images")
    elif selection == 8:
        #delete a specific image
        id = raw_input("Select an image to delete:")
        os.system("curl -s -X DELETE -H 'Accept: application/json' http://35.187.185.180:8080/images/%s" % id)
    elif selection == 9:
        #Create a new container
        id = raw_input("select Image ID/Name:")
        os.system(
            "curl -X POST -H 'Content-Type: application/json' http://35.187.185.180:8080/containers -d '{\"image\": \"%s\"}'" % id)
    elif selection == 10:
        #Create a new image
        os.system("curl -H 'Accept: application/json' -F file=@Dockerfile http://35.187.185.180:8080/images")
    elif selection == 11:
        #update container
        id = raw_input("Select a Container:")
        while True:
            change = raw_input("Please Enter 1 to change to running, 2 to change to stopped:")
            if change == '1':
                os.system(
                    "curl -X PATCH -H 'Content-Type: application/json' http://35.187.185.180:8080/containers/%s -d '{\"state\": \"running\"}'" % id)
                break
            elif change == '2':
                os.system(
                    "curl -X PATCH -H 'Content-Type: application/json' http://35.187.185.180:8080/containers/%s -d '{\"state\": \"stopped\"}'" % id)
                break
            else:
                print "Unknown Option Selected!"
    elif selection == 12:
        #Update an image
        id = raw_input("Select an Image:")
        os.system(
            "curl -s -X PATCH -H 'Content-Type: application/json' http://35.187.185.180:8080/images/%s -d '{\"tag\": \"test:1.0\"}'" % id)




