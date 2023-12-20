function show_search() {
    document.querySelector(".dainiki-header").classList.toggle("show-search")
    document.querySelector(".mobile-nav").classList.remove("show-nav")
}
function show_nav() {
    document.querySelector(".mobile-nav").classList.toggle("show-nav")
    document.querySelector(".dainiki-header").classList.remove("show-search")
}
window.addEventListener("scroll",()=>{
    document.querySelector(".dainiki-header").classList.remove("show-search")
    document.querySelector(".mobile-nav").classList.remove("show-nav")
})

var currentBannerIndex = 0;

var banners = document.querySelectorAll(".banner-container")

var dots = document.querySelectorAll(".index-dot .dot")
function slideshow(cn)
{
    currentBannerIndex = cn
}

setInterval(() => {
    currentBanner(currentBannerIndex);
    console.log(currentBannerIndex)
    console.log(banners.length)
    ++currentBannerIndex
    currentBannerIndex = currentBannerIndex % banners.length
   
}, 4000);
function currentBanner(currentBannerIndex) {
    banners.forEach(item => {
        console.log("Hello")
        item.style.display = "none";

    })
    dots.forEach(item =>{
        item.style.backgroundColor = "#807979"
    })
    banners[currentBannerIndex].style.display = "flex";
    dots[currentBannerIndex].style.backgroundColor = "#313131"
}
currentBanner(currentBannerIndex);



