# force in UF2 mode
import microcontroller
microcontroller.on_next_reset(microcontroller.RunMode.UF2)
microcontroller.reset()

# remote /boot.py (re-enable disk)
import os
os.remove("/boot.py")
import microcontroller
microcontroller.reset()


