while  [ true ]
do
    now=$(date +"%T")
    if [ "$now" == "09:43:00" ] # set a fixed time that you want to send emails each day
    then
        # echo "Current time: $now"
        python3 main.py
        sleep 10
        # break
    fi
done