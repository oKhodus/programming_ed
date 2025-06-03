let slider = document.getElementById("myRange");
let out = document.getElementById("out");

out.innerHTML = slider.value;

slider.oninput = function() {
out.innerHTML = this.value;
// console.log(slider.value);
}

function gen() {
    let range = document.getElementById("rangepass").value;
    let out_place = document.getElementById("out");
    let charset = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz~!@-#$";
    let final_password = '';

    
    if (!range) {
        out_place.innerHTML = "Enter please range for password!";
        return;
    }
    
    for (let i = 0, n = charset.length; i < Number(range); i++) {
        final_password += charset.charAt(Math.floor(Math.random() * n));
    }

    out_place.innerHTML = final_password;

}