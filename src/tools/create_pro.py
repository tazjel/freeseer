#!/usr/bin/python

from os import listdir;

LANGAUGE_DIRECTORY = '../freeseer/frontend/default/languages';   
MAIN_DIRECTORY = '../freeseer/frontend/default';  
FORM_DIRECTORY = '../freeseer/frontend/default/forms';  

#Retrieve source , ui and language files 
src_files = listdir(MAIN_DIRECTORY);
ui_files =  listdir(FORM_DIRECTORY);
qm_files =  listdir(LANGAUGE_DIRECTORY);

#Select valid src files that end in .py
src_files = map(lambda x:x.split('.'),src_files);
src_files = filter(lambda x: x[len(x)-1]=='py',src_files);

#Select the valid ui files that end in .ui
ui_files = map(lambda x:x.split('.'),ui_files);
ui_files = filter(lambda x: x[len(x)-1]=='ui',ui_files);


#Select the language prefixes from the .qm files 
qm_files = map(lambda x: x.split('.'),qm_files);
qm_files = filter(lambda x: x[len(x)-1] == 'qm' , qm_files);
qm_files = map(lambda x: (x[0].split("_"))[1],qm_files);



#Retrieve system languages 
try:
  language_file = open('languages.txt' , 'r');
  languages = language_file.readlines();
  languages = map(lambda x: x.rstrip() , languages);
  language_file.close();
except:
  languages = qm_files;
  
  
#Generate the project file    
print('SOURCES = \\');
for i in range(0,len(src_files)):
  end = '\\';
  if(i == len(src_files)-1):
    end = '';
  print(MAIN_DIRECTORY+"/"+src_files[i][0]+'.'+src_files[i][1] + ""+ end);
  
print('FORMS = \\');
for i in range(0,len(ui_files)):
  end = '\\';
  if(i == len(ui_files)-1):
    end = '';
  print(FORM_DIRECTORY+"/"+ui_files[i][0]+'.'+ui_files[i][1] + ""+ end);

print('TRANSLATIONS = \\');
for i in range(0,len(languages)):
  end = '\\';
  if(i == len(languages)-1):
    end = '';
  print(LANGAUGE_DIRECTORY+"/"+'tr_'+languages[i] + ".ts" + end);

  
