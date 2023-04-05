ports=("/dev/ttyACM0" "/dev/ttyUSB0")
for elem in ${ports[@]}; do
sudo chmod a+rw $elem
done
