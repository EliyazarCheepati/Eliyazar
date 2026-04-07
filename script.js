const API = "http://localhost:5000/api/students";

// ADD STUDENT
const form = document.getElementById("studentForm");

if (form) {
    form.addEventListener("submit", async (e) => {
        e.preventDefault();

        const student = {
            name: document.getElementById("name").value,
            age: document.getElementById("age").value,
            course: document.getElementById("course").value,
            marks: document.getElementById("marks").value
        };

        await fetch(API, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(student)
        });

        alert("Student Added Successfully!");
        form.reset();
    });
}

// LOAD STUDENTS
async function loadStudents() {
    const res = await fetch(API);
    const data = await res.json();

    const table = document.getElementById("studentTable");

    if (table) {
        table.innerHTML = "";

        data.forEach((s) => {
            table.innerHTML += `
                <tr>
                    <td>${s.name}</td>
                    <td>${s.age}</td>
                    <td>${s.course}</td>
                    <td>${s.marks}</td>
                    <td>
                        <button onclick="deleteStudent('${s._id}')">Delete</button>
                    </td>
                </tr>
            `;
        });
    }
}

// DELETE STUDENT
async function deleteStudent(id) {
    await fetch(`${API}/${id}`, {
        method: "DELETE"
    });

    loadStudents();
}

// AUTO LOAD
loadStudents();