# Imports
from logging import Logger
from pathlib import Path
from time import perf_counter_ns

from .logger import get_logger

# Variables
logger: Logger = get_logger(Path(__file__).name)


# Functions
def runtime_to_msg(runtime: int) -> str:
    # Time unit conversions
    ns_per_minute: int = 60000000000
    ns_per_hour: int = 3600000000000
    # Seconds check
    if runtime < 1e2:
        return f"Runtime is {runtime} ns!"
    elif runtime < 1e5:
        runtime: float = 1e-3 * runtime
        return f"Runtime is {runtime:.3f} us!"
    elif runtime < 1e8:
        runtime: float = 1e-6 * runtime
        return f"Runtime is {runtime:.3f} ms!"
    elif runtime < ns_per_minute:
        runtime: float = 1e-9 * runtime
        return f"Runtime is {runtime:.3f} s!"

    # Minutes check
    if runtime < ns_per_hour:
        minutes: float = runtime / ns_per_minute
        seconds_ns: float = runtime - (minutes * ns_per_minute)
        seconds: float = 1e-9 * seconds_ns
        seconds_ms: float = 1e-9 * seconds_ns - seconds
        hours: int = 0
        return f"Runtime is {hours:02}:{minutes:02}:{seconds:02}.{seconds_ms:.3f}!"

    # Hour check
    raise NotImplementedError(
        f"Runtime is {runtime / ns_per_hour} hrs"
    )


class TimeIt:
    def __init__(self, func):
        # Cache function to time
        self.func = func
        # Define print method
        self.print = print
        if "logger" in globals():
            self.print = logger.info

    def __call__(self, *args, **kwargs):
        # Run function and calculate runtime
        start_time: int = perf_counter_ns()
        output = self.func()
        runtime_ns: int = perf_counter_ns() - start_time
        # Format print message
        runtime_msg: str = runtime_to_msg(runtime_ns)
        self.print(runtime_msg)
        # Return output
        return output


@TimeIt
def main() -> None:
    pass


if __name__ == "__main__":
    main()
