# lamps-ESP32

Created for personal usage only, no support guaranteed. Although I don't really see any point for anyone else to use this, I'm gonna try to help either over at discord (@siesta.161) or in the GitHub issues of this repo, if any problems arise (they probably will).

## Setup

First and foremost, you're gonna need a [Laterna](https://github.com/siestaw/laterna?tab=readme-ov-file#%EF%B8%8F-setup) server

#### 1. Flash [MicroPython](https://docs.micropython.org/en/latest/esp32/tutorial/intro.html) onto your model by following their documentation

#### 2. Configure this codebase

A [example config](https://github.com/siestaw/laterna-esp32/blob/main/config.json.example) is provided.

```sh
$ cp config.json.example config.json
```

<details><summary>Configuration explanation</summary>

```jsonc
{
    "wifi": {
        "SSID": "", // Name of the Wifi Network
        "password": "" // Pasword of the Wifi Network
    },
    "api": {
        "url": "http://...:8080/", // Laterna API address
        "token": "", // Laterna API token
        "id": 1, // Laterna Controller ID
        "poll_interval": 5 // Seconds to wait before pinging the server for color updates
    },
    "led": {
        "red": 26, // PIN of the red LED
        "green": 27, // PIN of the green LED
        "blue": 25, // PIN of the blue LED
        "internal": 2 // PIN of the internal LED (probably doesn't need to be changed)
    }
}
```

For more information on how to configure your Laterna server (token, controller ID), consult the [Laterna api documentation](https://github.com/siestaw/Laterna?tab=readme-ov-file#-api-documentation)

</details>

#### 3. Copy onto the microcontroller

for example, using [mpremote](https://docs.micropython.org/en/latest/reference/mpremote.html)

```sh
$ mpremote connect /dev/ttyUSB0 fs cp * :
```

You could also use the [MicroPico VS Code Extension](https://github.com/paulober/MicroPico) for the installation process. Despite it's name, it works wonderfully on ESP32 boards and has blessed me with an bearable developer experience instead of losing my sanity over mpremote

## Error Codes

| Color        | Interval | Message                               |
| ------------ | -------- | ------------------------------------- |
| Red          | 1        | Internal Wifi Error                   |
| Yellow       | 1        | API Connection Error                  |
| Blue         | 1        | Laterna Error (check your API config) |
| Internal LED | 1        | RGB LED configuration error           |

You can connect to the microcontroller over REPL to get more detailed error descriptions. After you've established an connection, exit the current file execution by running 'CTRL + C'. Then, import main to restart the program

```sh
$ mpremote connect /dev/ttyUSB0
> CTRL-C
>>> import main
```
