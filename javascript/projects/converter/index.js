function conv() {
    let x1 = document.getElementById("inp1").value;
    let checkbox1 = document.getElementById("check_cmtoin");
    cm_to_inches = (Number(x1) / 2.54).toFixed(2);

    out = document.getElementById("out");
    if (!x1) {
        out.innerHTML = "Please enter value!"
    }
    else if (!checkbox1.checked){
        out.innerHTML = "Please check the box to continue!"
    }
    else{
        out.innerHTML = `${x1} (cm) will be ${cm_to_inches} (in)`;
    }
}




