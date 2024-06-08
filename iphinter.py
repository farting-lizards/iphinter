#!/usr/bin/env python3
# Copyright (c) 2024 David Caro <david@greyllama.cc>
# All Rights Reserved.
#
# This file is part of iphinter
#
# iphinter is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# iphinter is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with Toolforge Builds-Api. If not, see <http://www.gnu.org/licenses/>.

import argparse
import http
import http.server
import io
import json
from shutil import copyfileobj


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self) -> None:
        data = {
            "ip": self.client_address[0],
            "headers": {key: value for key, value in self.headers.items()},
            "path": self.path,
        }
        bytes_data = json.dumps(data, indent=4).encode("utf-8")
        self.send_response(http.HTTPStatus.OK)
        self.send_header("X-Origin-Ip", str(self.client_address[0]))
        self.send_header("Content-type", "application/json")
        self.send_header("Content-Length", str(len(bytes_data)))
        self.end_headers()

        response_bytes = io.BytesIO()
        response_bytes.write(bytes_data)
        response_bytes.seek(0)
        try:
            copyfileobj(fsrc=response_bytes, fdst=self.wfile)  # type:ignore
        finally:
            response_bytes.close()


def main(port: int) -> None:
    address = "0.0.0.0"
    print(f"Starting on address {address} port {port}")
    reachable_address = address if address != "0.0.0.0" else "127.0.0.1"
    print(f"   example: http://{reachable_address}:{port}")
    s = http.server.HTTPServer((address, port), Handler)
    s.serve_forever()


if __name__ == "__main__":
    parser = argparse.ArgumentParser("iphinter")
    parser.add_argument("--port", type=int, default=7777)
    args = parser.parse_args()
    main(port=args.port)
