function validerFormulaire() {

    var code = document.getElementById("code");
    var q1 = document.getElementById("q1");
    var q2 = document.getElementById("q2");
    var q3 = document.querySelectorAll('input[type="radio"][name="q3"]');
    var q4 = document.querySelectorAll('input[type="checkbox"][name="q4"]');
    var q5 = document.querySelectorAll('input[type="checkbox"][name="q5"]');
    var labelQ1 = document.getElementById("labelQ1");
    var labelQ2 = document.getElementById("labelQ2");
    var labelQ3 = document.getElementById("labelQ3");
    var labelQ4 = document.getElementById("labelQ4");
    var labelQ5 = document.getElementById("labelQ5");
    var codeLabel = document.getElementById("codeLabel");
    var formValide = true;

    let q3Choisi = false;
    let q4Choisi = false;
    let q5Choisi = false;

    for (var q3Choix of q3) {
        if (q3Choix.checked) {
            q3Choisi = true;
            break;
        }
    }

    for (var q4Choix of q4) {
        if (q4Choix.checked) {
            q4Choisi = true;
            break;
        }
    }

    for (var q5Choix of q5) {
        if (q5Choix.checked) {
            q5Choisi = true;
            break;
        }
    }

    if (code.value === '') {
        codeLabel.style.color = "red"
        formValide = false;
    }

    if (q1.options.length === 0) {
        labelQ1.style.color = "red"
        formValide = false;
    }
    if (q2.value === '') {
        labelQ2.style.color = "red"
        formValide = false;
    }
    if (!q3Choisi) {
        labelQ3.style.color = "red"
        formValide = false;
    }
    if (!q4Choisi) {
        labelQ4.style.color = "red"
        formValide = false;;
    }
    if (!q5Choisi) {
        labelQ5.style.color = "red"
        formValide = false;
    }

    return formValide;
}
