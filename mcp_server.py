from fastmcp import FastMCP
from fastmcp.utilities.types import Image
from mcp.types import ImageContent

from qr import generate_epc_qr_code, PaymentInfo

# Initialize the MCP server
mcp = FastMCP('sbley-qr-code')

@mcp.tool(name="generate_epc_qr_code")
def epc_qr_code(payment_info: PaymentInfo) -> ImageContent:
    """
    Generates an EPC QR code image based on the provided payment information and returns it as a base64-encoded string.
    """
    image = generate_epc_qr_code(payment_info)  # Should return a PIL Image or similar
    return _encode_image(image)

def _encode_image(image) -> ImageContent:
    """
    Encodes a PIL Image to a format compatible with ImageContent.
    """
    import io
    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    img_bytes = buffer.getvalue()
    img_obj = Image(data=img_bytes, format="png")
    return img_obj.to_image_content()


if __name__ == '__main__':
    mcp.run(transport='stdio')
