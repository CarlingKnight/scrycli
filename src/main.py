from src import lookup_query


def execute(args):
    possible_flags = ["--cmc", "--name"]

    arguments = ' '.join(args[1:])
    sorting = "cmc"

    for flag in possible_flags:
        if flag in arguments:
            arguments.replace(flag, "")
            sorting = flag.replace("--", "")

    lookup_query.print_query(arguments, sort_by=sorting)
