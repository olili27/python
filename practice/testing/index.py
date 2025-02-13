from kisa_utils.response import Response, Ok

def test(a: int) -> Response:
    """_summary_

    Args:
        a (int): _description_

    Returns:
        Response: _description_
    """
    return Ok(a * a)


def add(a, b):
    return a + b
