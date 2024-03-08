import os

if __name__ == '__main__':
    cur_dir_path = os.getcwd()
    covers_dir_path = os.path.join(cur_dir_path, '16khz')
    print(covers_dir_path)
    print(os.listdir(covers_dir_path))

    profiles_dir_path = os.path.join(cur_dir_path, 'vocalProfiles')
    print(profiles_dir_path)
    print(os.listdir(profiles_dir_path))
    print(len(os.listdir(covers_dir_path)))

    # for each profile, run it on the cover and then output the csv
    # file in ./testResults
    ACCESS_KEY=os.environ.get('ACCESS_KEY')

    # We only need to replace these files:
    missing_excel_files = os.listdir(os.path.join(os.getcwd(), 'missingExcelFiles'))
    print(missing_excel_files)
    print(len(missing_excel_files))
    j = []

    for profile in os.listdir(profiles_dir_path):
        if profile[0] == '.': continue
        for cover in os.listdir(covers_dir_path):
            if cover[0] == '.': continue
            # print(cover, profile)
            tokens = cover.split('.')
            output = profile.upper() + ''.join(tokens[:len(tokens) - 1]) + '.csv'

            test_audio_path = f'./16khz/{cover}'
            if output not in missing_excel_files:
                continue

            print(cover, profile)

            print('Running', f'python eagle_demo_file.py test --access_key {ACCESS_KEY} --input_profile_paths ./vocalProfiles/{profile} --test_audio_path {test_audio_path} --csv_output_path ./redoneExcelFiles/{output}')
            os.system(f'python eagle_demo_file.py test --access_key {ACCESS_KEY} --input_profile_paths ./vocalProfiles/{profile} --test_audio_path {test_audio_path} --csv_output_path ./redoneExcelFiles/{output}')

    print(len(j))