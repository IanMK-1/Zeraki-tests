CREATE TABLE IF NOT EXISTS student(
    student INT(11),
    name VARCHAR(250),
    course INT(11),
    FOREIGN KEY (course) REFERENCES course (courseid) ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS course (
    courseid INT(11),
    name VARCHAR(250),
    institution INT(11),
    FOREIGN KEY (institution) REFERENCES institution (institutionid) ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS institution (
    institutionid INT(11),
    name VARCHAR(250)
);

SELECT institution.name AS INSTITUTION_NAME, (SELECT course.name AS COURSE_NAME WHERE course.institution = institution.institutionid), (SELECT COUNT(student.studentid) AS NUMBER_OF_STUDENTS WHERE student.course = course.courseid) FROM student, course, institution;

