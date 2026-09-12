
document.getElementById("analyzeBtn").addEventListener("click", async function () {

    const jobDescription =
        document.getElementById("job_description").value;

    const skills =
        document.getElementById("skills").value;


    document.getElementById("requiredSkills").innerText =
        "Analyzing...";

    document.getElementById("yourSkills").innerText = "";

    document.getElementById("missingSkills").innerText = "";

    document.getElementById("learningRoadmap").innerText = "";


    const response = await fetch("/analyze", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            job_description: jobDescription,
            skills: skills
        })

    });


    const result = await response.json();


    document.getElementById("requiredSkills").innerHTML =
        result.required_skills
            .map(skill => `<span class="skill">${skill}</span>`)
            .join("");


    document.getElementById("yourSkills").innerHTML =
        result.your_skills
            .map(skill => `<span class="skill">${skill}</span>`)
            .join("");


    document.getElementById("missingSkills").innerHTML =
        result.missing_skills
            .map(skill => `<span class="skill">${skill}</span>`)
            .join("");


    document.getElementById("learningRoadmap").innerText =
        result.learning_roadmap;

});

