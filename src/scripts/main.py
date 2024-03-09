import pandas as pd
import os
import glob

folder_path = 'src\\data\\raw'

excel_files = glob.glob( os.path.join(folder_path, '*.xlsx'))

if not excel_files:
    print("No archives find in folder")
else:
    dfs = []

    for file in excel_files:
        try: 
            df_temp = pd.read_excel(file)

            file_name = os.path.basename(file)
            
            df_temp['filename'] = file_name

            if 'brasil' in file_name.lower():
                df_temp['location'] = 'br'
            elif 'france' in file_name.lower():
                df_temp['location'] = 'fr'
            elif 'italia' in file_name.lower():
                df_temp['location'] = 'it'

            df_temp['campaign'] = df_temp['utm_link'].str.extract(r'utm_campaign=(.*)')

            dfs.append(df_temp)

        except Exception as e:
            print(f"Error reading the file {file} : {e}")

if dfs:
    result = pd.concat(dfs, ignore_index=True)

    output_file = os.path.join('src', 'data', 'ready', 'clean.xlsx')

    writer = pd.ExcelWriter(output_file, engine='xlsxwriter')

    result.to_excel(writer, index=False)
    
    #salva o arquivo de excel
    writer._save()
else:
    print("No data to be saved")