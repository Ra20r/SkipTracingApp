document.addEventListener("DOMContentLoaded", () => {
    const submit = document.querySelector("#submitBtn");
    const sanity = document.querySelector("#confirmSanity");
    submit.disabled = true;
    sanity.checked = false;
});


function emailCheck(item){
    const ex= /^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$/;
    return ex.test(item.value);
}

function phoneCheck(item){
    const ex= /^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$/;    ;
    return ex.test(item.value);
}

function numericCheck(item){
    const ex= /^\d+(\d+)*$/;
    return ex.test(item.value);
}

function check(){ //called when agree to proceed is clicked
    const submit = document.querySelector("#submitBtn");
    const sanity = document.querySelector("#confirmSanity");
    const textField = document.querySelectorAll('.task');
    const error = document.querySelector("#errorDiv");
    let valid = true;
    textField.forEach( item => {
        console.log("another one");
        console.log(valid);
        if(item.value.length === 0){
            valid = false;
            return;
        } else if(item.dataset.checker==="email" && !emailCheck(item)) {
            valid= false;
            return;
        } else if(item.dataset.checker==="pnumber" && !phoneCheck(item)) {
            valid = false;
            return;
        } else if(item.dataset.checker==="numeric" && !numericCheck(item)){
            valid = false;
            return;
        }
    });
    if(valid){
        submit.disabled = false;
        error.innerHTML = "Your form is valid, please submit";
    } else {
        submit.disabled = true;
        error.innerHTML = "Your form seems to be invalid, please re-check";
        sanity.checked = false;
    }
    return false;
}

function check_pill(name){
    const submit = document.querySelector("#submitBtn");
    const sanity = document.querySelector("#confirmSanity");
    const item = document.querySelector(`.${name}`);
    const error = document.querySelector(`.errorDiv${name}`);
    let valid = true;
    if(item.value.length === 0){
        valid = false;
    } else if(item.dataset.checker==="email" && !emailCheck(item)) {
        valid= false;
    } else if(item.dataset.checker==="pnumber" && !phoneCheck(item)) {
        valid = false;
    } else if(item.dataset.checker==="numeric" && !numericCheck(item)){
        valid = false;
    } else if(item.dataset.checker==="file" && !fileCheck(item)){
        valid = false;
    }
    if(valid){
        submit.disabled = false;
        error.innerHTML = "Your form is valid, please submit";
    } else {
        submit.disabled = true;
        error.innerHTML = "Your form seems to be invalid, please re-check";
        sanity.checked = false;
    }
    return false;
}