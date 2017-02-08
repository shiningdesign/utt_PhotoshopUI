// by ying 2016
// a photoshop javascript file to call the Python file in same directory that sharing the same name.
// like call_PhotoshopUI.jsx will auto launch PhotoshopUI.pyw (pyw is same as py but will auto open by python without console pop up) from Photoshop script menu, 
// or from action panel if you record a script call macro

// extra research code included for your study purpose
/*
function WhoAmI() {
var where;
try {var F = FO;
}catch( err ) {where = File(err.fileName);}
return where;
}; 
var a = WhoAmI();
//alert(a);
//alert(app.activeScript.parent);
//alert(app.activeDocument.filePath); // not working
var myPath = (app.activeDocument.fullName.parent.fsName).toString().replace(/\\/g, '/'); // python like path
alert(myPath);
alert(Folder.current); 
var thisFile = new File($.fileName); // works great for this script file location
var basePath = thisFile.path; 
alert(basePath);

var file = new File("/D/myFolder/myCmd.bat");
file.execute();
*/
var thisFile = new File($.fileName); // works great for this script file location
var curPath = thisFile.path;
var call_fileName_ext = thisFile.name;
var fileName = call_fileName_ext.substring(call_fileName_ext.indexOf("_")+1, call_fileName_ext.lastIndexOf("."));
var pyFile = new File(curPath+"/"+fileName+".pyw");
pyFile.execute();
