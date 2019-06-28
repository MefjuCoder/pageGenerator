def closeAll():
    index.close()
    podstrona1.close()
    podstrona2.close()
    podstrona3.close()
    podstrona4.close()
    css.close()
a=[0,1,2,3,4]
index= open("index.html", "w")
index.write("<! DOCTYPE html><head><link rel='stylesheet' href='style.css' type='text/css' /></head></html>")

podstrona1= open("podstrona1.html", "w")
podstrona1.write("<! DOCTYPE html><head><link rel='stylesheet' href='style.css' type='text/css' /></head></html>")

podstrona2= open("podstrona2.html", "w")
podstrona2.write("<! DOCTYPE html><head><link rel='stylesheet' href='style.css' type='text/css' /></head></html>")

podstrona3= open("podstrona3.html", "w")
podstrona3.write("<! DOCTYPE html><head><link rel='stylesheet' href='style.css' type='text/css' /></head></html>")

podstrona4= open("podstrona4.html", "w")
podstrona4.write("<! DOCTYPE html><head><link rel='stylesheet' href='style.css' type='text/css' /></head></html>")

css = open("style.css","w")
css.write("p{ line-height: 3px}")

closeAll()

