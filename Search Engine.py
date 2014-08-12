def get_page(url):
    try:
        if url == '''url here''':
            return #stuff goes here 
        elif url == '''url here''':
            return #stuff goes here
    except:
        return ""
    return ""

'''
def get_page(url):
    try:
        if url == "http://www.udacity.com/cs101x/index.html":
            return ('<html> <body> This is a test page for learning to crawl! '
            '<p> It is a good idea to '
            '<a href="http://www.udacity.com/cs101x/crawling.html">learn to '
            'crawl</a> before you try to  '
            '<a href="http://www.udacity.com/cs101x/walking.html">walk</a> '
            'or  <a href="http://www.udacity.com/cs101x/flying.html">fly</a>. '
            '</p> </body> </html> ')
        elif url == "http://www.udacity.com/cs101x/crawling.html":
            return ('<html> <body> I have not learned to crawl yet, but I '
            'am quite good at '
            '<a href="http://www.udacity.com/cs101x/kicking.html">kicking</a>.'
            '</body> </html>')
        elif url == "http://www.udacity.com/cs101x/walking.html":
            return ('<html> <body> I cant get enough '
            '<a href="http://www.udacity.com/cs101x/index.html">crawling</a>! '
            '</body> </html>')
        elif url == "http://www.udacity.com/cs101x/flying.html":
            return ('<html> <body> The magic words are Squeamish Ossifrage! '
            '</body> </html>')
        elif url == "http://top.contributors/velak.html":
            return ('<a href="http://top.contributors/jesyspa.html">'
        '<a href="http://top.contributors/forbiddenvoid.html">')
        elif url == "http://top.contributors/jesyspa.html":
            return  ('<a href="http://top.contributors/elssar.html">'
        '<a href="http://top.contributors/kilaws.html">')
        elif url == "http://top.contributors/forbiddenvoid.html":
            return ('<a href="http://top.contributors/charlzz.html">'
        '<a href="http://top.contributors/johang.html">'
        '<a href="http://top.contributors/graemeblake.html">')
        elif url == "http://top.contributors/kilaws.html":
            return ('<a href="http://top.contributors/tomvandenbosch.html">'
        '<a href="http://top.contributors/mathprof.html">')
        elif url == "http://top.contributors/graemeblake.html":
            return ('<a href="http://top.contributors/dreyescat.html">'
        '<a href="http://top.contributors/angel.html">')
        elif url == "A1":
            return  '<a href="B1"> <a href="C1">  '
        elif url == "B1":
            return  '<a href="E1">'
        elif url == "C1":
            return '<a href="D1">'
        elif url == "D1":
            return '<a href="E1"> '
        elif url == "E1":
            return '<a href="F1"> '
    except:
        return ""
    return ""
'''	
	
def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1: 
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)

def get_all_links(page):
    links = []
    while True:
        url,endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links

'''
def record_user_click(index,keyword,url):
    for entry in index:
        if entry[0] == keyword:
            for pair in entry[1]:
                if pair[0] == url:
                    pair[1] = pair[1] + 1
            return

def add_to_index(index, keyword, url):
    for entry in index:
        if entry[0] == keyword:
            for pair in entry[1]:
                if url in pair:
                    return     
            return entry[1].append([url,0])
    index.append([keyword, [[url, 0]]])
'''
			
def add_to_index(index, keyword, url):
    for entry in index:
        if entry[0] == keyword:
			if not url in entry[1]: 
				entry[1].append(url) 
				return
	if lookup(index, keyword) == None: 
		index.append([keyword, [url]])
	
def add_page_to_index(index, url, content):
    words = content.split()
    for word in words:
        add_to_index(index, word, url)

def lookup(index, keyword):
    for entry in index:
        if entry[0] == keyword:
            return entry[1]	
	
def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
	index[]
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
			content = get_page(page)
			add_page_to_index(index, page, content)
			union(tocrawl, get_all_links(content))
			crawled.append(page)
    return index

'''
def crawl_web(seed, max_pages):
    tocrawl = [seed]
    crawled = []
	the_max = max_pages
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
			crawled.append(page)
            links = get_all_links(get_page(page))
            union(tocrawl,links)
			if len(crawled) >= the_max:
				break
    return crawled          

def crawl_web(seed,max_depth):
    page_in_depth, current_depth = 1,0
    tocrawl = [seed]
    crawled = []
    while tocrawl and current_depth <= max_depth:
        page = tocrawl.pop(0)
        page_in_depth -= 1
        if page not in crawled:
            union(tocrawl, get_all_links(get_page(page)))
            crawled.append(page)
            if page_in_depth == 0:
                page_in_depth = len(tocrawl)
                current_depth += 1
    return crawled
'''