def longest_word(url):
    import urllib.request
    response_dict = urllib.request.urlopen("https://raw.githubusercontent.com/fpro-admin/recitas/master/words")
    html_dict = set(response_dict.read().decode().split("\n"))
    response_search = urllib.request.urlopen(url)
    html_search = sorted(set(response_search.read().decode().strip("\n").split(" ")))
    return max(html_search, key=lambda i: len(i) if i in html_dict else 0)
