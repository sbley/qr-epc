import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import SquareModuleDrawer
from pydantic import BaseModel

class PaymentInfo(BaseModel):
    bic: str
    name: str
    iban: str
    amount: float
    description: str

def generate_epc_qr_code(payment_info: PaymentInfo):
    """
    Generates an EPC QR code based on the provided payment information.

    Args:
        payment_info (PaymentInfo): Contains BIC, name, IBAN, amount, and description.

    Returns:
        PIL Image: The generated QR code image.
    """
    epc_string = _create_epc_string(payment_info)
    qr_code_image = _create_qr_code(epc_string)
    return qr_code_image

def _create_epc_string(payment_info: PaymentInfo):
    return f"""BCD
        001
        1
        SCT
        {payment_info.bic}
        {payment_info.name}
        {payment_info.iban}
        EUR{payment_info.amount:.2f}
        CHAR

        {payment_info.description}"""

def _create_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=3,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(image_factory=StyledPilImage, module_drawer=SquareModuleDrawer())
    return img
