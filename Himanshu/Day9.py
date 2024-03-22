student_scores={"Harry": 81,"Ron": 78,"Hermione": 99,"Draco": 74,"Neville": 62,}      #giving input

student_grades = student_scores.copy()

# Changing according to the scoring criteria for Students

for i in student_scores:
  score = student_scores[i]
  if score > 90:
    student_grades[i] = "Outstanding"
  elif score > 80:
    student_grades[i] = "Exceeds Expectations"
  elif score > 70:
    student_grades[i] = "Acceptable"
  else:
    student_grades[i] = "Fail"

# The final version of the student_grades dictionary###*/
###* @INFO
###* Bot Coded by Royaloakap| https://discord.gg/RoyalC2
###* @INFO
###* Please mention HRoyaloakap, when using this Code
###* @INFO
###* Telegram - https://t.me/royal_faq
###*/
