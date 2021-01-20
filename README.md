Just some tool scripts for GW2.

Dual licensed CC0/WTFPL - chose whichever you prefer.

## checkoff.py

Test w/`python checkoff.py`; create config.json as:
```
{
  "key": "<key here, needs progression permission>",
  "reset": "17",
  "path": "<path to file w/date>"
}
```

Reset is which hour in 24 hour format the dailies reset in your timezone.

Requires the `requests` library to be installed.

### Install

- Create `config.json`
- `cp checkoff.service ~/.config/systemd/user/`
- `cp checkoff.timer ~/.config/systemd/user/`
- Modify `~/.config/systemd/user/checkoff.service` to point to where checkoff.py is located
- `systemctl --user enable checkoff.timer`
- `systemctl --user start checkoff.timer`
