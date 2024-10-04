#
# Generated by git_graph_commit_history_gnuplot.sh
#
# from https://github.com/HariSekhon/DevOps-Bash-tools
#
set terminal pngcairo size 1280,720 enhanced font 'Arial,14'
set ylabel 'Number of Commits'
set grid
set xtics rotate by -45
set boxwidth 0.5 relative
set style fill solid
set datafile separator ' '
set title "Git Commits per Year"
set xlabel "Year"
# results in X axis labels every 2 years
#set xdata time
#set timefmt "%Y"
#set format x "%Y"
# trick to get X axis labels for every year
stats "data/git_commits_per_year.dat" using 1 nooutput
set xrange [STATS_min:STATS_max]
set xtics 1
set output "images/git_commits_per_year.png"
plot "data/git_commits_per_year.dat" using 1:2 with boxes title 'Commits'
