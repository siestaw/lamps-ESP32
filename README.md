# lamps-ESP32

Created for personal usage only, no support guaranteed. Although I don't really see any point for anyone else to use this, I'm gonna try to help either over at discord (@siesta.161) or in the GitHub issues of this repo, if any problems arise (they probably will).

## Setup

#### 0.5. Setup a [Laterna](https://github.com/siestaw/laterna?tab=readme-ov-file#%EF%B8%8F-setup) server

#### 1. Flash [MicroPython](https://docs.micropython.org/en/latest/esp32/tutorial/intro.html) onto your model by following their documentation

#### 2. Configure this codebase

A [example config](https://github.com/siestaw/laterna-esp32/blob/main/config.json.example) is provided.

```sh
$ cp config.json.example config.json
```

#### 3. Copy onto the microcontroller

for example, using [mpremote](https://docs.micropython.org/en/latest/reference/mpremote.html)

```sh
$ mpremote connect /dev/ttyUSB0 fs cp * :
```

You could also use the [MicroPico VS Code Extension](https://github.com/paulober/MicroPico) for the installation process. Despite it's name, it works wonderfully on ESP32 boards and has blessed me with an bearable developer experience instead of losing my sanity over mpremote

## Error Codes

| Color  | Interval | Message             |
| ------ | -------- | ------------------- |
| Red    | 1        | Internal Wifi Error |
| Yellow | 0.5      | API Error           |
