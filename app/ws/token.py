import secrets

_tokens = {}


def create(server: str):
    token = secrets.token_hex(32)
    _tokens[token] = server

    print("=" * 50)
    print("CREATE TOKEN")
    print("SERVER :", server)
    print("TOKEN  :", token)
    print("TOKENS :", _tokens)
    print("=" * 50)

    return token


def verify(server: str, token: str):
    print("=" * 50)
    print("VERIFY")
    print("SERVER :", server)
    print("TOKEN  :", token)
    print("TOKENS :", _tokens)
    print("LOOKUP :", _tokens.get(token))
    print("RESULT :", _tokens.get(token) == server)
    print("=" * 50)

    return _tokens.get(token) == server


def revoke(token: str):
    _tokens.pop(token, None)
