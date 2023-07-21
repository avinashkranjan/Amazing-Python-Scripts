# Intruder Detector UI
This is a web-based UI specifically designed to display the information that the  Intruder Detector reference implementation processes.   
This web browser UI is not real-time, but uses the information processed by the application. Because of this, the UI should be started after the application has been stopped.

## Running the UI

Go to UI directory present in this project directory:
```
cd UI
```
### Install the dependencies

```
sudo apt install composer
composer install
```
Run the following command on the terminal to open the UI.<br>
Chrome*:
```
google-chrome  --user-data-dir=$HOME/.config/google-chrome/Intruder-detector --new-window --allow-file-access-from-files --allow-file-access --allow-cross-origin-auth-prompt index.html
```
Firefox*:
```
firefox index.html
```
**_Note:_** For Firefox*, if the alerts list does not appear on the right side of the browser window, click anywhere on video progress bar to trigger a refresh.
