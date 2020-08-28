class Preset:
    def __init__(self):
        self.presets = {
            "signed_percent_error": (self.signed_pe, -1, 1),
            "abs_percent_error": (self.abs_pe, 0, 1),
            "relative_distance": (self.rel_dist, 0, 1),
        }
        self.short_name = {
            "spe": self.presets["signed_percent_error"],
            "ape": self.presets["abs_percent_error"],
            "rd" : self.presets["relative_distance"],
        }

    def abs_pe(self, actual, desired, diff, itr):
        """
        Diff is populated with % Error and undefined based on % Error Equation
        Later to be filtered to remove undefined Error.
        """
        if (actual[itr] == 0 and desired[itr] == 0):
            diff.append(0)
        elif (desired[itr]) != 0:
            diff.append(abs(actual[itr]-desired[itr])/abs(desired[itr]))
        else:
            diff.append("undefined")


    def signed_pe(self, actual, desired, diff, itr):
        """
        Diff is populated with +/- % Error and undefined based on % Error Equation
        Later to be filtered to remove undefined Error. 
        """
        if (actual[itr] == 0 and desired[itr] == 0):
            diff.append(0)
        elif (desired[itr]) != 0:
            diff.append((actual[itr]-desired[itr])/float(abs(desired[itr])))
        else:
            diff.append("undefined")

    def rel_dist(self, actual, desired, diff, itr):
        """
        Difference is populated with relative difference. Normalize in [0,1] range for normalization.
        """
        if (actual[itr] == 0 and desired[itr] == 0):
            diff.append(0)
        else:
            diff.append(abs(actual[itr]-desired[itr])/((abs(actual[itr])+abs(desired[itr]))/2))

    def __call__(self, str):
        return self.short_name[str]

    def help_message(self):
        msg = "<" + ' | '.join([k for k in self.short_name.keys()]) + "> ----- " + ', '.join([m for m in self.presets.keys()])
        return msg

