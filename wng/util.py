def pyccle_to_text(s):
    return " ".join(map(lambda x: x.split("\t")[0],
                        s.split("\n")))
