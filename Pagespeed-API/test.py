import pagespeed
from pagespeed import PageSpeed

ps = PageSpeed()

response = ps.analyse('https://www.example.com', strategy='mobile')
ls = [
    response.url, response.loadingExperience, response.originLoadingExperience,
    response.originLoadingExperienceDetailed,
    response.loadingExperienceDetailed, response.finalUrl,
    response.requestedUrl, response.version, response.userAgent
]  # , response.lighthouseResults]
ps.save(response)
print(ls)
