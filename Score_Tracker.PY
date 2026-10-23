# ============================
# Introduction to Matplotlib
# ============================

# =========================================
# Activity - My Score Tracker
# File: DSCM8L3-Jr-activity-complete.PY
# =========================================

# Part 1 - Import Matplolib
# Before drawing any chart you need to import the matplotlib library
# matplotlib.pylot is the drawing tool -- "plt" is it's short nickname
import matplotlib.pyplot as plt

# Part 2 - Your Data
# days hold the x-axis labels -- the days of your school week
# scores hold the y-axis values -- your quiz score for each day
# every score pairs up with the day in the same position
days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
scores = [70, 85, 60, 90, 75]

# Part 3 - Plot your first line graph
# plt.plot(x, y) draws a line through all your data points
# plt.show() opens the cart window -- call it at the end of every chart
plt.plot(days, scores)
plt.show()

# Part 4 - Add labels ad a title
# plt.title()    -- adds a heading at the top of the chart
# plt.xlabel()    -- labels the x-axis (across the bottom)
# plt.ylabel()    -- labels the y-axis (up to side)
# plt.grid(True)    -- adds faint gridlines so values are easier to read
# plrt.ylim(0, 100) -- locks the y-aix from 0 to 100 so scores fit neatly
plt.plot(days, scores)
plt.title("My Quiz Tracker")
plt.xlabel("Day of the week")
plt.ylabel("Score")
plt.grid(True)
plt.ylim(0, 100)
plt.show()

# Part 5 - Style your line chart
# color="blue"    -- changes the line color
#marker="0"    -- puts a filled dot on every data point
# linestyle="dashed"    -- draws the line as dashes instead of solid
# linewidth=2    -- makes the line thicker so it stands out
# All four styles options go inside the same plt.plot() call
plt.plot(days, scores, color="Blue", marker="o", linestyle="dashed", linewidth=2)
plt.title("My Quiz Tracker")
plt.xlabel("Day of the week")
plt.ylabel("Score")
plt.grid(True)
plt.ylim(0, 100)
plt.show()

# Part 6 - Draw a bar chart
# plt.bar(x, y) draws a bar chart -- one bar per day rising to it's score
# Bar charts are great for comparing values side by side
# color="orange" fills every bar with orange
# The same title, labels and ylim commands work exactly the same way
plt.bar(days, scores, color="orange")
plt.title("My Quiz Score Bar Chart")
plt.xlabel("Day of the Week")
plt.ylabel("Score")
plt.ylim(0, 100)
plt.show()