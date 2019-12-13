def update_reputation_from_patch(rep_file, rep_rev, patch, remote_rev):
    f = open(rep_file, "r")
    rep_data = f.read()
    f.close()

    rep_data = rep_data.split("\n")
    patch_data = frozenset(patch.split("\n"))

    for i in patch_data:
        try:
            if i != "":
                if i[0] == "-":
                    line = list(i)  # Delete first char
                    line[0] = ""
                    line = "".join(line)
                    rep_data.remove(line)
                elif i[0] == "+":
                    line = list(i)  # Delete first char
                    line[0] = ""
                    line = "".join(line)
                    rep_data.append(line)
        except:
            pass

    # Dump new reputation
    f = open(rep_file, "w")
    for ln in rep_data:
        if ln != "":
            f.write("%s\n" % ln)
    f.close()

    # Dump new revision
    # f = open(rep_rev, "w")
    # f.write(remote_rev)
    # f.close()


refilee = "9_third_party_modules/rep_data.txt"
pat = "9_third_party_modules/path.txt"
update_reputation_from_patch(rep_file=refilee, patch=pat, )