# Google Image Scrapper

![](http://ForTheBadge.com/images/badges/made-with-python.svg)



## You will need docker to run the application


## Run the following command to run the application

```console
docker build --tag google_image:1.0 .
docker run --name google_image_flask -p 8000:8000 -v ~/simple_images:/opt/simple_images google_image:1.0
```
- Your downloaded images will be at ~/simple_images

***The real craft is scrapper.py module which can be engineered according to your use case***
