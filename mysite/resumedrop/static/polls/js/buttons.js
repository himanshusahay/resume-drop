document.getElementById("student_button").onclick = function () {
        location.href = "{% url 'resumedrop:student_create' %}";
    };

document.getElementById("company_button").onclick = function () {
	    location.href = "{% url 'admin:index' %}";
	};