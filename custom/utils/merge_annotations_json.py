import json
import glob

result = []
ct_img_id = 0
ct_file = 0

# for each file
for f in glob.glob("C:/Users/baferreira/Downloads/merge_jsons/*.json"):
    with open(f, "rb") as infile:
        result.append(json.load(infile))

        # Fix image id field (different jsons have the same id for different images)  # noqa:E501
        # for each key
        for key in list(result[ct_file]):
            # increment image id
            ct_img_id += 1
            # replace old key for a correct one
            result[ct_file][str(ct_img_id)] = result[ct_file].pop(key)

            # Fix/update region_attributes
            for anot in range(len(result[ct_file][str(ct_img_id)]["regions"])):
                # if invalid key-value
                if result[ct_file][str(ct_img_id)]["regions"][anot]["region_attributes"] == {"pv": "1"}:  # noqa:E501
                    # change key
                    result[ct_file][str(ct_img_id)]["regions"][anot]["region_attributes"][str("name")] = result[ct_file][str(ct_img_id)]["regions"][anot]["region_attributes"].pop("pv")  # noqa:E501
                    # change value
                    result[ct_file][str(ct_img_id)]["regions"][anot]["region_attributes"].update({"name": "pv"})  # noqa:E501

    # increment file id
    ct_file += 1

# merge dicts
super_dict = {}
for i in result:
    for k, v in i.items():  # d.items() in Python 3+
        super_dict.setdefault(k, []).append(v)

# create new json
with open("merged_file.json", "w") as outfile:
    outfile.write(str(super_dict))
