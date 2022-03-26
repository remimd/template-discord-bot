bold=$(tput bold)
reset=$(tput sgr0)
cyan=$(tput setaf 6)

function title {
  if [ "$1" ]
  then
    entitled=$1
  else
    entitled="PLEASE PASS A TITLE"
  fi

  echo "${cyan}${bold}### $entitled ###${reset}"
}

if [ "$1" ]
then
  path=$1
else
  path="./"
fi

title "BLACK"
black "$path"

title "FLAKE"
flake8 "$path"
