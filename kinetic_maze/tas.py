import time
import json
import odrive.enums


def tas(kmm, filename, tracker=None):
    with open(filename, "r") as f:
        route = json.load(f)
    path = route["path"]
    for step in path:
        if step["kind"] == "pause":
            time.sleep(step["duration"])
        elif step["kind"] == "move":
            kmm.go_to_angle(step["target"],
                            direction=step.get("direction"),
                            max_velocity=step.get("max_velocity"),
                            max_accel=step.get("max_accel"),
                            max_decel=step.get("max_decel"))
        elif step["kind"] == "wait":
            if not tracker:
                if input("Continue? (Y/n) > ").lower().startswith("n"):
                    return
            else:
                tracker.sync_stream()
                res = tracker.wait_for_dab(timeout=step.get("timeout"),
                                           must_have_other_user=True)
                if not res:
                    return
        else:
            raise ValueError("Invalid step kind %r" % (step["kind"],))

def zero_current(kmm):
    with kmm.axis_context(control_mode=odrive.enums.CTRL_MODE_CURRENT_CONTROL):
        kmm.axis().controller.current_setpoint = 0
        input("Zero current mode enabled. Press enter to continue. ")
