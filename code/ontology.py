import json


def load_data(fname):
    return json.load(open(fname))


if __name__ == "__main__":
    """This is how you load a json file, assuming you ran this from the base directory"""

    ont = load_data("data/data.json")
    print("there are %d nodes in the ontology" % len(ont))
