<!-- Copyright (c) 2024 David Caro <david@greyllama.cc>
All Rights Reserved.

This file is part of iphinter

iphinter is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

iphinter is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with Toolforge Builds-Api. If not, see <http://www.gnu.org/licenses/>.
-->

# IPHinter

This is a very small http server using only the python standard library that
will return the ip (and some extra data) of the caller.

## Example usage

```bash
$ python3 iphinter.py &
[1] 1125059
Starting on address 0.0.0.0 port 7777
   example: http://127.0.0.1:7777

$ curl http://127.0.0.1:7777
127.0.0.1 - - [08/Jun/2024 11:41:00] "GET / HTTP/1.1" 200 -
{
    "ip": "127.0.0.1",
    "headers": {
        "Host": "127.0.0.1:7777",
        "User-Agent": "curl/8.6.0",
        "Accept": "*/*"
    },
    "path": "/"
}
```
