'''
The code allows converting parametric equations from https://www.wolframalpha.com/
1. Find a person curve on the site
2. Click on 'plain text' below a snippet with equations and copy the text
3. Create an empty file 'Text.txt' on your local computer in a Python project folder where  and paste the text. Close the file
4. Run the script on your computer
5. Open the 'Text.txt' file and copy the text
6. Open a new project in Tableau, create a calculation X and paste the text. There will be 2 strings pasted. 
7. Cut a lower string ad click 'Ok'
8. Create a new calculation 'Y' and paste it, click 'Ok'

Now we have parametric equation for X and Y where t is a variable
'''



import re
import os

with open('Text.txt', encoding='utf-8', mode='r') as g:
  old_data = g.read()
new_data = old_data.replace('θ', 'O')
with open ('Text.txt', encoding='utf-8', mode='w') as g:
  g.write(new_data)

with open('Text.txt', encoding='utf-8', mode='r') as g:
  old_data = g.read()
new_data = old_data.replace(' π', '*PI')
with open ('Text.txt', encoding='utf-8', mode='w') as g:
  g.write(new_data)

replacements2 = {' t': '*t', ' sin': '*sin'}

with open('Text.txt') as infile, open('Text1.txt', 'w') as outfile:
    for line in infile:
        for src, target in replacements2.items():
            line = line.replace(src, target)
        outfile.write(line)

with open('Text1.txt', 'r') as x:
  old_data = x.read()
new_data = re.sub('O\((.*?)\)', r'*IIF(\1<0,0,1)', old_data)
with open ('Text1.txt', 'w') as y:
  y.write(new_data)

with open('Text1.txt', encoding='utf-8', mode='r') as g:
  old_data = g.read()
new_data = old_data.replace('*PI', '*PI()')
with open ('Text1.txt', encoding='utf-8', mode='w') as g:
  g.write(new_data)

replacements = {'-*t' :'-t', '+*t' :'+t', '-*sin' :'-sin', '+*sin' :'+sin', '+*PI()' :'+PI()' , '-*PI()' :'-PI()', 'x(t) =':'', 'y(t) =':'',  '*IIF(sqrt(sgn(sin(t/2<0,0,1))))': '*IIF((sqrt(IF sin([t]/2)<0 THEN -1 ELSEIF sin([t]/2)>0 THEN 1 ELSE 0 END))<0,0,1)'}

with open('Text1.txt') as infile, open('Text.txt', 'w') as outfile:
    for line in infile:
        for src, target in replacements.items():
            line = line.replace(src, target)
        outfile.write(line)

os.remove('Text1.txt')
