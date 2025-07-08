from mcp.server.fastmcp import FastMCP

import qr
from qr import generate_epc_qr_code, PaymentInfo

# Initialize the MCP server
mcp = FastMCP('sbley-qr-code')

@mcp.tool(name="generate_epc_qr_code")
def epc_qr_code(payment_info: PaymentInfo) -> str:
    """
    Generates an EPC QR code image based on the provided payment information and returns it as a base64-encoded string.
    """
    image = generate_epc_qr_code(payment_info)  # Should return a PIL Image or similar
    return _encode_image_to_base64(image)

def _encode_image_to_base64(image):
    """
    Encodes a PIL Image to a base64 string.
    """
    import io
    import base64
    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    return base64.b64encode(buffer.getvalue()).decode("utf-8")

if __name__ == '__main__':
    mcp.run(transport='stdio')
