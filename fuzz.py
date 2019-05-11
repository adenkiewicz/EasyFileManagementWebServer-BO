#!/usr/bin/env python3
from boofuzz import s_initialize, s_static, s_string, s_get, Session, Target, SocketConnection


def main():
    session = Session(
            target=Target(connection=SocketConnection("192.168.0.101", 80, proto='tcp')),
            )

    s_initialize(name="Command")
    s_static("GET /vfolder.ghp HTTP/1.1\r\n")
    s_static("Host: 192.168.0.101\r\n")
    s_static("User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0\r\n")
    s_static("Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n")
    s_static("Accept-Language: en-US,en;q=0.5\r\n")
    s_static("Accept-Encoding: gzip, deflate\r\n")
    s_static("Referer: http://192.168.0.101/login.htm\r\n")
    s_static("Content-Type: application/x-www-form-urlencoded\r\n")
    s_static("Content-Length: 60\r\n")
    s_static("Cookie: UserID=")
    s_string("1")  # this is the part we fuzz
    s_static("\r\n")
    s_static("Cache-Control: max-age=0\r\n")
    s_static("\r\nConnection: close\r\n\r\n")

    session.connect(s_get("Command"))

    session.fuzz()


if __name__ == "__main__":
    main()
