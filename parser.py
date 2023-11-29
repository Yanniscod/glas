import argparse


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="RobotScheduler",
        description="Scheduler to automate the lab's worlkflows",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-p",
        "--port",
        type=int,
        default=8000,
        help="Port of the scheduler to communicate with",
    )
    parser.add_argument(
        "-n",
        "--nodes",
        type=str,
        default="./config/nodes.json",
        help="File path of the node descriptions",
        dest="path_to_nodes",
    )
    parser.add_argument(
        "-w",
        "--workflows",
        type=str,
        default="./config/workflows.json",
        help="File path of the workflow descriptions",
        dest="path_to_workflows",
    )
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose mode")
    parser.add_argument(
        "-l", "--logs", action="store_true", help="Store the logs in a file as well"
    )

    return parser.parse_args()