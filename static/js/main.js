var text_btn = document.getElementById("text-btn");
var img_btn = document.getElementById("img-btn");
var hidden_input = document.getElementById("hidden-input");
var form = document.getElementById("input-form")

var text_input = document.getElementById("text-input");
var img_input = document.getElementById("image-input");

var img_label = document.getElementById("img-label")

var selection = document.getElementById("selection");

var text_limit = document.getElementById("text-limit");
var limit = 450;

// If text submit -> hidden field value = text + submit
text_btn.addEventListener("click", function() {
    hidden_input.value = "text"
    form.submit()
});

// If image submit -> hidden field value = image + submit
img_btn.addEventListener("click", function() {
    hidden_input.value = "image"
    form.submit()
});


// Enabling and disabling submit button - TEXT
text_input.addEventListener("input", function() {
    if (text_input.value == '') {
        text_btn.disabled = true;
        text_btn.classList.add("disabled");
    }
    else {
        text_btn.disabled = false;
        text_btn.classList.remove("disabled");
    }
});

// Enabling and disabling submit button - IMAGE
img_input.addEventListener("change", function() {
    // If no files
    if (img_input.files.length == 0) {
        img_btn.disabled = true;
        img_btn.classList.add("disabled");

        selection.innerText = "";
    }
    // If more than 1 file
    else if (img_input.files.length > 1) {
        alert("Only 1 file is allowed at a time. Please upload a single image file.")
        img_input.value = '';
    }
    // If 1 file added
    else {
        img_btn.disabled = false;
        img_btn.classList.remove("disabled");

        selection.innerText += "Selected: " + img_input.files[0].name;
    }
});


// Deselect Image
selection.addEventListener("click", function() {
    if (img_input.files.length > 0) {
        img_input.value = '';

        selection.innerText = "";

        img_btn.disabled = true;
        img_btn.classList.add("disabled");
    }
});




// Limiting max number of words
text_limit.textContent = 0 + "/" + limit;
text_input.addEventListener("input", function() {
    var current_value = text_input.value.trim();
    var current_length = current_value === '' ? 0 : current_value.split(/\s+/).length;
    
    text_limit.textContent = current_length + "/" + limit;

    if (current_length > limit) {
        text_limit.classList.add("error");
        text_input.classList.add("error");
        text_btn.disabled = true;
        text_btn.classList.add("disabled");
    }
    else {
        if (text_input.value.length == 0) {
            text_btn.disabled = true;
            text_btn.classList.add("disabled");
        }
        else {
            text_limit.classList.remove("error");
            text_input.classList.remove("error");
            text_btn.disabled = false;
            text_btn.classList.remove("disabled");
        }
    }
});








// Image drag
img_label.addEventListener("dragover", function(event) {
    event.preventDefault();

});
// Image drop
img_label.addEventListener("drop", function(event) {
    event.preventDefault();
    var files = event.dataTransfer.files;

    if (files.length == 1) {
        if (files[0].type.startsWith('image/')) {
            img_input.files = files;

            img_btn.disabled = false;
            img_btn.classList.remove("disabled");
        }
        else {
            alert("Only image file types are accepted. Please upload an image file.")
        }
    }
    if (files.length > 1) {
        alert("Only 1 file is allowed at a time. Please upload a single image file.")
    }
});


