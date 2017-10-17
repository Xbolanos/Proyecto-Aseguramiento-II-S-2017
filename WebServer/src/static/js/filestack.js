// Para una imagen--------------------------------------------------------

var apikey = 'ABeQAmZTIQ8ygf76s90Bnz';
// El api es para subir las imagenes a internet

var client = filestack.init(apikey);

var trainingOptions = {
  uploadInBackground: false,
  accept: 'image/*',
  minFiles: 5,
  maxFiles: 10,
  imageMin: [92, 112],
  imageMax: [92, 112],
  imageDim: [92, 112],
  fromSources: ['local_file_system','webcam', 'customsource']
}

var recognizeOptions = { //Cuando es 1 foto
  uploadInBackground: false,
  accept: 'image/*',
  imageMin: [92, 112],
  imageMax: [92, 112],
  imageDim: [92, 112],
  fromSources: ['local_file_system','webcam', 'customsource']
}
   
var openPickerForTraining = () => { //Cuando es 1 foto
  return client.pick(trainingOptions).then(function(result) {
	  result.filesUploaded.forEach(function(file){
      console.log(file.url); //file.url tiene la dirección de las imagenes
    });
  });
}

var openPickerForRecognition = () => { //Cuando es 1 foto
  return client.pick(recognizeOptions).then(function(result){
	  result.filesUploaded.forEach(function(file){
      console.log(file.url); //file.url tiene la dirección de las imagenes
    });
  });
}