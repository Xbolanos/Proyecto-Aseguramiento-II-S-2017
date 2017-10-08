 filepicker.setKey("ABeQAmZTIQ8ygf76s90Bnz");
  
var openPicker = () => {  
  return filepicker.pick(
  {
		mimetype:'image/*',
		maxFiles: 1,
		services: ['COMPUTER','WEBCAM'],
		folders:true
  },
  function(Blob){
	console.log(JSON.stringify(Blob.url));   //Aqui esta el url de la imagen
  },
  function(FPError){
    console.log(FPError.toString());
  });
}
  
var openPicker2 = () => {  
  return filepicker.pickMultiple(
  {
		mimetype:'image/*',
		minFiles: 4,
		maxFiles:20,
		services: ['COMPUTER'],
		folders:true
  },
  function(Blobs){
	var path = JSON.stringify(Blobs[0].path);
	var nombre_folder = ' ';  
	var cont = 0;
	for(var i = 0; i < path.length; ++i){
		if(path[i] == '/'){cont=cont+1;}
		if(path[i] != '/' && cont < 2 ){ nombre_folder = nombre_folder + path[i];}
	}
	console.log(nombre_folder); //Aqui esta el nombre del folder
	
	var urls = [];
	for(var i = 0; i < Blobs.length; ++i){
		urls=urls+[JSON.stringify(Blobs[i].url)];
	}
	console.log(urls); // aqui esta un arreglo con todos los urls de las imagenes del folder

  },
  function(FPError){
    console.log(FPError.toString());
  });
}
