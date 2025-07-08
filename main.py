from qr import generate_epc_qr_code, PaymentInfo

def main():
    print("Hello, QR Code Generator!")

    payment_info = PaymentInfo(
        bic="BP0TBEB1",
        name="Red Cross of Belgium",
        iban="BE72000000001616",
        amount=1.9,
        description="Rechnung 123"
    )

    img = generate_epc_qr_code(payment_info)
    img.save("qr-code.png")


if __name__ == "__main__":
    main()
