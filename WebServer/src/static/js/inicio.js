window.onload = function() {        
		/*
        @summary: This function will run once the entire page (including images or frames),
        not just the DOM(Document Object Model), is ready. 
        
        Parameters
        ----------
        @param 
        fileInput: gets the input with id:fileInput in the html file.
        fileDisplayArea: gets the div with id:fileDisplayArea
        file: gets the chosen image by the user from the input fileInput.
        imageType: define the type of the content we are waiting
        reader: Returns a newly constructed FileReade.
        img: creates a new HTMLImageElement instance.
        
        Returns
        ----------
        @return: Displays the image selected by the user in the page
        */

		var fileInput = document.getElementById('fileInput');
		var fileDisplayArea = document.getElementById('fileDisplayArea');
	

		fileInput.addEventListener('change', function(e) { //When the user selects another image
			var file = fileInput.files[0];
			var imageType = /\*.jpg/;

			if (file.type.match(imageType)) { //Verify the content is a image, not other type
				var reader = new FileReader();

				reader.onload = function(e) { //After the page has been loaded
					fileDisplayArea.innerHTML = ""; //Change the HTML content of  fileDisplayArea

					var img = new Image();
					img.src = reader.result; //.src =Change the URL of an image  .result =Returns the file's contents

					fileDisplayArea.appendChild(img); // Append an image in fileDisplayArea
				}

				reader.readAsDataURL(file);	 // read the contents of the file
			} else { //User selected another type of file
				fileDisplayArea.innerHTML = "File not supported!"
			}
		});

}