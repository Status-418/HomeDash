(function ($) {

// Toggle the side navigation
   $("#sidebarToggle").on("click", function (e) {
    e.preventDefault();
    $("body").toggleClass("sidenav-toggled");
});

    // Activate Feather icons
    feather.replace();
})(jQuery);