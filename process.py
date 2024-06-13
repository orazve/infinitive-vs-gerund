import itertools
from collections import defaultdict

import pandas as pd
from verbs import __v_to, __v_ing, __v_obj_to, __v_obj_ing
from patterns import __pattern_ing, __pattern_to, __pattern_obj_ing, __pattern_obj_to


def find_contexts(song_dict, pattern):
    d = defaultdict(list)
    for key, value in song_dict.items():
        matches = pattern.finditer(value)
        for match in matches:
            g = match.groups()
            d[key].append(f"{g[0]} __{g[1].lower()}__ {g[2]}")
    sorted_dict = dict(sorted(d.items()))
    return sorted_dict


def process_dataset(head=-1):
    df = pd.read_csv("../processed.csv")

    keys = zip(df['artist'], df['song'])
    vals = [text.replace("\n", " ") for text in df['text'].tolist()]
    all_songs = dict(zip(keys, vals))
    if head == -1:
        return all_songs
    else:
        return dict(itertools.islice(all_songs.items(), head))


def print_out_results(forms, songs, f):
    print("", file=f, flush=True)
    print(f"## {forms[0]}", file=f)
    print("| Song | Context |", file=f)
    print("| --- | --- |", file=f)
    for song, contexts in songs.items():
        song_artist_and_title = f"{song[0]} _\"{song[1]}\"_"
        print(f"| {song_artist_and_title} | "+'<br>'.join(contexts) + " |", file=f, end=' <br /> \n')
    pass


def process():
    songs_dict = process_dataset()

    dict_of_tasks = {
        "VERB + ING": (__pattern_ing, __v_ing),
        "VERB + TO": (__pattern_to, __v_to),
        "VERB + OBJ + ING": (__pattern_obj_ing, __v_obj_ing),
        "VERB + OBJ + TO": (__pattern_obj_to, __v_obj_to)
    }

    for task, (func_pattern, func_verbs) in dict_of_tasks.items():
        filename = f"__res_{task.replace(' + ', '_').lower()}.md"
        print(f"Processing {task} to {filename}")
        with open(filename, 'w') as f:
            for forms in func_verbs():
                print(f"Searching for {task}: {forms}")
                songs = find_contexts(songs_dict, func_pattern(forms))
                print_out_results(forms, songs, f)


if __name__ == "__main__":
    process()
