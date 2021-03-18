import time
import os
# from Bio import SeqIO
import multiprocessing as mp
# import numpy as np
import platform

import Util
import Logic
import LogicPrep
#################### st env ####################
WORK_DIR = os.getcwd() + "/"
PROJECT_NAME = WORK_DIR.split("/")[-2]
SYSTEM_NM = platform.system()

if SYSTEM_NM == 'Linux':
    # REAL
    pass
else:
    # DEV
    WORK_DIR = "D:/000_WORK/Ramu/20210318/WORK_DIR/"

IN = 'input/'
OU = 'output/'

os.makedirs(WORK_DIR + IN, exist_ok=True)
os.makedirs(WORK_DIR + OU, exist_ok=True)

INDEX_PAIRS = "Index_pairs.txt"
SEQ_TO_NUMID = "seq_to_numID.txt"
SAMPLE_ID_EXCEL = "Sequencing_Statistics_Result.xlsx"

RESULT_PATH = "Ramu_Sequencing_Statistics_Result"

TOTAL_CPU = mp.cpu_count()
MULTI_CNT = int(TOTAL_CPU*0.8)
#################### en env ####################


def find_index_id():
    util = Util.Utils()
    logic_prep = LogicPrep.LogicPreps()
    logic = Logic.Logics()

    index_pairs = util.read_tsv_ignore_N_line(WORK_DIR + IN + INDEX_PAIRS, 0)
    seq_to_numID_f = util.read_tsv_ignore_N_line(WORK_DIR + IN + SEQ_TO_NUMID, 0)
    sample_id_df = util.read_excel_to_df(WORK_DIR + IN + SAMPLE_ID_EXCEL, 'Sequencing Result', 0)

    index_pairs_dict = logic_prep.make_index_pairs_dict_by_list(index_pairs, 1, [0])
    seq_to_numID_dict = logic_prep.make_seq_to_numID_dict(seq_to_numID_f, 1, 0)

    result_list = logic.find_index_id_by_df(sample_id_df, index_pairs_dict, seq_to_numID_dict)

    header = ["SampleID", "", "A_id", "seq_A", "", "B_id", "seq_B", "", "num_id"]
    util.make_excel(WORK_DIR + OU +RESULT_PATH, header, result_list)


if __name__ == '__main__':
    start_time = time.perf_counter()
    print("start [ " + PROJECT_NAME + " ]>>>>>>>>>>>>>>>>>>")
    find_index_id()
    print("::::::::::: %.2f seconds ::::::::::::::" % (time.perf_counter() - start_time))