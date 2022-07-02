import sys


def change_file_func(config_file, sample_file):
    with open(config_file, 'r') as file:
        lines = file.readlines()
        lines = {line.strip().split("=")[0]: line.strip().split("=")[1] for line in lines}
    with open(sample_file, 'r') as file:
        output_data = file.readlines()

    changed_dict = {}
    new_output = []
    for new_line in output_data:
        line = new_line.strip()
        for key, value in lines.items():
            new_line = new_line.strip().replace(key, value)
        count = sum(1 for elm1, elm2 in zip(line, new_line) if elm1 != elm2)
        changed_dict[new_line] = count
        new_output.append(new_line)
    sorted_dict = dict(sorted(changed_dict.items(), key=lambda item: item[1], reverse=True))
    with open(sample_file, 'w') as file:
        for output in new_output:
            file.write(output + "\n")
    for key, value in sorted_dict.items():
        print("Changed line:", key, "Total number of symbols replaced:", value)


change_file_func(config_file=sys.argv[1], sample_file=sys.argv[2])