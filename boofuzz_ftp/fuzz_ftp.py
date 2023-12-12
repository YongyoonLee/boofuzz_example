from boofuzz import *

def main():
    target_ip = "127.0.0.1"
    target_port = 8021

    session = Session(
        target=Target(
            connection=TCPSocketConnection(target_ip, target_port)
        ),
        sleep_time=1    # sec
    )

    define_protocol(session=session)
    session.fuzz()

def define_protocol(session:Session):
    user = Request("user", children =(
        String(name="key", default_value="USER", fuzzable=False),
        Delim(name="space", default_value=" ", fuzzable=False),
        String(name="val", default_value="anonymous", fuzzable=False),
        Static(name="end", default_value="\r\n")
    ))

    passw = Request("pass", children =(
        String(name="key", default_value="PASS", fuzzable=False),
        Delim(name="space", default_value=" ", fuzzable=False),
        String(name="val", default_value="james", fuzzable=False),
        Static(name="end", default_value="\r\n")
    ))

    stor = Request("stor", children =(
        String(name="key", default_value="STOR", fuzzable=False),
        Delim(name="space", default_value=" ", fuzzable=False),
        String(name="val", default_value="AAAA"),
        Static(name="end", default_value="\r\n")
    ))

    retr = Request("retr", children =(
        String(name="key", default_value="RETR", fuzzable=False),
        Delim(name="space", default_value=" ", fuzzable=False),
        String(name="val", default_value="AAAA"),
        Static(name="end", default_value="\r\n")
    ))

    session.connect(user)
    session.connect(user, passw)
    #session.connect(passw, stor)
    session.connect(passw, retr)

if __name__ == "__main__":
    main()