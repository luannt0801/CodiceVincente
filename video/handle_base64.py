import base64

def encode_image_to_base64(image_path: str) -> str:
    """
    Đọc file ảnh và mã hóa sang chuỗi Base64.

    Args:
        image_path (str): Đường dẫn đến file ảnh (png, jpg, v.v.)

    Returns:
        str: Chuỗi Base64 (đã mã hóa UTF-8)
    """
    with open(image_path, "rb") as image_file:
        encoded_bytes = base64.b64encode(image_file.read())
        encoded_str = encoded_bytes.decode("utf-8")
    return encoded_str


def decode_base64_to_image(b64_string: str, output_path: str) -> None:
    """
    Giải mã chuỗi Base64 và lưu thành file ảnh.

    Args:
        b64_string (str): Chuỗi Base64
        output_path (str): Đường dẫn file ảnh xuất ra (ví dụ 'output.png')
    """
    image_data = base64.b64decode(b64_string)
    with open(output_path, "wb") as f:
        f.write(image_data)
