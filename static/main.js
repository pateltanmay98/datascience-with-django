$(document).ready(function(){
$('#select')
  .dropdown()
;
$('.message .close')
  .on('click', function() {
    $(this)
      .closest('.message')
      .transition('fade')
    ;
  })
;
$('#modal-btn').click(function(){
   $('.ui.modal')
   .modal('show');
});
})