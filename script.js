function getRandomValue() {
    return (Math.random() * 10 - 5).toFixed(2); // -5 to 5
}

function getSensorData() {
    return {
        shoulder_1: [getRandomValue(), getRandomValue(), getRandomValue()],
        shoulder_2: [getRandomValue(), getRandomValue(), getRandomValue()],
        neck: [getRandomValue(), getRandomValue(), getRandomValue()],
        back: [getRandomValue(), getRandomValue(), getRandomValue()]
    };
}

function checkPosture(data) {
    const s1 = data.shoulder_1;
    const s2 = data.shoulder_2;
    const neck = data.neck;
    const back = data.back;

    // Example Good Posture Rule:
    const shouldersAligned = Math.abs(s1[0] - s2[0]) < 2 && Math.abs(s1[1] - s2[1]) < 2;
    const spineAligned = Math.abs(neck[2] - back[2]) < 2;

    return shouldersAligned && spineAligned;
}

function updateUI(data, postureGood) {
    const sensorDiv = document.getElementById('sensor-data');
    sensorDiv.innerHTML = `
        <strong>Shoulder 1:</strong> [${data.shoulder_1.join(", ")}] <br>
        <strong>Shoulder 2:</strong> [${data.shoulder_2.join(", ")}] <br>
        <strong>Neck:</strong> [${data.neck.join(", ")}] <br>
        <strong>Back:</strong> [${data.back.join(", ")}]
    `;

    const statusDiv = document.getElementById('posture-status');
    if (postureGood) {
        statusDiv.textContent = "Posture: GOOD ✅";
        statusDiv.className = "good";
    } else {
        statusDiv.textContent = "Posture: BAD ❌";
        statusDiv.className = "bad";
    }
}

function loop() {
    const data = getSensorData();
    const postureGood = checkPosture(data);
    updateUI(data, postureGood);
}

setInterval(loop, 2000);
