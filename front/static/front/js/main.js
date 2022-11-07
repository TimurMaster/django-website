new WOW().init();



var prevScrollpos = window.pageYOffset;
window.onscroll = function(){
    var currentScrollPos = window.pageYOffset;
    if(prevScrollpos > currentScrollPos){
        document.getElementById("navbar").style.top = "0px";
    }else if(currentScrollPos == 0){
        document.getElementById("navbar").style.top = "0px";
    }else{
        document.getElementById("navbar").style.top = "-130px";
    }
    prevScrollpos = currentScrollPos;


    
var scrolled;
    scrolled = window.pageYOffset || document.documentElement.scrollTop;
        if(scrolled > 10){
            $("#navbar").addClass('active');
            $("#navbar").removeClass('nonactive');
        }
        if(10 > scrolled){
            $("#navbar").addClass('nonactive');
            $("#navbar").removeClass('active'); 
        }
}



var swiper = new Swiper('.clients-swiper', {
    slidesPerView: 5,
    spaceBetween: 30,
    autoplay: {
      delay: 3000,
      disableOnInteraction:false,
    },
    pagination: {
        el: '.swiper-pagination-clients',
      },
     // Responsive breakpoints
     breakpoints: {
      // when window width is >= 320px
      320: {
        slidesPerView: 2,
        spaceBetween: 10
      },
      // when window width is >= 640px
      640: {
        slidesPerView: 4,
        spaceBetween: 20
      },
      940: {
        slidesPerView: 5,
      }
    }
  });


  var swiper = new Swiper('.partners-swiper', {
    slidesPerView: 5,
    spaceBetween: 30,
    autoplay: {
      delay: 3000,
      disableOnInteraction:false,
    },
    pagination: {
        el: '.swiper-pagination-partners',
      },
     // Responsive breakpoints
     breakpoints: {
      // when window width is >= 320px
      320: {
        slidesPerView: 2,
        spaceBetween: 10
      },
      // when window width is >= 640px
      640: {
        slidesPerView: 4,
        spaceBetween: 20
      },
      940: {
        slidesPerView: 5,
      }
    }
  });


  var swiper = new Swiper('.about-swiper', {
    slidesPerView: 1,
    autoplay: {
      delay: 3000,
      disableOnInteraction:false,
    },
    navigation: {
      nextEl: '.swiper-button-next-about',
      prevEl: '.swiper-button-prev-about',
    },
  });

  var swiper = new Swiper('.main-swiper', {
    slidesPerView: 1,
    navigation: {
      nextEl: '.swiper-button-next-main',
      prevEl: '.swiper-button-prev-main',
    },
  });



$(function() {
  $(document).on("click", ".mob-toggle", function(e) {
    $(this).toggleClass("active");
    $(".m-nav").toggleClass("active");
    if ( $(".mob-toggle").hasClass("active")) {
    $("body").css("overflow", "hidden");
    } else {
      $("body").css("overflow", "auto");
    }
  });
})


$(function() {
  $(document).on("click", ".m-menu a", function(e) {
    $(".mob-toggle").removeClass("active");
    $(".m-nav").removeClass("active");
    $("body").css("overflow", "auto");
  });
})


$(function() {
  $(document).on("click", ".search .icon", function(e) {
    $(".cont-top-inner").addClass("active");
  });
})



$(document).click( function(e){
  if ( $(e.target).closest('.search .icon').length ) {
      return;
  }

  if ( $(e.target).closest('.search-div').length ) {
    return;
  }
  $(".cont-top-inner").removeClass("active");
});