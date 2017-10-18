// Para una imagen--------------------------------------------------------

var apikey = 'ABeQAmZTIQ8ygf76s90Bnz';
// El api es para subir las imagenes a internet

var client = filestack.init(apikey);

var trainingOptions = {
  uploadInBackground: false,
  disableTransformer: true,
  accept: 'image/*',
  minFiles: 1,
  maxFiles: 10,
  imageMin: [92, 112],
  imageMax: [92, 112],
  imageDim: [92, 112],
  fromSources: ['local_file_system','webcam', 'customsource']
};

var recognizeOptions = { //Cuando es 1 foto
  uploadInBackground: false,
  disableTransformer: true,
  accept: 'image/*',
  imageMin: [92, 112],
  imageMax: [92, 112],
  imageDim: [92, 112],
  fromSources: ['local_file_system','webcam', 'customsource']
};

var sendRequest = (destiny, files) => {
  var imagesUrls = [];
  var data;
  
  files.filesUploaded.forEach(function(file) {
    imagesUrls.push(file.handle);
  });

  data = JSON.stringify(imagesUrls);

  $.ajax({
    url: destiny,
    method: 'POST',
    beforeSend: function(xhr, settings) {
      xhr.setRequestHeader('X-CSRFToken', csrftoken);
    },
    data: data,
    dataType: 'json',
    contentType: "application/json",
    success: function(result) {
      swal(
        result.title,
        result.message,
        result.type
      )
    },
    error: function(result) {
      swal(
        'Ha ocurrido un error',
        'Verifique su conexión a internet o contactese con su proveedor',
        'question'
      )
    }
  });
}
   
var openPickerForTraining = () => { //Cuando es 1 foto
  return client.pick(trainingOptions).then(function(result) {
    sendRequest('http://localhost:8000/learn', result);
  });
}

var openPickerForRecognition = () => { //Cuando es 1 foto
  return client.pick(recognizeOptions).then(function(result){
	  result.filesUploaded.forEach(function(file){
      console.log(file.url); //file.url tiene la dirección de las imagenes
    });
  });
}