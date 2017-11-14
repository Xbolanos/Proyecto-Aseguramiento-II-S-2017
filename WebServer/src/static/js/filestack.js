var apikey = 'AhZpdzSRTdW9nhvd946LAz';
// El api es para subir las imagenes a internet

var client = filestack.init(apikey);

var trainingOptions = {
  uploadInBackground: false,
  disableTransformer: true,
  accept: ['image/*', '.pgm'],
  minFiles: 8,
  maxFiles: 8,
  imageMin: [92, 112],
  imageMax: [92, 112],
  imageDim: [92, 112],
  fromSources: ['local_file_system','webcam', 'customsource']
};

var recognizeOptions = { //Cuando es 1 foto
  uploadInBackground: false,
  disableTransformer: true,
  accept: ['image/*', '.pgm'],
  imageMin: [92, 112],
  imageMax: [92, 112],
  imageDim: [92, 112],
  fromSources: ['local_file_system','webcam', 'customsource']
};

/**
 * Makes a request to the application backend to add the new subject
 * to the system, this will show a waiting dialog while it waits for the
 * server's response.
 * 
 * @param {string} destiny 
 * @param {object} data 
 */
var sendRequest = (destiny, data) => {
  swal({
    title: 'Registrando sujeto',
    text: 'Por favor espere mientras se completa el registro.',
    allowOutsideClick: false,
    onOpen: function () {
      swal.showLoading()
    }
  }).then(
    $.ajax({ 
      url: destiny, 
      method: 'POST',
      beforeSend: function(xhr, settings) { 
        xhr.setRequestHeader('X-CSRFToken', csrftoken); 
      }, 
      data: data,
      cache: false,
      contentType: false,
      processData: false,
    })
    .done(function(result) {
      swal( 
        result.title, 
        result.message, 
        result.type 
      ) 
    })
    .fail(function(result) {
      swal( 
        'Ha ocurrido un error', 
        'Verifique su conexión a internet o contactese con su proveedor', 
        'error' 
      ) 
    })
  );
}

var openSelectTrainingMethod = () => {
  swal({
    title: '¿Folder o imágenes?',
    text: '¿Va a cargar un folder con varios sujetos o imágenes de un solo sujeto?',
    icon: 'warning',
    buttons: {
      folder: {
        text: 'Folder',
        value: true
      },
      image: {
        text: 'Imágenes',
        value: false
      }
    }
  }).then((value) => {
    if(!value) {
      openPickerForTraining();
    } else {

    }
  })
}

/**
 * Opens a new dialog to allow the client the upload of images. In this case
 * it is formated as requested for the system training and then allows up to
 * 8 images.
 */
var openPickerForTraining = () => {
  return client.pick(trainingOptions).then(function(result) {
    var data = {
      handlers: [],
      tag: ''
    };
    
    result.filesUploaded.forEach(function(file) {
      data.handlers.push(file.handle);
    });

    swal({
      title: 'Agregar tag para el nuevo sujeto',
      input: 'text',
      showCancelButton: false,
      confirmButtonText: 'Completar registro',
      allowOutsideClick: false
    }).then(function (tag) {
      data.tag = tag
      sendRequest('http://localhost:8000/learn', data);
    });
  });
}

/**
 * Opens a new dialog to allow the client the upload of images. In this case
 * it is formated as requested for the system recognition and then allows
 * only one image.
 */
var openPickerForRecognition = () => {
  return client.pick(recognizeOptions).then(function(result){
	  result.filesUploaded.forEach(function(file){
      console.log(file.url); //file.url tiene la dirección de las imagenes
    });
  });
}

$('#training').submit((e) => {
  e.preventDefault();
  var files = document.getElementById("trainingFiles").files;
  var form_data = new FormData()
  
  for(var i = 0; i < files.length; i++) {
    form_data.append('file' + i, files[i]);
  }

  sendRequest('http://localhost:8000/learn', form_data);
});

var selectFolder = (e) => {
  for (var i = 0; i < e.target.files.length; i++) {
     var s = e.target.files[i].name + '\n';
     s += e.target.files[i].size + ' Bytes\n';
     s += e.target.files[i].type;
     console.log(s)
  }
}