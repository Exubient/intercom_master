
<script>
  
$(document).ready(function(){
  $(document).on('click', '.nav .navbar-nav .nav-tabs li a', function () {
    console.log($(this));
    $('.active').removeClass('active');
    $(this).parent().addClass('active');
  });
});

</script>