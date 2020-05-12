import os
site = """SEMESTRE 1 202
  ELEMENTOS DE COMPUTACION GR 7
  APRECIACION DE CINE GR 3
  CALCULO Y ALGEBRA LINEAL GR 8
  DIBUJO TECNICO GR 3
  FISICA GENERAL II GR 7
  INTR. TEC. CIENCIA Y TECNOLOGIA GR 12
  LABORATORIO FISICA GENERAL II GR 11
  COMUNICACION ESCRITA GR 25"""

courses = site.split("\n")
semester = courses[0]
courses.pop(0)
for place, course in enumerate(courses):
    course = course.strip()
    courses[place] = course
path = "C:/Users/Mariano/Desktop/Mariano/Documents"
os.mkdir(path + "/" + semester)
for course in courses:
    course_path = path + "/" + semester + "/" + course
    os.mkdir(course_path)
    print("creating directory {}".format(course_path))