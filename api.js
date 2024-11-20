function consumoApi() {
    const edad = document.getElementById("edad").value;
    const genero = document.getElementById("genero").value;
    const hipertenso = document.getElementById("hipertenso").value;
    const corazon = document.getElementById("corazon").value;
    const casado = document.getElementById("casado").value;
    const trabajo = document.getElementById("trabajo").value;
    const residencia = document.getElementById("residencia").value;
    const glucosa = document.getElementById("glucosa").value;
    const imc = document.getElementById("imc").value;
    const fumador = document.getElementById("fumador").value;

    const data = {
        age: parseFloat(edad),
        gender: parseInt(genero),
        hypertension: parseInt(hipertenso),
        heart_disease: parseInt(corazon),
        ever_married: parseInt(casado),
        work_type: parseInt(trabajo),
        Residence_type: parseInt(residencia),
        avg_glucose_level: parseFloat(glucosa),
        bmi: parseFloat(imc),
        smoking_status: parseInt(fumador),
    };
    

    fetch('http://127.0.0.1:5000/prediccion', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
        .then(response => response.json())
        .then(result => {
            document.getElementById('respuesta').innerHTML = `Respuesta: ${JSON.stringify(result)}`;
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById('respuesta').innerHTML = 'Ocurrió un error. Revisa la consola para más detalles.';
        });
}
