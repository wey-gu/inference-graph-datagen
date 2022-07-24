import csv
import multiprocessing

from concurrent.futures import ProcessPoolExecutor

from faker import Faker
from rich import progress
from random import randint
from rich.console import Console
from rich.table import Table

#                        .─────.                             .─────.
#                       ╱       ╲                           ╱       ╲
#                      (    H    )                         (    I    )
#                       `.      '                           `.      '
#                         `──┬'                               `─▲─'
#                            │                                  │
#                            └ ─ ─ ─ ─ ─ ─ ─    ─ ─ ─ ─ ─ ─ ─ ─ ┘
#                                   e7      │  │       e8
#                                           │  │
#   .─────.            .─────.             .▼──┴─.            .─────.             .─────.
#  ╱       ╲          ╱       ╲           ╱       ╲          ╱       ╲           ╱       ╲
# (    A    )─ ─ ─ ─▶(    B    )─ ─ ─ ─ ▶(    C    )─ ─ ─ ─▶(    D    )─ ─ ─ ─ ▶(    E    )
#  `.      '    e1    `.      '    e2     `.      '   e3     `.      '    e4     `.      '
#    `───'              `──┬'               `───'              `───'               `───'
#                          │                                     ▲
#                          │                                     │
#                           ─ ─ ─ ─ ─ ─ ─        ─ ─ ─ ─ ─ ─ ─ ─ ┘
#                                 e5     │      │       e6
#
#                                        │      │
#                                        ▼.─────.
#                                        ╱       ╲
#                                       (    F    )
#                                        `.      '
#                                          `───'

# Vertices Count in TAG: A, B, C, D, E, F, H, I
# Edges Count in TAG: e1, e2, e3, e4, e5, e6, e7, e8

A_COUNT = 12183
B_COUNT = 1560
C_COUNT = 31469
D_COUNT = 31409
E_COUNT = 47104
F_COUNT = 644794
H_COUNT = 183
I_COUNT = 184

e1_COUNT = 5841
e2_COUNT = 31469
e3_COUNT = 31469
e4_COUNT = 29469
e5_COUNT = 644794
e6_COUNT = 644794
e7_COUNT = 31408
e8_COUNT = 31408

WRITE_BATCH = 10000  # Larger requires more memory
# Maximum partition size, try putting your CPU_count * 4 or a larger number here
WORKCER_COUNT = 8
PARTITION_COUNT = 10  # Partition count per generation job
console = Console()


def log(message):
    console.log("\n[bold bright_cyan][ Info:[/bold bright_cyan]", message)


def title(title, description=None):
    table = Table(show_header=True)
    table.add_column(title, style="dim", width=96)
    if description:
        table.add_row(description)
    console.log("\n", table)


def csv_writer(file_path, row_count, row_generator, index=False, index_prefix="", init_index=0):
    with open(file_path, mode='w') as file:
        if index:
            cursor = int(init_index)
        writer = csv.writer(
            file, delimiter=',', quotechar="'", quoting=csv.QUOTE_MINIMAL)
        csv_buffer = list()
        for row in range(row_count):
            if index:
                csv_buffer.append(
                    (f"{index_prefix}{cursor}",) + row_generator())
                cursor += 1
            else:
                csv_buffer.append(row_generator())
            if len(csv_buffer) > WRITE_BATCH:
                writer.writerows(csv_buffer)
                del csv_buffer[:]
        if csv_buffer:
            writer.writerows(csv_buffer)
            del csv_buffer[:]


faker = Faker("zh_CN")


def tag_generator():
    """
    (name)
    """
    return (faker.name(),)


def edge_generator_template(src_prefix, src_count, dst_prefix, dst_count):
    """
    (source_vid, destination_vid)
    """
    def edge_generator():
        return (
            f"{ src_prefix }_{ randint(0, src_count - 1) }",
            f"{ dst_prefix }_{ randint(0, dst_count - 1) }")
    return edge_generator


def gen_tag_a(i, task_id):

    partition_size = A_COUNT // WORKCER_COUNT
    csv_writer(
        f"data/A_{i}.csv",
        partition_size,
        tag_generator,
        index=True,
        index_prefix=f"a",
        init_index=i * (partition_size))
    log(f"task: {task_id} partition: {i} finshed.")


def gen_tag_b(i, task_id):

    partition_size = B_COUNT // WORKCER_COUNT
    csv_writer(
        f"data/B_{i}.csv",
        partition_size,
        tag_generator,
        index=True,
        index_prefix=f"b",
        init_index=i * (partition_size))
    log(f"task: {task_id} partition: {i} finshed.")


def gen_tag_c(i, task_id):

    partition_size = C_COUNT // WORKCER_COUNT
    csv_writer(
        f"data/C_{i}.csv",
        partition_size,
        tag_generator,
        index=True,
        index_prefix=f"c",
        init_index=i * (partition_size))
    log(f"task: {task_id} partition: {i} finshed.")


def gen_tag_d(i, task_id):

    partition_size = D_COUNT // WORKCER_COUNT
    csv_writer(
        f"data/D_{i}.csv",
        partition_size,
        tag_generator,
        index=True,
        index_prefix=f"d",
        init_index=i * (partition_size))
    log(f"task: {task_id} partition: {i} finshed.")


def gen_tag_e(i, task_id):

    partition_size = E_COUNT // WORKCER_COUNT
    csv_writer(
        f"data/E_{i}.csv",
        partition_size,
        tag_generator,
        index=True,
        index_prefix=f"e",
        init_index=i * (partition_size))
    log(f"task: {task_id} partition: {i} finshed.")


def gen_tag_f(i, task_id):

    partition_size = F_COUNT // WORKCER_COUNT
    csv_writer(
        f"data/F_{i}.csv",
        partition_size,
        tag_generator,
        index=True,
        index_prefix=f"f",
        init_index=i * (partition_size))
    log(f"task: {task_id} partition: {i} finshed.")


def gen_tag_h(i, task_id):

    partition_size = H_COUNT // WORKCER_COUNT
    csv_writer(
        f"data/H_{i}.csv",
        partition_size,
        tag_generator,
        index=True,
        index_prefix=f"h",
        init_index=i * (partition_size))
    log(f"task: {task_id} partition: {i} finshed.")


def gen_tag_i(i, task_id):

    partition_size = I_COUNT // WORKCER_COUNT
    csv_writer(
        f"data/I_{i}.csv",
        partition_size,
        tag_generator,
        index=True,
        index_prefix=f"i",
        init_index=i * (partition_size))
    log(f"task: {task_id} partition: {i} finshed.")


def gen_edge_e1(i, task_id):
    csv_writer(
        f"data/e1_{i}.csv",
        e1_COUNT // WORKCER_COUNT,
        edge_generator_template("a", A_COUNT, "b", B_COUNT))
    log(f"task: {task_id} partition: {i} finshed.")


def gen_edge_e2(i, task_id):
    csv_writer(
        f"data/e2_{i}.csv",
        e2_COUNT // WORKCER_COUNT,
        edge_generator_template("b", B_COUNT, "c", C_COUNT))
    log(f"task: {task_id} partition: {i} finshed.")


def gen_edge_e3(i, task_id):
    csv_writer(
        f"data/e3_{i}.csv",
        e3_COUNT // WORKCER_COUNT,
        edge_generator_template("c", C_COUNT, "d", D_COUNT))
    log(f"task: {task_id} partition: {i} finshed.")


def gen_edge_e4(i, task_id):
    csv_writer(
        f"data/e4_{i}.csv",
        e4_COUNT // WORKCER_COUNT,
        edge_generator_template("d", D_COUNT, "e", E_COUNT))
    log(f"task: {task_id} partition: {i} finshed.")


def gen_edge_e5(i, task_id):
    csv_writer(
        f"data/e5_{i}.csv",
        e5_COUNT // WORKCER_COUNT,
        edge_generator_template("b", B_COUNT, "f", F_COUNT))
    log(f"task: {task_id} partition: {i} finshed.")


def gen_edge_e6(i, task_id):
    csv_writer(
        f"data/e6_{i}.csv",
        e6_COUNT // WORKCER_COUNT,
        edge_generator_template("f", F_COUNT, "d", D_COUNT))
    log(f"task: {task_id} partition: {i} finshed.")


def gen_edge_e7(i, task_id):
    csv_writer(
        f"data/e7_{i}.csv",
        e7_COUNT // WORKCER_COUNT,
        edge_generator_template("h", H_COUNT, "c", C_COUNT))
    log(f"task: {task_id} partition: {i} finshed.")


def gen_edge_e8(i, task_id):
    csv_writer(
        f"data/e8_{i}.csv",
        e8_COUNT // WORKCER_COUNT,
        edge_generator_template("c", C_COUNT, "i", I_COUNT))
    log(f"task: {task_id} partition: {i} finshed.")


tasks = [
    ("TAG:A", gen_tag_a), ("TAG:B", gen_tag_b), ("TAG:C", gen_tag_c),
    ("TAG:D", gen_tag_d), ("TAG:E", gen_tag_e), ("TAG:F", gen_tag_f),
    ("TAG:H", gen_tag_h), ("TAG:I", gen_tag_i),
    ("EDGE:E1", gen_edge_e1), ("EDGE:E2", gen_edge_e2),
    ("EDGE:E3", gen_edge_e3), ("EDGE:E4", gen_edge_e4),
    ("EDGE:E5", gen_edge_e5), ("EDGE:E6", gen_edge_e6),
    ("EDGE:E7", gen_edge_e7), ("EDGE:E8", gen_edge_e8)]


if __name__ == "__main__":

    title(
        "[bold blue][ Generating Data ] [/bold blue]",
        f"Will be running with maximum {WORKCER_COUNT} processes")

    with progress.Progress(
        "[progress.description]{task.description}",
        progress.BarColumn(),
        "[progress.percentage]{task.percentage:>3.0f}%",
        progress.TimeRemainingColumn(),
        progress.TimeElapsedColumn(),
        refresh_per_second=1,  # bit slower updates
    ) as progress:
        futures = []  # keep track of the jobs
        with multiprocessing.Manager() as manager:

            overall_progress_task = progress.add_task(
                "[green]All jobs progress:")

            with ProcessPoolExecutor(max_workers=WORKCER_COUNT) as executor:
                for t in tasks:
                    progress.add_task(t[0], visible=False)
                    for p in range(PARTITION_COUNT):
                        futures.append(executor.submit(t[1], p, t[0]))

                while (n_finished := sum([future.done() for future in futures])) < len(
                    futures
                ):
                    progress.update(
                        overall_progress_task, completed=n_finished, total=len(
                            futures)
                    )

                for future in futures:
                    future.result()
