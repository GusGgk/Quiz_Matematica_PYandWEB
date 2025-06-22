function verificarQ1() {
    const condInput = document.getElementById("q1_cond").value.trim().replace(/\s+/g, "");
    const erroInput = document.getElementById("q1_erro").value.trim().toLowerCase();
    const feedback = document.getElementById("q1_feedback");

    if (condInput === "num_user!=0" && ["zero", "0"].includes(erroInput)) {
        feedback.textContent = "✅ Correto!";
        feedback.style.color = "green";
        document.getElementById("q1").classList.add("hidden");
        document.getElementById("q2").classList.remove("hidden");
    } else {
        feedback.textContent = "❌ Tente novamente!";
        feedback.style.color = "red";
    }
}

function verificarQ2() {
    const cond = document.getElementById("q2_cond").value.trim().replace(/\s+/g, "");
    const erro = document.getElementById("q2_erro").value.trim().toLowerCase();
    const fb = document.getElementById("q2_feedback");

    if (cond === "num_user>=0" && erro === "número negativo") {
        fb.textContent = "✅ Correto!";
        fb.style.color = "green";
        document.getElementById("q2").classList.add("hidden");
        document.getElementById("q3").classList.remove("hidden");
    } else {
        fb.textContent = "❌ Tente novamente!";
        fb.style.color = "red";
    }
}

function verificarQ3() {
    const cond = document.getElementById("q3_cond").value;
    const erro = document.getElementById("q3_erro").value;
    const fb = document.getElementById("q3_feedback");

    if (cond === "num_user>0" && erro === "zero") {
        fb.textContent = "✅ Correto!";
        fb.style.color = "green";
        document.getElementById("q3").classList.add("hidden");
        document.getElementById("q4").classList.remove("hidden");
    } else {
        fb.textContent = "❌ Tente novamente!";
        fb.style.color = "red";
    }
}

function verificarQ4() {
    const cond = document.getElementById("q4_cond").value;
    const erro = document.getElementById("q4_erro").value;
    const fb = document.getElementById("q4_feedback");

    if (cond === "indice%2!=0 or radicando>=0" && erro === "número negativo") {
        fb.textContent = "✅ Correto!";
        fb.style.color = "green";
        document.getElementById("q4").classList.add("hidden");
        document.getElementById("q5").classList.remove("hidden");
    } else {
        fb.textContent = "❌ Tente novamente!";
        fb.style.color = "red";
    }
}

function verificarQ5() {
    const cond = document.getElementById("q5_cond").value;
    const erro = document.getElementById("q5_erro").value;
    const fb = document.getElementById("q5_feedback");

    if (cond === "base!=0 or expoente>=0" && erro === "negativo") {
        fb.textContent = "✅ Correto!";
        fb.style.color = "green";
        document.getElementById("q5").classList.add("hidden");
        document.getElementById("q6").classList.remove("hidden");
    } else {
        fb.textContent = "❌ Tente novamente!";
        fb.style.color = "red";
    }
}

function verificarQ6() {
    const cond = document.getElementById("q6_cond").value;
    const erro = document.getElementById("q6_erro").value;
    const fb = document.getElementById("q6_feedback");

    if (cond === "divisor!=0" && erro === "zero") {
        fb.textContent = "✅ Correto!";
        fb.style.color = "green";
        document.getElementById("q6").classList.add("hidden");
        document.getElementById("q7").classList.remove("hidden");
    } else {
        fb.textContent = "❌ Tente novamente!";
        fb.style.color = "red";
    }
}

function verificarQ7() {
    const cond = document.getElementById("q7_cond").value;
    const erro = document.getElementById("q7_erro").value;
    const fb = document.getElementById("q7_feedback");

    if (cond === "x!=2 and x!=-2" && erro === "2 ou -2") {
        fb.textContent = "✅ Correto!";
        fb.style.color = "green";
        document.getElementById("q7").classList.add("hidden");
        document.getElementById("q8").classList.remove("hidden");
    } else {
        fb.textContent = "❌ Tente novamente!";
        fb.style.color = "red";
    }
}

function verificarQ8() {
    const cond = document.getElementById("q8_cond").value;
    const erro = document.getElementById("q8_erro").value;
    const fb = document.getElementById("q8_feedback");

    if (cond === "valor>0 and base>0 and base!=1" && erro === "1") {
        fb.textContent = "✅ Correto!";
        fb.style.color = "green";
        document.getElementById("q8").classList.add("hidden");
        document.getElementById("q9").classList.remove("hidden");
    } else {
        fb.textContent = "❌ Tente novamente!";
        fb.style.color = "red";
    }
}

function verificarQ9() {
    const cond = document.getElementById("q9_cond").value;
    const erro = document.getElementById("q9_erro").value;
    const fb = document.getElementById("q9_feedback");

    if (cond === "True" && erro === "número negativo") {
        fb.textContent = "✅ Correto!";
        fb.style.color = "green";
        document.getElementById("q9").classList.add("hidden");
        document.getElementById("q10").classList.remove("hidden");
    } else {
        fb.textContent = "❌ Tente novamente!";
        fb.style.color = "red";
    }
}

function verificarQ10() {
    const cond = document.getElementById("q10_cond").value;
    const erro = document.getElementById("q10_erro").value;
    const fb = document.getElementById("q10_feedback");

    if (cond === "x!=3" && erro === "zero") {
        fb.textContent = "✅ Correto! Quiz finalizado!";
        fb.style.color = "green";
    } else {
        fb.textContent = "❌ Tente novamente!";
        fb.style.color = "red";
    }
}
