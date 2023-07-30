# importing requiered modules
import win10toast
import speedtest

st = speedtest.Speedtest()

# download speed
download = st.download() / 1048576

# upload speed
upload = st.upload() / 1048576
servernames = []
names = st.get_servers(servernames)

# ping
ping = st.results.ping

# storing the values in a list
data = [download, upload, ping]
formated_data = ["%.2f" % elem for elem in data]

# creating a message for the notification
message = "Download Speed: {}Mbps, \nUpload Speed: {}Mbps,\n Ping: {}ms".format(
    *formated_data
)

# creating a notification window
toaster = win10toast.ToastNotifier()

# printing the data
print(message)

# displaying the notification
toaster.show_toast("Wifi Speedtest Successfull!", message, duration=20)