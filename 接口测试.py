# coding = utf-8
import requests
import os
import re
import webbrowser
import json
# import pandas
Gjlist = []
fileName = 'index.html'
def Getlist(ID,Key):
    url = "https://api.bos.xyz/models/" + ID + "/outlines"
    querystring = {"devcode":Key }
    response = requests.request("GET", url, params=querystring)
    # print(response.text)
    Gjlist = response.text
    # print (Gjlist.find('['))
    # print (Gjlist.find(']'))
    new = Gjlist[Gjlist.find("[") + 1 : Gjlist.find("]") - 1]
    # print (re.sub('"','',new))
    new2 = re.sub('"', "", new)
    global new1_list
    # print(new2.split(','))
    new1_list = new2.split(",")
    # print(new1_list )
    file = open("构建列表.txt", "w",encoding='utf8')
    for line in new1_list:
        file.write(line + "\n")
    file.close()
    return new1_list


def Gettext(text_list,id,Key):
    file1 = open("构建信息.txt", "w",encoding='utf8')
    for line in text_list:
        url1 = "https://api.bos.xyz/models/"+id+"/components/" + line + "/primary"
        querystring = {"devcode": Key }
        response = requests.request("GET", url1, params=querystring)
       # print(response.text)
        file1.write(response.text + "\n")
    file1.close()


# https://api.bos.xyz/models/{fileKey}/components/{componentKey}/attributes
def Getattribute(text_list,id,Key):
    file1 = open("构建属性.txt", "w",encoding='utf8')
    for line in text_list:
        url1 = "https://api.bos.xyz/models/"+id+"/components/" + line + "/attributes"
        querystring = {"devcode": Key }
        response = requests.request("GET", url1, params=querystring)
       # print(response.text)
        file1.write(line + ' | ' + response.text + "\n")
    file1.close()

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

    file = open('系统列表.txt','w',encoding='utf8')
    for line in new1_list:
        file.write(line+'\n')
    file.close()
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

def GetTree (text_list):
    data_list = []
    i=0
    Tree_list = []
    d = {}
    file1 = open('系统数据.txt','w',encoding='utf8')
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
        i+=1
        for line1 in data_list:
            for line2 in line1:
                file1.write(line2 + ' | ')
            file1.write('\n')          
    file1.close()
    return Tree_list


def jsongo(id,Key):
    data = GetTree(GetTreelist(id,Key))
    jsfilename = "data.json"
    fi=open(jsfilename,"w",encoding = "utf-8")
    nlist = []
    t = []
    i=0
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
            else:
                nlist.append(line.name)
    
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
    </head>
    <body style="overflow-y: hidden">
    <div id="viewport" ></div>
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


def runall(ID,KEY):
    if os.path.exists("data.json"): # 如果文件存在
        os.remove("data.json") # 则删除
    Getlist(ID,KEY)
    #Gettext(Getlist(ID,KEY),ID,KEY)
    Getattribute(Getlist(ID,KEY),ID,KEY)
    GetTreelist(ID,KEY)
    GetTree(GetTreelist(ID,KEY))
    jsongo(ID,KEY)
    writeHtml(ID,KEY)
    webbrowser.open(fileName)
