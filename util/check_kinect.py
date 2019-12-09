import time
import os


SYSFS_USB_PATH = "/sys/bus/usb/devices"

SYSFS_USB_VENDOR_FNAME  = "idVendor"
SYSFS_USB_PRODUCT_FNAME = "idProduct"

SYSFS_USB_AUTHORIZED_FNAME = "authorized"
RESET_DELAY_TIME = 1
KINECT_INITIALIZATION_TIME = 5

KINECT_HUB_VENDOR  = 0x0409
KINECT_HUB_PRODUCT = 0x005a

def find_kinect_hub():
    # Iterate over all usb devices
    for device in os.listdir(SYSFS_USB_PATH):
        dev_path = os.path.join(SYSFS_USB_PATH, device)
        vendor_path  = os.path.join(dev_path, SYSFS_USB_VENDOR_FNAME)
        product_path = os.path.join(dev_path, SYSFS_USB_PRODUCT_FNAME)

        # Ensure that the device has a vendor and product
        if not (os.path.exists(vendor_path) and os.path.exists(product_path)):
            continue

        # Check if they are the kinect vendor and product
        # Place inside a try/catch in case the device disappears while we are iterating
        try:
            with open(vendor_path, "rb") as f:
                if int(f.read(4), 16) != KINECT_HUB_VENDOR:
                    # Vendor didn't match; skip this one
                    continue
            with open(product_path, "rb") as f:
                if int(f.read(4), 16) != KINECT_HUB_PRODUCT:
                    # Product didn't match; skip this one
                    continue

            return dev_path
        except OSError as e:
            # If this was due to permissions, re-raise it so that it can be fixed
            # (Probably by re-running as root)
            if isinstance(e, PermissionError):
                raise
            # Otherwise, the device was probably just removed while we were checking, so move on
            pass
    raise FileNotFoundError("Could not find Kinect hub")

def reset_device(path):
    authorized_path = os.path.join(path, SYSFS_USB_AUTHORIZED_FNAME)
    with open(authorized_path, "wb") as f:
        # Disable communication
        f.write(b"0\n")
        # Wait a second for the device to fully uninitialize
        time.sleep(RESET_DELAY_TIME)
        # Re-enable communication, forcing the device to re-initialize
        f.write(b"1\n")

def reset_kinect():
    reset_device(find_kinect_hub())
    time.sleep(KINECT_INITIALIZATION_TIME)

def check_kinect():
    pass


if __name__ == "__main__":
    reset_kinect()
