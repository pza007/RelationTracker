import pandas as pd
import numpy as np


class Database:
    __instance = None

    @staticmethod
    def get_instance():
        """
        Get instance of singleton class
        """
        if Database.__instance is None:
            Database()
        return Database.__instance

    def __init__(self, *args, **kwargs):
        if Database.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            super(Database, self).__init__(*args, **kwargs)
            Database.__instance = self

        # for current use
        self.names = []
        self.groups = []
        self.locations = []
        self.df_characters = pd.DataFrame()
        self.df_relations = pd.DataFrame()

        # for statistics
        self.stat_characters = {}
        self.stat_relations = {}

        self.get_characters_from_file("input_files\\characters.xlsx")
        self.get_relations_from_file("input_files\\relations.xlsx")

    def set_relation_value(self, name1, name2, in_value):
        self.df_relations[name1][name2] = in_value
        self.df_relations[name2][name1] = in_value

    def filter_characters(self, location, group, name):
        # df = df.loc[reduce(lambda x, y: x | y, [df['Location'] == val for val in locations]), :]

        # filter data
        df = self.df_characters
        if location:
            df = df.loc[df['Location'] == location, :]
        if group:
            df = df.loc[df['Group'] == group, :]
        if name:
            df = df.loc[df['Name'] == name, :]

        return df

    def get_characters_from_file(self, in_path):
        sheets = pd.read_excel(in_path, sheet_name=None)
        # statistics
        self.stat_characters = sheets
        # current
        df = sheets[list(sheets.keys())[-1]]
        self.names = list(set(df['Name'].values))
        self.groups = list(set(df['Group'].values))
        self.locations = list(set(df['Location'].values))
        self.df_characters = df

    def get_relations_from_file(self, in_path: str):
        """
        Convert dataframe entry to a list
            example: 0  ->  [0, []]
            example: "-1\n2 drink\n-3 fight"  ->  [-1, [(2, 'drink'), (-3, 'fight')]]
        """
        sheets = pd.read_excel(in_path, sheet_name=None)
        # statistics
        for key, value in sheets.items():
            df = value
            # drop "Unnamed" columns
            df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
            # replace nan to None
            df = df.replace({np.nan: None})
            # replace rows (from int to str => character names)
            df.index = df.columns.values
            # check if values are symmetric
            for row_name in df.index.values:
                for column_name in df.columns.values:
                    if df.at[row_name, column_name] != df.at[column_name, row_name]:
                        raise Exception(f'Values are not symmetric! [{row_name}][{column_name}]={df.at[row_name, column_name]} != [{column_name}][{row_name}]={df.at[column_name, row_name]}')
            # parse values
            for row_name in df.index.values:
                for column_name in df.columns.values:
                    val = df.loc[row_name, column_name]
                    # val = None
                    if val is None:
                        continue
                    # val = 0
                    elif isinstance(val, (float, int)):
                        out_val = [int(val), []]
                    elif val.count('\n') > 0:
                        splits = val.split('\n')
                        # val = "-1\n2 drink\n-3 fight"
                        tmp_list = []
                        for obj in splits[1:]:
                            idx_space = obj.find(' ')
                            tmp_list.append((int(obj[:idx_space]), str(obj[idx_space + 1:])))  # (-3, 'fight')
                        out_val = [int(splits[0]), tmp_list]
                    else:
                        raise Exception(f'Undefined value={val}')
                    # assign
                    df.loc[row_name, column_name] = out_val
                    sheets[key] = df
                    self.stat_relations[key] = df

        # current
        df = sheets[list(sheets.keys())[-1]]
        self.df_relations = df

        # add "new" characters that are not mentioned in relations
        if len(set(self.names) & set(self.df_relations.index.values)) != len(self.names):
            # add new columns and rows
            for ch_name in self.names:
                if ch_name not in self.df_relations.index.values:
                    new_df = pd.DataFrame(data='', columns=[ch_name], index=[ch_name])
                    self.df_relations = pd.concat([self.df_relations, new_df])
            # change values to [0, []] or None for added values
            for row_name in self.df_relations.index.values:
                for column_name in self.df_relations.columns.values:
                    val = self.df_relations.at[row_name, column_name]
                    if row_name == column_name:
                        self.df_relations.at[row_name, column_name] = None
                    elif isinstance(val, float) and pd.isna(val):
                        self.df_relations.at[row_name, column_name] = [0, []]
            self.df_relations = self.df_relations.replace({np.nan: None})
