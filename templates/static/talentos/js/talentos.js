// document.addEventListener("DOMContentLoaded", function(){
//   var csrf_token = document.querySelector('meta[name="csrf-token"]').getAttribute('content');
//   var filterBtns = document.querySelectorAll('.filter-btn');
//   filterBtns.forEach(function (btn) {
//       btn.addEventListener('click', function() {
//           var filterId = btn.id; 
//           $.ajax({
//             url: 'filter-talentos/'+btn.id,
//             type: 'POST',
//             data: {
//                 id: filterId,
//                 csrfmiddlewaretoken: csrf_token
//             },
//             success: function(response) {
//                 $('#filtered-talentos').html(response);
//             },
//             error: function(xhr) {
//                 console.log('Error');
//             }
//         });
//       });
//   });
// });





//           // console.log(btn.id);
//           // $.ajax({
//           //   url: '/talentos/' + filterId + '/',
//           //   method: 'get',
//           //   data: {
//           //     csrfmiddlewaretoken: csrf_token,
//           //     id: btn.id
//           //   },
//           //   success: function(data) {
//           //     $("body").html(data);
//           //   }
//           // });




