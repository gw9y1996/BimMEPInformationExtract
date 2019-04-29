/**
 * @description:   系统信息提取与展示
 */
let systemFlag = false;
// 初始化，主函数
const init = () => {
  vizbim.resize();
  vizbim.showModelByDocumentId(filekey, function () {
    const promptingMessage1 = vizbim.promptingMessage(
      "info", "系统数据获取中，请稍等...",
      false
    );    // 模型弹出框
    getSystemTreeComponents(filekey)
      .then(data => {
        promptingMessage1.remove();
        initTree(getSystemTreeNodes(data.data));
        initTree(data1)
      })
      showSystemComponents();  // 展示构件内系统列表
      showSystemComponents1();
      addRestorButton(); 
      vizbim.listentoSelectObjs(function (componentId, component) {
        console.log("componentId:",componentId);
        console.log("component",component);
        if (componentId) {    // 如果选中构件的时候可以拿到这个构件id，则执行下面的逻辑
          vizbim.restoreObjtColor();
          vizbim.setObjtColor([componentId], [0, 1, 0]);
          if (!systemFlag) {
            getComponentinformationAttributesByComponentId(componentId)
              .then(data =>{
                const CPattributes = data.data
                $("#attributeContent1").children().remove();
                for (intm in CPattributes) {
                  console.log(intm)
                  $("#attributeContent1").append(
                    '  <div class="layui-card-header"style="background-color:#B0E2FF">' +
                    intm +
                    '</div>' +
                    '  <div id="systemComponents" >' +
                    '  </div>'
                  );
                  for(line in CPattributes[intm])
                  $("#attributeContent1").append(
                    '  <div class="layui-card-header" style="overflow:hidden;">' +
                    line +
                    ' '+
                    '___'+
                    ' '+
                    CPattributes[intm][line]+
                    '</div>' +
                    '  <div id="systemComponents";>' +
                    '  </div>'
                  );
                }
              });

            getComponentSystemIdByComponentId(componentId)
              .then((data) => data.data)
              .then(systemId => {
                getComponentinformationByComponentId(systemId).then((data1) => {
                  const systemInfomation = data1.data;
                  const systemgroup = systemInfomation.systemgroup;  // 一个系统的构件的systemgroup属性值一样
                  const systemType = systemInfomation.systemtype;  // 一个系统的构件的systemgroup属性值一样
                  $("#attributeContent").children().remove();
                  systemFlag = true;
                  const componentIds = systemgroup;
                  if (componentIds && componentIds.length > 0) {
                    $("#attributeContent").append(
                      '  <div class="layui-card-header"style="background-color:#B0E2FF">' +
                      systemType +
                      '</div>' +
                      '  <div id="systemComponents" class="layui-card-body">' +
                      '  </div>'
                    );
                    vizbim.hideObjs(vizbim.alloids);
                    vizbim.showObjs(componentIds);
                    componentIds.forEach(item => {
                      const idItem = item.substring(0,23) + "...";
                      const componentItem = $(`<p 
                      style="cursor: pointer;padding-right: 10px" 
                      id=${item}
                      title=${item}
                      >
                          ${idItem}
                      </p>`);
                      $("#systemComponents").append(componentItem);
                      document.getElementById(item).onclick = function () {
                        onClickComponent(item)
                      };
                      
                    })
                  }
                })
              });
          }
        }
      });
  });
}

// 添加左侧树
const initTree = (tree) => {
  $('#tree').treeview({
    data: tree,
    collapseIcon: "glyphicon glyphicon-minus",
    expandIcon: 'glyphicon glyphicon-plus',
    onNodeSelected: function (event, data) {
      console.log("点中的data--", data);
      const hightArray = data.componentArray;
      vizbim.resetScene(false, false, false, true, true, false);
      vizbim.adaptiveSize(hightArray);
      vizbim.reverseTransparentObjs(hightArray, 0.4, true);
    },
    onNodeUnselected: (event, data) => {
      vizbim.resetScene(true, true, true, true, true, true);
    }
  });
  $('#tree').treeview('collapseAll', {silent: true});
}

// 获取模型系统树结构
const getSystemTreeComponents = (filekey) => {
  return fetch(`${op.baseaddress}models/${filekey}/components/system?devcode=${op.devcode}`)
    .then(response => response.json())
}

// 将系统树接口返回的数据加工成bootstraptreeview所需要的node数据结构
const getSystemTreeNodes = (arr) => {
  var tree = [];
  for (var i = 0; i < arr.length; i++) {
    var node = {};
    node.id = arr[i].key;
    node.text = arr[i].systemtype;
    node.componentArray = arr[i].systemgroup;
    tree.push(node);
  }
  
  return tree;
 
};

document.write("<script language=javascript src='data.json?callback=data1'></script>");
function data1 (result){  
  console.log(result);  
  var tree1 = JSON.stringify(result);
  console.log(tree1);
  return tree1
}



// 构件点击事件，当点击左侧系统树控制台时，将对应的构件回复高亮并且聚焦
const onClickComponent = (componentId) => {
  $("#systemComponents").find("p").css('background', '');
  document.getElementById(componentId).style.background = '#70b1c5';
  const comArray = [componentId];
  vizbim.restoreObjtColor();   // 恢复构件颜色
  vizbim.setObjtColor(comArray, [0, 1, 0]);  // 设置构件颜色
  vizbim.adaptiveSize(comArray);  // 适应构件视角
}

// 数据接口：根据构件id 获取此构件所属的系统id
const getComponentSystemIdByComponentId = (componentId) => {
  return fetch(`${op.baseaddress}models/${filekey}/components/${componentId}/get/systempoint?devcode=${op.devcode}`)
    .then(response => response.json())
}


// 数据接口：根据构件的id，返回这个构件的systemtype
const getComponentinformationByComponentId = (componentId) => {
  return fetch(`${op.baseaddress}models/${filekey}/components/${componentId}/primary?devcode=${op.devcode}`)
    .then(response => response.json())
}
//数据接口：根据构件的id，返回这个构件的attributeshttps://api.bos.xyz/models/{fileKey}/components/{componentKey}/attributes
const getComponentinformationAttributesByComponentId = (componentId) => {
  return fetch(`${op.baseaddress}models/${filekey}/components/${componentId}/attributes?devcode=${op.devcode}`)
    .then(response => response.json())
}


// 显示左侧系统树的操控台
const showSystemComponents = () => {
  // 创建指引说明
  /*$("body").append(
    "<div " +
    "style = 'position: absolute;" +
    "top: 20px;" +
    "left: 15px;" +
    "font-size:18px'>" +
    "先选择想要查询的构件" +
    "</div>"
  )
  */
  const Lobibox = vizbim.Lobibox;  // vizbim框对象，目的是调用vizbim封装好的显示出一个边框容器

  // 创建边框容器的属性配置
  const attribute = {
    title: '系统内构件列表',
    width: 300,
    height: 500,
    closeOnEsc: false,
    closeButton: false,
    content: '<div id="attributeContent" class="layui-card"></div>'
  };
  attributeWindow = Lobibox.window(attribute);
  attributeWindow.setPosition({
    left: 1450,
    top: 60,
    //position :absolute
  });
}

const showSystemComponents1 = () => {
  // 创建指引说明
  /*$("body").append(
    "<div " +
    "style = 'position: absolute;" +
    "top: 20px;" +
    "left: 15px;" +
    "font-size:18px'>" +
    "先选择想要查询的构件" +
    "</div>"
  )
  */
  const Lobibox = vizbim.Lobibox;  // vizbim框对象，目的是调用vizbim封装好的显示出一个边框容器

  // 创建边框容器的属性配置
  const attribute = {
    title: '构件属性列表',
    width: 300,
    height: 400,
    closeOnEsc: false,
    closeButton: false,
    content: '<div id="attributeContent1" class="layui-card"></div>'
  };
  attributeWindow = Lobibox.window(attribute);
  attributeWindow.setPosition({
    left: 1450,
    top: 400
  });
}

// 创建复位按钮,目的是点击按钮的时候将模型回复到初始状态
const addRestorButton = () => {
  const toolId = vizbim.uuid;
  const toolbar = $('<div style="margin-left:0" class="yj-tool" id="my-tool' + toolId + '" ></div>');
  toolbar.appendTo($("#" + vizbim.viewport));
  //group1
  const group1 = $('<div class="yj-group"></div>');
  group1.appendTo(toolbar);
  const $toolHome = $('<button type="button" class="yj-but" title="初始化" id="home' + toolId + '"><div class="yj-icon home-icon" ></div></button>');
  $toolHome.appendTo(group1);
  $toolHome.click(() => {
    systemFlag = false;
    vizbim.resetScene();
    $("#attributeContent").children().remove();
  });
}
