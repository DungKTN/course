from config import cloudinary_config  # Chỉ cần import là config đã chạy
import cloudinary.uploader
from cloudinary.exceptions import Error as CloudinaryError

def upload_file_to_cloudinary(files, folder="uploads"):
    try:
        result =[]
        for file in files:
            upload_result = cloudinary.uploader.upload(
                file,
                folder=folder,
                resource_type="auto"  # Tự động nhận diện loại tệp (hình ảnh, video, v.v.)
            )
            result.append({
                "url": upload_result.get("secure_url"),
                "public_id": upload_result.get("public_id"),
                "format": upload_result.get("format")
            })
        return result  # Trả về danh sách nếu có nhiều tệp, ngược lại trả về đối tượng đơn
    except CloudinaryError as e:
        raise Exception(f"Upload to Cloudinary failed: {str(e)}")
def delete_file_from_cloudinary(public_ids):
    results = []
    for public_id in public_ids:
        try:
            cloudinary.uploader.destroy(public_id)
            results.append({"public_id": public_id, "deleted": True})
        except CloudinaryError as e:
            results.append({"public_id": public_id, "deleted": False, "error": str(e)})
    return results
