USERS=(U0101 U0102 U0103 U0104 U0105 U0106 U0107 U0108 U0109 U0110 U0111 U0201 U0202 U0203 U0204 U0205 U0206 U0207 U0208 U0209 U0210)
SESSIONS=(S0100 S0200 S0300 S0400 S0500)

for user in ${USERS[@]}; do
    for sess in ${SESSIONS[@]}; do
        make build USER=${user} SESSION=${sess}
    done
done