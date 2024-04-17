// // document.getElementById("encodeForm").onsubmit = function () {
// //   document.getElementById("loading").style.display = "block";
// //   setTimeout(function () {
// //     document.getElementById("loading").style.display = "none";
// //   }, 3000); // Adjust the timeout as needed
// // };
// var encodeUrl = document.getElementById("encodeUrl").innerText;
// document.getElementById("encodeForm").onsubmit = function (e) {
//   console.log(encodeUrl);
//   e.preventDefault(); // Prevent the default form submission
//   document.getElementById("loading").style.display = "block";

//   var formData = new FormData();
//   formData.append("inputImage", document.getElementById("inputImage").files[0]);
//   formData.append("inputText", document.getElementById("inputText").value);

//   fetch(encodeUrl, {
//     method: "POST",
//     body: formData,
//   })
//     .then((response) => response.json())
//     .then((data) => {
//       setTimeout(function () {
//         document.getElementById("loading").style.display = "none";
//         console.log(data.encodedImagePath);
//         var img = document.createElement("img");
//         img.src = data.encodedImagePath; // The path you returned from Flask
//         img.style.maxWidth = "500px"; // Adjust size as needed
//         img.style.height = "auto";
//         document.getElementById("resultImage").appendChild(img);
//       }, 5000); // Adjust timeout as needed
//     })
//     .catch((error) => console.error("Error:", error));
// };

// // document.getElementById("encodeForm").onsubmit = function (event) {
// //   event.preventDefault(); // Prevent the form from submitting in the traditional way
// //   document.getElementById("loading").style.display = "block";

// //   var formData = new FormData(this);
// //   fetch("{{ url_for('encode') }}", {
// //     method: "POST",
// //     body: formData,
// //   })
// //     .then((response) => response.json())
// //     .then((data) => {
// //       setTimeout(function () {
// //         document.getElementById("loading").style.display = "none";
// //         var resultImageDiv = document.getElementById("resultImage");
// //         var image = new Image();
// //         image.src = data.encodedImageUrl;
// //         image.style.width = "50%"; // Adjust the size as needed
// //         image.style.height = "auto";
// //         resultImageDiv.appendChild(image);
// //       }, 5000); // Adjust timeout as needed
// //     });
// // };
// var encodeUrl = document.getElementById("encodeUrl").innerText;
// document.getElementById("encodeForm").onsubmit = function (e) {
//   console.log(encodeUrl);
//   e.preventDefault(); // Prevent the default form submission
//   document.getElementById("loading").style.display = "block";

//   var formData = new FormData();
//   formData.append("inputImage", document.getElementById("inputImage").files[0]);
//   formData.append("inputText", document.getElementById("inputText").value);

//   fetch(encodeUrl, {
//     method: "POST",
//     body: formData,
//   })
//     .then((response) => response.json())
//     .then((data) => {
//       setTimeout(function () {
//         document.getElementById("loading").style.display = "none";
//         console.log(data.encodedImagePath);
//         var img = document.createElement("img");
//         img.src = data.encodedImagePath; // The path you returned from Flask
//         img.style.maxWidth = "500px"; // Adjust size as needed
//         img.style.height = "auto";
//         document.getElementById("resultImage").appendChild(img);
//       }, 5000); // Adjust timeout as needed
//     })
//     .catch((error) => console.error("Error:", error));
// };
