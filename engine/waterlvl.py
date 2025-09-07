#waterlvl.py
import eel

@eel.expose
def update_water_level(percentage: int):
    """
    Sends water level percentage to frontend.
    :param percentage: int (0-100)
    """
    eel.setWaterLevel(percentage)

