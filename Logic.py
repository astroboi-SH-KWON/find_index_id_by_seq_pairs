
from astroboi_bio_tools.ToolLogic import ToolLogics
class Logics(ToolLogics):
    def find_index_id_by_df(self, sample_id_df, index_dict, seq_num_dict):
        result_list = []
        df_len = len(sample_id_df)
        for row in range(df_len):
            sample_nm = sample_id_df.loc[row][0]
            seq_arr = sample_nm.replace("4_", "").split("-")
            num_id = seq_num_dict[seq_arr[1]].replace("D", "") + seq_num_dict[seq_arr[0]].replace("D", "-")
            result_list.append(
                ["Sample_" + sample_nm, "", seq_num_dict[seq_arr[0]], seq_arr[0], "", seq_num_dict[seq_arr[1]],
                 seq_arr[1], "", index_dict[num_id][0]])

        return result_list
