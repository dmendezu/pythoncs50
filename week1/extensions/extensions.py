import mimetypes

strIn=input('Insert file name wiht extension ').lower().strip()

if strIn.find('.')!=-1:
    fileT=strIn.rsplit('.',1)[1]
    if fileT!='':
        print(mimetypes.types_map['.'+fileT])
else:
    print('application/octet-stream')