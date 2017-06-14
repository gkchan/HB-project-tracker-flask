"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)

    project_list = hackbright.get_grades_by_github(github)


    return render_template("student_info.html",
                           first=first,
                           last=last,
                           github=github,
                           project_list=project_list)

@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")

@app.route("/student-add")
def student_add():
    """Shows the form"""

    

    return render_template("new_student.html")

@app.route("/new-student-results", methods=['POST'])
def display_new_student():
    """Processes the form"""

    first = request.form.get('first')
    last = request.form.get('last')
    github = request.form.get('github')

    hackbright.make_new_student(first, last, github)

    return render_template("confirmation.html",
                           github=github)

@app.route("/project")
def get_and_display_project():
    """Show information about the student's project"""

    project = request.args.get('project')

    title, description, max_grade = hackbright.get_project_by_title(project)


    github_grade_list = hackbright.get_grades_by_title(project)

    return render_template("project_info.html",
                            title=title,
                            description=description,
                            max_grade=max_grade,
                            github_grade_list=github_grade_list)
                  


if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
