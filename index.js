/**
 * @description:   系统信息提取与展示
 */
let systemFlag = false;
// 空间树接口拿到的
let buildingLevel = [];
// layui的form
let form = layui.form;

//构件所有的类别数组
let comTypeArray = [];
// 初始化，主函数
const init = (fileKey) => {
  vizbim.resize();
  vizbim.showModelByDocumentId(filekey, function () {
    const promptingMessage1 = vizbim.promptingMessage(
      "info", "系统数据获取中，请稍等...",
      false 
    );// 模型弹出框
    addTileandSearchBoard(fileKey);    //  创建左侧的搜索区域
    updateLoucengInformation(fileKey); //  根据[数据接口:获取模型对于的空间树的楼层信息]更新楼层选项的值
    updateComponentStyle(fileKey);     
    getSystemTreeComponents(filekey)
      .then(data => {
        promptingMessage1.remove();
        initTree(getSystemTreeNodes(data.data));
        initTree(data1)
      })
      showSystemComponents();  // 展示构件内系统列表
      showSystemComponents1();
      addRestorButton();
         //  根据选择的楼层信息更新构件类的值
      let tool = new BIMWINNER.Tool(vizbim);
      tool.createTool(); 
      vizbim.listentoSelectObjs(function (componentId, component) {
        console.log("componentId:",componentId);
        console.log("component",component);
        if (componentId) {    // 如果选中构件的时候可以拿到这个构件id，则执行下面的逻辑
          vizbim.restoreObjtColor();
          vizbim.setObjtColor([componentId], [0, 1, 0]);
          
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
            if (!systemFlag) {
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
                      getComponentinformationByComponentId(item)
                      .then((data3)=>{
                      const text = data3.data;
                      const IDname = text.name;
                      const idItem = IDname.substring(0,17) + "...";
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
    height: 400,
    closeOnEsc: false,
    closeButton: false,
    content: '<div id="attributeContent" class="layui-card"></div>'
  };
  attributeWindow = Lobibox.window(attribute);
  attributeWindow.setPosition({
    left: 1500,
    top: 50,
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
    left: 1500,
    top: 400,
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
  const $toolHome = $('<button  style = "bottom: 40px" type="button1" class="yj-but" title="初始化" id="home' + toolId + '"><div class="yj-icon home-icon" ></div></button>');
  $toolHome.appendTo(group1);
  $toolHome.click(() => {
    systemFlag = false;
    vizbim.resetScene();
    $("#attributeContent").children().remove();
    $("#attributeContent1").children().remove();
  });
}

let description = false;
let description2 = false;

// 显示title说明
const showDescription = () => {
  if (!description) {
    $(descriptionContainer).attr("style", "font-size:16px;margin-bottom: 0;left:270px;top:10px;background-color:white;position:absolute;width:150px");
  } else {
    $(descriptionContainer).css("display", "none");
  }
  description = !description;
}

// 显示构件名称输入说明
const showDescription2 = () => {
  if (!description2) {
    $("#descriptionContainer2").attr("style", "font-size:16px;margin-bottom: 0;left:240px;top:160px;background-color:white;position:absolute;width:170px");
  } else {
    $("#descriptionContainer2").css("display", "none");
  }
  description2 = !description2;
}

// 创建左侧搜索框
const addTileandSearchBoard = (fileKey) => {
  var toolBarZK = $("#viewport");
  const toolContainer = $(" <div id='container'></div>");
  toolBarZK.append(toolContainer);
  $(toolContainer).append("<div id='descriptionContainer' style='display:none'> </div>")
  $(toolContainer).append("<div id='descriptionContainer2' style='display:none'> </div>")
  $("#descriptionContainer").append("<p id ='title1'>" + "对当前模型构件进行筛选，可以只选填部分参数。" + "</p>");
  $("#descriptionContainer2").append("<p id ='title2'>" + "请输入构件名称，进行模糊查找，例如:门、窗户等 " + "</p>");
  $(toolContainer).append("<p id ='title' style='font-size:30px;margin-bottom: 21px;margin-left: 50px;'> " +
    " 构件查询 " +
    "<i style='font-size:20px;cursor:pointer;'class='far fa-question-circle' onmousedown='showDescription()'></i>" +
    "</p>");
  const formContainer = $("<form id='formContainer' class='layui-form'></form>");
  $(toolContainer).append(formContainer);
  const formItem1 = $("<div class='layui-form-item'>" +
    "<label class='layui-form-label'>楼层</label>" +
    "<div class='layui-input-block'>" +
    "<select name='louceng' lay-filter='louceng' id='louceng' lay-search >" +
    "<option value='disable' id='disable'>数据获取中</option>" +
    " </select>" +
    " </div>" +
    "  </div>");
  const formItem2 = $("<div class='layui-form-item'>" +
    "<label class='layui-form-label'>构件类</label>" +
    "<div class='layui-input-block'>" +
    "<select name='goujianlei' lay-filter='goujianlei' id='goujianlei' lay-search  >" +
    "<option value='disable2' id='disable2'>数据获取中</option>" +
    "<option value=''>--</option>" +
    " </select>" +
    " </div>" +
    "  </div>");
  const formItem3 = $("  <div class='layui-form-item'>" +
    "    <label class='layui-form-label'>构件名称</label>" +
    "    <div class='layui-input-inline' style='width: 110px;position:absolute'>" +
    "      <input type='text' name='gjname' autocomplete='off' class='layui-input'>" +
    "    </div>" +
    "    <div class='layui-form-mid layui-word-aux' style='left: 210px;position: absolute'>" +
    "       <i style='font-size:20px;cursor:pointer;'class='far fa-question-circle' onmousedown='showDescription2()'></i>" +
    "     </div>" +
    "  </div>");
  const formItem4 = $("  <div class='layui-form-item'>" +
    "    <div class='layui-input-block'>" +
    "      <button id='searchButton' class='lyButton' disabled lay-submit lay-filter='beginSearch'>开始搜索</button>" +
    "    </div>" +
    "  </div>");
  //如需显示楼层索引 去掉下处注释 修改CSS文件中的container高度和位置
  // $("#formContainer").append(formItem1);
  $("#formContainer").append(formItem2);
  $("#formContainer").append(formItem3);
  $("#formContainer").append(formItem4);

  layui.use('form', function () {
    form = layui.form;
    //监听提交
    form.on('submit(beginSearch)', function (data) {
      const info = data.field;
      updateMoelBySearchResult(fileKey, info.louceng, info.goujianlei, info.gjname);
      return false;   // 阻止表单跳转
    });

    form.on('select(louceng)', function (data) {
      updateComponentStyleByLevelId(data.value);
      return false; // 阻止表单跳转
    });
  });
}

//更新form的楼层信息
const updateLoucengInformation = (fileKey) => {
  // 利用[数据接口:获取模型对于的空间树的楼层信息] 将返回的数据更新表单的楼层信息
  getModelLoactionTree(fileKey).then((result) => {
    $("#disable").remove();
    const dataArray = result[0].childrenResultList[0].childrenResultList[0].childrenResultList;
    if (dataArray && dataArray.length !== 0) {
      dataArray.forEach(item => {
        if (item.type === "IFCBUILDINGSTOREY" && item.children.length > 0) {
          let obj = {};
          obj.name = item.name;
          obj.key = item.key;
          buildingLevel.push(obj);
        }
      });
    }
    if (buildingLevel.length !== 0) {
      buildingLevel.forEach((item1, index1) => {
        getLevelCompnentTypes(fileKey, item1.key).then(data => {
          if (data.code === 200) {
            if (data.data.length !== 0) {
              item1.componentTypes = data.data;
            }
          }
        });
      });
      $("#louceng").append("<option value=''>" + "--" + "</option>");
      buildingLevel.forEach((item, index) => {
        $("#louceng").append("<option value=" + item.key + ">" + item.name + "</option>");
      });
      if (form) form.render('select');
    } else {
      $("#louceng").append("<option value=''>" + "该模型无楼层信息" + "</option>");
    }
    $(".lyButton").removeAttr("disabled");
  })
}


// 根据楼层id更新构建类的option
const updateComponentStyleByLevelId = (levelid) => {
  $("#goujianlei").children("option").remove();
  $("#goujianlei").append("<option value=''>--</option>");
  if (levelid !== '') {
    const upArray = buildingLevel.filter(item => item.key === levelid)[0].componentTypes;
    const withoutUpcaseArray = filterAllCapsComponentTypes(upArray);
    withoutUpcaseArray.forEach(item => {
      $("#goujianlei").append("<option value=" + item + ">" + item + "</option>")
    })
  } else {
    comTypeArray.forEach((item, index) => {
      $("#goujianlei").append("<option value=" + item + ">" + item + "</option>");
    })
  }
  if (form) form.render('select');
}

// 更新form的构件类信息
const updateComponentStyle = (fileKey) => {
  getAllModelComponentTypes(fileKey).then(data => {
    comTypeArray = filterAllCapsComponentTypes(data.data);
    comTypeArray.forEach((item, index) => {
      $("#goujianlei").append("<option value=" + item + ">" + item + "</option>");
    })
    $("#disable2").remove();
    if (form) form.render('select');
  })
}

// 用户点击搜索后的操作，将用户选择的楼层和构件类还有构件名称利用[数据接口:获取模型空间树结构]返回的构件id
// 将这些构件反选透明
const updateMoelBySearchResult = (fileKey, levelId, type, name) => {
  $("#searchButton").prepend("<i id='searchingIcon' class='layui-icon layui-icon-loading-1 layui-icon layui-anim layui-anim-rotate layui-anim-loop'></i>");
  $("#searchButton").attr("disabled", 'disabled');
  getModelSearchComponents(fileKey, levelId, type, name).then((result) => {
    let comArray = [];
    if (result.code === 200) {
      $("#searchingIcon").remove();
      $("#searchButton").removeAttr("disabled");
      if (result.data.length !== 0) {
        result.data.forEach(item => {
          if (item.children === null) {
            comArray.push(item.key);
          } else if (item.children && item.children.length !== 0) {
            item.children.forEach(item1 => {
              comArray.push(item1);
            })
          }
        });
        if (comArray.length !== 0) {
          vizbim.resetScene(false, true, true, true, true, true, true);
          vizbim.reverseTransparentObjs(comArray, 0.1, true);
          vizbim.fly.flyTo(mainView);
        }
      } else {
        vizbim.reverseTransparentObjs(comArray, 0.1, true);
        layer.open({
          title: '提示'
          , content: '当前条件下无对应构件，请重新选填查找条件'
        });
      }
    } else {
      vizbim.promptingMessage("error", "错误码:" + result.code + ",错误内容:" + result.message);
    }
  });
}

// 数据接口:获取模型对于的空间树的楼层信息
const getModelLoactionTree = (fileKey) => {
  return fetch(`${op.baseaddress}models/${fileKey}/trees/location?devcode=${op.devcode}`)
    .then(response => response.json());
}

// 数据接口:获取模型空间树结构 
//如需加入楼层索引 在'${op.devcode}'后加入&component=${levelId}    
const getModelSearchComponents = (fileKey, levelId, type, name) => {
  return fetch(`${op.baseaddress}models/${fileKey}/components/!query?devcode=${op.devcode}&type=${type}&name=${name}`)
    .then(response => response.json());
}

// 数据接口:获取当前模型下所有构件类型
const getAllModelComponentTypes = (fileKey) => {
  return fetch(`${op.baseaddress}models/${fileKey}/types?devcode=${op.devcode}`)
    .then(result => result.json());
}

// 数据接口:获取指定楼层下构件类别
const getLevelCompnentTypes = (fileKey, componentId) => {
  return fetch(`${op.baseaddress}models/${fileKey}/components/${componentId}/types?devcode=${op.devcode}`)
    .then(result => result.json());
}

// 过滤出全部大写的字母，将返回的构件类别的结果里全部是大写的类别过滤掉
const filterAllCapsComponentTypes = (componentTypesArray) => {
  if (componentTypesArray && componentTypesArray.length !== 0) {
    return componentTypesArray.filter(item => {
      if (typeof item === "string") {
        return hasLowerLetter(item);
      }
    });
  }
}

// 判断一个字符串是否有小写字母，供filterAllCapsComponentTypes使用
const hasLowerLetter = (str) => {
  for (let i = 0; i < str.length; i++) {
    if (str[i] >= 'a' && str[i] <= 'z') {
      return true;
    }
  }
}