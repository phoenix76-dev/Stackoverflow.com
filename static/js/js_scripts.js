/**
 * Created by user on 01.07.2017.
 */

function checkLogin() {
    if(logged_in) {
        return true;
    }
    else {
        return false;
    }
}

$(document).ready(function () {

    // Select active section in top menu
   var uri = $(location).attr('href');
   if(uri.search('/questions/') > 0) {
       $('#nav-1').toggleClass('active-nav-btn');
   }
   else if(uri.search('/jobs/') > 0) {
       $('#nav-2').toggleClass('active-nav-btn');
   }
   else if(uri.search('/documentations/') > 0) {
       $('#nav-3').toggleClass('active-nav-btn');
   }
   else if(uri.search('/tags/') > 0) {
       $('#nav-4').toggleClass('active-nav-btn');
   }
   else if(uri.search('/users/') > 0) {
       $('#nav-5').toggleClass('active-nav-btn');
   }
});