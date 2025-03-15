from msgspec import Struct, field


class PaymentDetails(Struct):
    """Details of payment in the creation payment response."""

    amount: str
    currency: str
    status: str


class RedirectRequestParams(Struct):
    """Parameters for redirect request."""

    pa_req: str = field(name="PaReq")
    term_url: str = field(name="TermUrl")


class RedirectRequest(Struct):
    """Details for redirect request, for example, for 3DS."""

    url: str
    params: RedirectRequestParams
    type: str  # e.g. "post"
