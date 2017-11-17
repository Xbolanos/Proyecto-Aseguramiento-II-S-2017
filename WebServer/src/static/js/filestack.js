var apikey = 'AhZpdzSRTdW9nhvd946LAz';
// El api es para subir las imagenes a internet

var client = filestack.init(apikey);

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
var sendRequest = (destiny, data, info) => {
  swal({
    title: info.title,
    text: info.text,
    icon: 'warning',
    closeOnClickOutside: false,
    closeOnEsc: false,
    buttons: false
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
      );
    })
    .fail(function(result) {
      swal( 
        'Ha ocurrido un error', 
        'Verifique su conexión a internet o contactese con su proveedor', 
        'error' 
      );
    })
  );
}

/**
 * Opens a new dialog to allow the client the upload of images. In this case
 * it is formated as requested for the system recognition and then allows
 * only one image.
 */
var openPickerForRecognition = () => {
  return client.pick(recognizeOptions).then(function(result){
    var fileHandler;

	  result.filesUploaded.forEach(function(file){
      fileHandler = file.handle; //file.url tiene la dirección de las imagenes
    });

    var info = {
      title: 'Identificando sujeto',
      text: 'Por favor espere mientras se completa la identificación.'
    }

    sendRequest('http://localhost:8000/recongnize', fileHandler, info);
  });
}

var isValid = (fileName) => {
  var validFiles = ['jpeg', 'png', 'pgm', 'jpg'];
  var length = validFiles.length;

  for(var i = 0; i < length; i++) {
    if(fileName.endsWith(validFiles[i])) {
      return true;
    }
  }

  return false;
}

var isInt = (value) => {
  return !isNaN(value) && 
         parseInt(Number(value)) == value && 
         !isNaN(parseInt(value, 10));
}

var sameQuantityOfImagesPerFolder = (numFilesPerFolder, initialKey) => {
  var baseValue = numFilesPerFolder[initialKey];

  for (var key in numFilesPerFolder) {
    if (numFilesPerFolder.hasOwnProperty(key)) {
      if(baseValue != numFilesPerFolder[key]) {
        return false;
      }
    }
  }

  return true;
}

$('#training').submit((e) => {
  e.preventDefault();
  var files = document.getElementById('trainingFiles').files;
  var form_data = new FormData();
  
  var name = '';
  var file;
  var numFilesPerFolder = {};
  
  for(var i = 0; i < files.length; i++) {
    file = files[i];

    if(isValid(file.name)) {
      name = file.webkitRelativePath;
      name = name.split('/');
      name = name[name.length - 2];

      if(!(name in numFilesPerFolder)) {
        numFilesPerFolder[name] = 1;
      } else {
        numFilesPerFolder[name] += 1;
      }

      form_data.append('file' + i, file);
      form_data.append('file' + i + 'data', name);
    }
  }

  if(!sameQuantityOfImagesPerFolder(numFilesPerFolder, name)) {
    swal('Entrada no valida', 'Se deben tener la misma cantidad de imágenes por sujeto. Verifique los archivos.', 'error');
    return;
  }

  var numImagesPerSubject = numFilesPerFolder[name];

  swal({
    text: 'Ingrese el número de auto-vectores a utilizar',
    content: "input",
    button: {
      text: "Entrenar",
      closeModal: false,
    },
  }).then((numvectors) => {
    if(!isInt(numvectors)) {
      swal('Entrada no valida', 'Debe ingresar un número mayor a cero.', 'error');
      return;
    }

    if(numvectors <= 0) {
      swal('Número invalido', 'El número de auto-vectores no puede ser menor o igual a 0.', 'error');
      return;
    }

    form_data.append('autovectors', numvectors);
    form_data.append('imagesPerSubject', numImagesPerSubject);

    var info = {
      title: 'Registrando sujeto(s)',
      text: 'Por favor espere mientras se completa el registro.'
    }
  
    sendRequest('http://localhost:8000/learn', form_data, info);
  });
});

var logout = () => {
  $.ajax({ 
    url: 'http://localhost:8000/logout', 
    method: 'POST',
    beforeSend: function(xhr, settings) { 
      xhr.setRequestHeader('X-CSRFToken', csrftoken); 
    },
    dataType: 'json'
  })
  .done((result) => {
    window.location.replace('http://localhost:8000');
  })
  .fail((result) => {
    swal( 
      'Ha ocurrido un error', 
      'Verifique su conexión a internet o contactese con su proveedor', 
      'error' 
    );
  })
}

var countFiles = (e) => {
  e.preventDefault();
  var files = document.getElementById('trainingFiles').files;
  var labelFiles = document.getElementById('labelFiles');

  labelFiles.textContent = 'Subir archivos... ' + files.length; 
}