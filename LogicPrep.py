
from astroboi_bio_tools.ToolLogicPrep import ToolLogicPreps

import Logic
class LogicPreps(ToolLogicPreps):
    def make_index_pairs_dict_by_list(self, index_pairs_list, key_idx, ele_idx_arr):
        result_dict = {}
        for idx_pairs_arr in index_pairs_list:
            key = idx_pairs_arr[key_idx]
            if key in result_dict:
                print(key, "is not unique")
            else:
                tmp_arr = []
                for i in ele_idx_arr:
                    tmp_arr.append(idx_pairs_arr[i])
                result_dict.update({key: tmp_arr})
        return result_dict

    def make_seq_to_numID_dict(self, seq_to_numID_list, key_idx, ele_idx):
        logic = Logic.Logics()
        result_dict = {}
        for seq_to_numID_arr in seq_to_numID_list:
            p_key = seq_to_numID_arr[key_idx]
            m_key = logic.make_complement_string(p_key)[::-1]
            if p_key in result_dict:
                print(p_key, "is not unique")
            else:
                result_dict.update({p_key: seq_to_numID_arr[ele_idx]})
            if m_key in result_dict:
                print(m_key, "is not unique")
            else:
                result_dict.update({m_key: seq_to_numID_arr[ele_idx]})

        return result_dict
