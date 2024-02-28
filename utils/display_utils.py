from IPython.display import clear_output

# displays the running info of the arms_histroy
def display_info(remaining_tries, arms_history = dict()):
    clear_output()  # clear the whole screen
    print("Arms history:")

    for i, ibandit in enumerate(arms_history.keys()):
        print(ibandit, i, ":", arms_history[ibandit])

    print("Tries Remaining: ", remaining_tries)

def display_summary(summary):
    print("=== SUMMARY of Pulls ===")
    print("   ", summary)
    print("=========================")
