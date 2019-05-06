# coding = utf-8
import requests
import os
import re
import webbrowser
import json
import xlwt
# import pandas
Gjlist = []
fileName = 'index.html'
a = 0
def Getlist(ID,Key):
    url = "https://api.bos.xyz/models/" + ID + "/outlines"
    querystring = {"devcode":Key }
    response = requests.request("GET", url, params=querystring)
    # print(response.text)
    Gjlist = response.text
    text = response.json()
    i = 0
    global a
    if a == 0 :
        workbook = xlwt.Workbook()
        sheet1 = workbook.add_sheet('sheet1',cell_overwrite_ok=True)
        for y in text['data']:
            sheet1.write(i,0,y)
            i += 1
        workbook.save(ID + '构建列表.xls')
        a += 1
    # print (Gjlist.find('['))
    # print (Gjlist.find(']'))
    new = Gjlist[Gjlist.find("[") + 1 : Gjlist.find("]") - 1]
    # print (re.sub('"','',new))
    new2 = re.sub('"', "", new)
    global new1_list
    # print(new2.split(','))
    new1_list = new2.split(",")
    # print(new1_list )
    #file = open("构建列表.txt", "w",encoding='utf8')
    #for line in new1_list:
        #file.write(line + "\n")
    #file.close()
    return new1_list


def Gettext(text_list,id,Key):
    #file1 = open("构建信息.txt", "w",encoding='utf8')
    i = 0
    workbook = xlwt.Workbook()
    sheet1 = workbook.add_sheet('sheet1',cell_overwrite_ok=True)
    for line in text_list:
        url1 = "https://api.bos.xyz/models/"+id+"/components/" + line + "/primary"
        querystring = {"devcode": Key }
        response = requests.request("GET", url1, params=querystring)
        text = response.json()
        #批量写入Excel
        if i == 0:
            x = 0
            for y in text['data'].keys() :
                sheet1.write(0,x,y)
                x += 1
            i += 1
        #print(type(text))
        #print(text['data'].keys())
        a = 0
        for key1 in text['data'].keys() :
            if type(text['data'][key1]) == list :
                sheet1.write(i,a,' '.join('%s' %n for n in text['data'][key1]))
            else:
                sheet1.write( i ,a ,text['data'][key1])
            a += 1
        i += 1
        #print(text['data'][])
       # print(response.text)
        #file1.write(response.text + "\n")
    workbook.save(id+'构建信息.xls')
    #file1.close()


# https://api.bos.xyz/models/{fileKey}/components/{componentKey}/attributes
def Getattribute(id,Key):
    url = "https://api.bos.xyz/models/" + id + "/export/excel/attributes"
    querystring = {"devcode":Key}
    response = requests.request("GET", url,params=querystring)
    with open(id + "构建属性.xlsx", "wb") as code:
        code.write(response.content)
b = 0
def GetTreelist (IDnum,Key):
    url = "https://api.bos.xyz/models/" + IDnum + "/components/system"
    querystring = {"devcode":Key}
    response = requests.request("GET", url,params=querystring)
    # print(response.text)
    Gjlist = response.text
    #print (Gjlist.find('['))
    #print (Gjlist.find(']'))
    new = Gjlist[Gjlist.find('[')+2:]
   # print (re.sub('},{','',new))
   # new2 = re.sub('"','',new)
   # global new1_list
   # print(new.split('},{'))
    new1_list = new.split('},{')
   # print(new1_list)
    workbook = xlwt.Workbook()
    sheet1 = workbook.add_sheet('sheet1',cell_overwrite_ok=True)
    text = response.json()
    print(text['data'])
    
    
    global b
    if b == 0:
        workbook = xlwt.Workbook()
        sheet1 = workbook.add_sheet('sheet1',cell_overwrite_ok=True)
        for z in text['data']:
            i = 0
            for y in text['data'][i]:
                sheet1.write(i,0,text['data'][i]['key'])
                sheet1.write(i,1,text['data'][i]['name'])
                i += 1
        b += 1
        workbook.save(IDnum + '系统列表.xls')
    return new1_list

class Tree:
    def __init__(self,val):
        self.val = val
    name = ""
    id = ''
    systemgroup = []

def obj_to_json(obj):
    return{
        "id":obj.id ,
        "text":obj.name ,
        "componentArray":obj.systemgroup ,
    }

def GetTree (text_list,ID):
    data_list = []
    i=0
    
    Tree_list = []
    d = {}
    workbook = xlwt.Workbook()
    sheet1 = workbook.add_sheet('sheet1',cell_overwrite_ok=True)
    for line in text_list:
        d['t'+str(i)]=Tree(i)
        
        data_list.append([])
        # print(line.find('name'))
        # print(line.find('"', line.find('name') + 8, line.find('name') +20))
        id = line[line.find('id') + 5:line.find('"', line.find('id') + 6, line.find('id') + 49)]
        key = line[line.find('key') + 6:line.find('"', line.find('key') + 6, line.find('key') + 38)]
        guid = line[line.find('guid') + 7:line.find('"', line.find('guid') + 7, line.find('guid') + 38)]
        name = line[line.find('name') + 7:line.find('"', line.find('name') + 7)]
        systemtype = line[line.find('systemtype') + 13:line.find('"', line.find('systemtype') + 13, line.find('systemtype') + 38)]
        systemgroup = line[line.find('systemgroup') + 14:line.find(']')-1]
        # print(systemgroup)
        d['t'+str(i)].id=key
        d['t'+str(i)].name = systemtype
        # print(d't'+str(i).name)
        newsys = re.sub('"', "", systemgroup)
        d['t'+str(i)].systemgroup = newsys.split(',')
        data_list[i].append(key)
        data_list[i].append(id)
        data_list[i].append(guid)
        data_list[i].append(name)
        data_list[i].append(systemtype)
        data_list[i].append(systemgroup)
        Tree_list.append(d['t'+str(i)])
        # print(data_list)
        # print(Tree_list[i])
        
        
        if i == 0 :
            sheet1.write(i,0,'key')
            sheet1.write(i,1,'id')
            sheet1.write(i,2,'guid')
            sheet1.write(i,3,'name')
            sheet1.write(i,4,'systemtype')
            sheet1.write(i,5,'systemgroup')
        x = 0
        for y in data_list[i]:
            sheet1.write(i+1,x,y)
            x += 1 
        i+=1
    workbook.save( ID + '系统数据.xls')
        
    return Tree_list


def jsongo(id,Key):
    data = GetTree(GetTreelist(id,Key),id)
    jsfilename = "data.json"
    fi=open(jsfilename,"w",encoding = "utf-8")
    nlist = []
    t = []
    c = 0
    d = 0
    SyschName = ['防排烟','回风','送风','喷淋系统','其他消防系统','家用冷水','空调冷水','家用热水','自喷系统','循环供水','循环回水','排风']
    for treedata in data:
        t.append(treedata.name)
    for i in data:
        for line in data:
            #print(nlist.count(line.name))
            #print(t.count(line.name))
            if nlist.count(line.name)>0 and t.count(line.name)>1:
                #print(nlit.count())
                x=t.index(line.name)
                z = data[x].systemgroup
                data.pop(x)
                t.pop(x)
                y = t.index(line.name)
                data[y].systemgroup.extend(z)
            else :
                nlist.append(line.name)
    for i in data:
        print(data[c].name)
        print(isAllChinese(data[c].name))
        if isAllChinese(data[c].name):
            c += 1
        else:
            print (type(data[c].name))
            print(SyschName[d])
            print(type(SyschName[d]))
            data[c].name = SyschName[d]
            d += 1
            c += 1   
    json.dump(data,fi,default=obj_to_json,ensure_ascii=False)
    fi.close()
    with open('data.json','r+',encoding = 'utf-8') as f:
        content = f.read()
        f.seek(0,0)
        f.write("data1 = '" +content+"'")
    f.close()

#json = json.dumps(data,default=obj_to_json)
#print(json)

def writeHtml (id,key):
    f = open(fileName,'w',encoding = "utf-8")
    message ="""
    <!DOCTYPE html>
    <html>
    <title>系统信息提取与展示</title>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
        <link rel="icon" href="https://www.bos.xyz/vizbim/img/redblock.ico" type="img/x-ico"/>
        <link rel="stylesheet" href="https://www.bos.xyz/vizbim/fontawesome5.4.1/css/all.css">
        <link rel="stylesheet" href="https://www.bos.xyz/vizbim/BIMWINNER.viewer.min.css"/>
        <link rel="stylesheet" href="https://www.bos.xyz/vizbim/layui/css/layui.css"/>
        <link rel="stylesheet" href="style.css"/>
    </head>
    <body style="overflow-y: hidden">
    <div id="viewport" style="width: 1920px; height: 1080px;" ></div>
    <div id="tree"
        style="width: 180px; position: absolute; height: 400px;top:80px; left:30px;"></div>

    <script type="text/javascript" src="https://www.bos.xyz/vizbim/jquery.min.js"></script>
    <script type="text/javascript" src="https://www.bos.xyz/vizbim/bootstrap-treeview.min.js"></script>
    <script type="text/javascript" src="https://www.bos.xyz/vizbim/spectrum.js"></script>
    <script type="text/javascript" src="https://www.bos.xyz/vizbim/jquery-ui.js"></script>
    <script type="text/javascript" src="https://www.bos.xyz/vizbim/three.min.js"></script>
    <script type="text/javascript" src="https://www.bos.xyz/vizbim/jszip.min.js"></script>
    <script type="text/javascript" src="https://www.bos.xyz/vizbim/BIMWINNER.viewer.min.js"></script>
    <script type="text/javascript" src="https://www.bos.xyz/vizbim/layui/layui.js"></script>
    <script type="text/javascript" src='https://www.bos.xyz/vizbim/html2canvas.min.js'></script>
    <script type="text/javascript" src="index.js"></script>
    <script type="text/javascript" src="data.json?callback=data1"></script>
    <script type="text/javascript">

    //  配置三维主对象参数
    const op = {
        viewport: "viewport",
        devcode: "%s",
        baseaddress: 'https://api.bos.xyz/',
        viewController: false        //不加载左上角视图球
    };
    // 初始化主对象
    const vizbim = new BIMWINNER.Viewer(op);
    const filekey = "%s"; // 模型文件key
    // 运行主函数
    init(filekey); 

    </script>
    </body>
    </html>"""%(key,id)
    f.write(message)
    f.close()
def isAllChinese(s):
    for c in s:
        if ('\u4e00' <= c <= '\u9fa5'):
            return True
    return False


def runall(ID,KEY):
    global a 
    a = 0
    global b 
    b = 0
    if os.path.exists("data.json"): # 如果文件存在
        os.remove("data.json") # 则删除
    Getlist(ID,KEY)
    GetTreelist(ID,KEY)
    GetTree(GetTreelist(ID,KEY),ID)
    jsongo(ID,KEY)
    writeHtml(ID,KEY)
    webbrowser.open(fileName)
    Gettext(Getlist(ID,KEY),ID,KEY)
    Getattribute(ID,KEY)