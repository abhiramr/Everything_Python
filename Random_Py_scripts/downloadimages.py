import urllib
count=1
while count < 31:
    urllib.urlretrieve("https://newevolutiondesigns.com/images/freebies/black-wallpaper-"+str(count)+".jpg", str(count)+".jpg")
    urllib.urlretrieve("https://newevolutiondesigns.com/images/freebies/conceptual-wallpaper-"+str(count)+".jpg",str(count)+"s.jpg")
    count=count+1
