// Para una imagen--------------------------------------------------------

var apikey = 'ABeQAmZTIQ8ygf76s90Bnz';
// El api es para subir las imagenes a internet

var client = filestack.init(apikey);


var options = { //Cuando es 1 foto
      uploadInBackground: false,
	  accept: 'image/*',
      fromSources: ['local_file_system','webcam', 'customsource']
  }
   
var openPicker = () => { //Cuando es 1 foto
  return client.pick(options).then(function(result){
	  result.filesUploaded.forEach( function(file){
	  alert(file.url);  });
	  //file.url tiene la dirección de las imagenes
  }
  );
}

//Para el folder------------------------------------------------------

var dropzone = document.getElementById("dropzone");

dropzone.addEventListener("drop", function(e) {
  e.stopPropagation();
  e.preventDefault();
  var items = event.dataTransfer.items;
  for (var i = 0; i < items.length; i++) {
    var entry = items[i].webkitGetAsEntry();
    if (entry) {
      traverse(entry);
    }
  }
  alert("Se cargaron bien las imagenes");
}, false);

dropzone.ondragover = function (e) {
  e.preventDefault()
}

function traverse(entry, path) {
  path = path || "";
  if (entry.isFile) {
    // Get file
    entry.file(function(file) {
      console.log("File:", path + file.name);
	  //Aqui esta el path de cada imagen que se carga.
	  //en Path está el nombre del folder
    });
  } else if (entry.isDirectory) {
    // Get folder contents
    var dirReader = entry.createReader();
    dirReader.readEntries(function(entries) {
      for (var i = 0; i < entries.length; i++) {
        traverse(entries[i], path + entry.name + "/");
      }
    });
  }
}