from msgspec import Struct


class CustomerBrowser(Struct):
    accept_header: str | None
    color_depth: int | None
    ip: str | None
    language: str | None
    screen_height: int | None
    screen_width: int | None
    tz: int | None
    user_agent: str | None
    java_enabled: bool | None
    javascript_enabled: bool | None
    window_width: int | None
    window_height: int | None


class CustomerInfo(Struct):
    """Client data to create a payment."""

    email: str
    address: str | None
    city: str | None
    region: str | None
    postcode: str | None
    first_name: str
    last_name: str
    phone: str
    ip: str | None
    birthday: str | None
    street: str | None
    state: str | None
    browser: CustomerBrowser | None
    country: str
