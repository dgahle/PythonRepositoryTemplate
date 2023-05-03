# Imports
from logging import Logger
from pathlib import Path
from time import perf_counter_ns

from .logger import get_logger

# Variables
logger: Logger = get_logger(Path(__file__).name)


# Functions
def runtime_to_msg(runtime: int, n_decimal: int = 3) -> str:
    n_decimal += 1
    # Time unit conversions
    ns_per_minute: int = 60000000000
    ns_per_hour: int = 3600000000000
    # Seconds check
    if runtime < 1e2:
        return f"Runtime is {runtime} ns!"
    elif runtime < 1e5:
        runtime: float = round(1e-3 * runtime, n_decimal)
        return f"Runtime is {runtime} us!"
    elif runtime < 1e8:
        runtime: float = round(1e-6 * runtime, n_decimal)
        return f"Runtime is {runtime} ms!"
    elif runtime < ns_per_minute:
        runtime: float = round(1e-9 * runtime, n_decimal)
        return f"Runtime is {runtime} s!"

    # Minutes check
    if runtime < ns_per_hour:
        minutes: int = int(runtime // ns_per_minute)
        seconds_ns: float = runtime - (minutes * ns_per_minute)
        seconds: int = int(1e-9 * seconds_ns)
        seconds_ms: int = round(1e-9 * seconds_ns - seconds)
        hours: int = 0
        return f"Runtime is {hours:02}:{minutes:02}:{seconds:02}.{seconds_ms:03}!"

    # Hour check
    raise NotImplementedError(
        f"Runtime is {round(runtime / ns_per_hour, n_decimal)} hrs"
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
