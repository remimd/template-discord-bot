bold=$(tput bold)
reset=$(tput sgr0)
cyan=$(tput setaf 6)

path="./"

if [ "$1" ]
then
  path=$1
fi

echo "${cyan}${bold}### BLACK ###${reset}"
black "$path"

echo "${cyan}${bold}### FLAKE ###${reset}"
flake8 "$path"
