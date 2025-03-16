from msgspec import Struct, field


class PaymentDetails(Struct):
    """Details of payment in the creation payment response.

    Attributes:
        amount (str): Amount of the payment.
        currency (str): Currency code of the payment.
        status (str): Current status of the payment.

    """

    amount: str
    currency: str
    status: str


class RedirectRequestParams(Struct):
    """Parameters for redirect request.

    Attributes:
        pa_req (str): Payment authentication request.
        term_url (str): URL to which the browser should be redirected after authentication.

    """

    pa_req: str = field(name="PaReq")
    term_url: str = field(name="TermUrl")


class RedirectRequest(Struct):
    """Details for redirect request, for example, for 3DS.

    Attributes:
        url (str): URL to redirect the user to.
        params (RedirectRequestParams): Parameters to include in the redirect.
        type (str): Type of redirect (e.g. "post").

    """

    url: str
    params: RedirectRequestParams
    type: str  # e.g. "post"


class ErrorDetail(Struct):
    """Details of the API error.

    Attributes:
        code (str): Error code.
        kind (str): Type or category of the error.

    """

    code: str
    kind: str
