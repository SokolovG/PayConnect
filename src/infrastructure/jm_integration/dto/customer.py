from msgspec import Struct


class CustomerBrowser(Struct):
    """Info about customer browser.

    Attributes:
        accept_header (str | None): Browser's Accept header.
        color_depth (int | None): Screen color depth.
        ip (str | None): Customer's IP address.
        language (str | None): Browser language.
        screen_height (int | None): Screen height in pixels.
        screen_width (int | None): Screen width in pixels.
        tz (int | None): Timezone offset.
        user_agent (str | None): Browser's User-Agent string.
        java_enabled (bool | None): Whether Java is enabled in the browser.
        javascript_enabled (bool | None): Whether JavaScript is enabled in the browser.
        window_width (int | None): Browser window width.
        window_height (int | None): Browser window height.

    """

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
    """Client data to create a payment.

    Attributes:
        email (str): Customer's email address.
        address (str | None): Customer's address.
        city (str | None): Customer's city.
        region (str | None): Customer's region.
        postcode (str | None): Customer's postal code.
        first_name (str): Customer's first name.
        last_name (str): Customer's last name.
        phone (str): Customer's phone number.
        ip (str | None): Customer's IP address.
        birthday (str | None): Customer's date of birth.
        street (str | None): Customer's street address.
        state (str | None): Customer's state.
        browser (CustomerBrowser | None): Customer's browser information.
        country (str): Customer's country code.

    """

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
