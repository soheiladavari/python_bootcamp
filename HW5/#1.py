from datetime import datetime


class WiFiMixin:
    def connect_wifi(self):
        print(f"{self.name} connected to Wi-Fi.")


class LogMixin:
    def log_event(self, message):
        with open("events.log", "a", encoding="utf-8") as file:
            file.write(f"{datetime.now()} - {message}\n")


class Device:
    def __init__(self, device_id, name):
        self.id = device_id
        self.name = name
        self._is_active = False

    @property
    def is_active(self):
        return self._is_active

    def turn_on(self):
        self._is_active = True
        print(f"{self.name} turned on.")

    def turn_off(self):
        self._is_active = False
        print(f"{self.name} turned off.")

    def __str__(self):
        status = "ON" if self.is_active else "OFF"
        return f"{self.name} - {status}"

    def __eq__(self, other):
        if not isinstance(other, Device):
            return False
        return self.id == other.id
class Light(Device, WiFiMixin, LogMixin):
    def turn_on(self):
        super().turn_on()
        self.log_event(f"{self.name} turned on")


class AirConditioner(Device, WiFiMixin, LogMixin):
    def turn_on(self):
        super().turn_on()
        self.log_event(f"{self.name} turned on")

    def turn_off(self):
        super().turn_off()
        self.log_event(f"{self.name} turned off")


class Television(Device, WiFiMixin):
    def turn_on(self):
        super().turn_on()


class DoorLock(Device, LogMixin):
    def lock(self):
        self._is_active = True
        print(f"{self.name} locked.")
        self.log_event(f"{self.name} locked")

    def unlock(self):
        self._is_active = False
        print(f"{self.name} unlocked.")
        self.log_event(f"{self.name} unlocked")

    def __str__(self):
        status = "LOCKED" if self.is_active else "UNLOCKED"
        return f"{self.name} - {status}"


class Camera(Device, WiFiMixin, LogMixin):
    def turn_on(self):
        super().turn_on()
        self.log_event(f"{self.name} turned on")


class SmartPlug(Device, WiFiMixin):
    def turn_on(self):
        super().turn_on()

class Home:
    def __init__(self, name):
        self.name = name
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)
        print(f"{device.name} added to {self.name}.")

    def find_device(self, device_id):
        for device in self.devices:
            if device.id == device_id:
                return device
        return None

    def remove_device(self, device_id):
        device = self.find_device(device_id)

        if device:
            self.devices.remove(device)
            print(f"{device.name} removed from {self.name}.")
        else:
            print("Device not found.")

    def device_count(self):
        return len(self.devices)

    def show_status(self):
        print("\n===== HOME STATUS =====")
        for device in self.devices:
            print(device)
        print("=======================\n")

    def info(self):
        print(f"Home: {self.name}")
        print(f"Number of devices: {len(self.devices)}")

    def __len__(self):
        return len(self.devices)

home = Home("My Smart Home")

light = Light(1, "Living Room Light")
ac = AirConditioner(2, "Air Conditioner")
tv = Television(3, "Television")
door = DoorLock(4, "Front Door")
camera = Camera(5, "Security Camera")

home.add_device(light)
home.add_device(ac)
home.add_device(tv)
home.add_device(door)
home.add_device(camera)

print("\nTotal devices:", len(home))

light.connect_wifi()
camera.connect_wifi()

light.turn_on()
ac.turn_on()
tv.turn_on()
camera.turn_on()

door.lock()

home.show_status()

found = home.find_device(2)

if found:
    print("Found:", found)

home.remove_device(3)

ac.turn_off()

home.show_status()

home.info()

light2 = Light(1, "Another Light")

print("\nComparison:")
print("light == light2:", light == light2)