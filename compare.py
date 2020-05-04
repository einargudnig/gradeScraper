import difflib

path = 'C:\\Users\\Einar\\Desktop\\pythonScraper\\'
file1 = path+'origin.html'
file2 = path+'test.html'


f1 = open(file1, 'r').readlines()
f2 = open(file2, 'r').readlines()


diff = difflib.HtmlDiff().make_file(f1, f2, file1, file2)

diffReport = open(path+'diff.html', 'w')

diffReport.write(diff)



#resultFile.write(htmldiffs)
#print(htmldiffs)