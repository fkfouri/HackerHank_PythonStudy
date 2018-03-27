"""
Modify the following google_sector_report so that it returns a json 
dump that contains the following information about each sector:
1. The sector name
2. The percentage change in sector value
3. The biggest gainer and the percentage change in the biggest gainer
4. The biggest loser and the percentage change in the biggest loser

The structure of the json is given in the assignment description on EdX.

Note:
To read files, use:

with open('filename') as f:
    lines = f.readlines()
"""

dd = 'E:\\Projetos\\HackerHank_PythonStudy\\Udemy\\library and functions\\GetDataFrom_WEB\\Problema_EDX\\'
def openFile(ref):
    with open(dd + ref + '.htm') as f:
        return f.readlines()



def google_sector_report():
    import requests
    from bs4 import BeautifulSoup

    json_string = {}
    json_string['result'] = {}

    content = openFile('Google Finance') 
    myPage = BeautifulSoup(' '.join(content),'lxml') 

    sector = myPage.find('div', {'id': 'secperf'})
    lines = sector.find_all('a')
    spans = sector.find_all('span')
    print(lines)
    print(spans)
    


    files = ['Energy']#, 'Basic Materials', 'Industrials']



    for file in files:
        temp = {}
        temp[file] = {}
        content = openFile(file)
        myPage = BeautifulSoup(' '.join(content),'lxml') 

        topmovers = myPage.find('table', {'class': 'topmovers'})
        lines = topmovers.find_all('tr')

        def readLine(num):
            myline = BeautifulSoup(str(lines[num]),'lxml') 
            equity = myline.find('a').get_text()
            change = myline.select('span')[1].get_text().replace('(','').replace(')','')
            return {"equity" : equity, "change" : change}

        temp[file] ={"biggest_gaineir" :readLine(1), "biggest_loser": readLine(7), "change" : 0}
        #print(temp)



       
    
    
    import json
    return json.dumps(json_string)

print(google_sector_report())