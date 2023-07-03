let refresh_cnt = document.getElementById("refresh_cnt").value;
let refresh_btn = document.getElementById("refresh_btn");


refresh_btn.addEventListener("click", function() {
    for (let i = 0; i < refresh_cnt; i ++) {
        location.reload();
        alert("hello");
    }
});