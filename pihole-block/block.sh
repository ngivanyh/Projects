h=$(date +"%H")
m=$(date +"%M")

if [ $h -ge 16 ] && [ $h -le 19 ]
then
    pihole -b youtube.com
    pihiole -wild youtube.com
    restartdns
elif [ $h -eq 19 ] && [ $m -gt 00 ]
then
    pihole -b -d youtube.com
    pihiole -wild -d youtube.com
    restartdns
fi