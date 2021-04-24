
$(document).ready(function () {
  $('.carousel').slick({
    speed: 500,
    slidesToShow: 5,
    slidesToScroll: 1,
    autoplay: false,
    autoplaySpeed: 2000,
    dots: false,
    centerMode: false,
    arrows: true,
  });
  // ==================================================================
  $('.recentcolumns').slick({
    speed: 500,
    slidesToShow: 3,
    slidesToScroll: 1,
    autoplay: false,
    autoplaySpeed: 2000,
    dots: false,
    centerMode: false,
    arrows: true,
  });
});