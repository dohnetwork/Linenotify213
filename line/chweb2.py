import urllib.request, urllib.error

url = 'http://saraban.doh.go.th/DipWeb/'
try:
    conn = urllib.request.urlopen(url)
except urllib.error.HTTPError as e:
    # Return code error (e.g. 404, 501, ...)
    # ...
    print(e.code)
except urllib.error.URLError as e:
    # Not an HTTP-specific error (e.g. connection refused)
    # ...
    print('URLError')
else:
    # 200
    # ...
    print('good')
