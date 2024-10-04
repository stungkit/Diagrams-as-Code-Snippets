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
set title "Git Commits per Month"
set xlabel "Year-Month"
set format x "%b %Y"
set xdata time
set timefmt "%Y-%m"
set output "images/git_commits_per_month.png"
plot "data/git_commits_per_month.dat" using 1:2 with boxes title 'Commits'
