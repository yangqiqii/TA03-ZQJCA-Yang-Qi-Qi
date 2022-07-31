from pathlib import Path
import api, overheads, cash_on_hand, profit_loss
def mainSolution():
    """
    """
    summary_file = Path.cwd()/"summary_report.txt"
    summary_file.touch()
    cohindex = 0
    plindex = 0
    cohsummary = cash_on_hand.cash_on_hand()
    plsummary = profit_loss.profit_loss()
    with summary_file.open(mode = "w", encoding = "UTF-8") as file:
        file.writelines(api.api())
    with summary_file.open(mode = "a", encoding = "UTF-8") as file:
        file.writelines(f" \n{overheads.overheads()}")
        while cohindex < len(cohsummary):
            file.writelines(f" \n{cohsummary[cohindex]}")
            cohindex +=1
        while plindex < len(plsummary):
            file.writelines(f"\n{plsummary[plindex]}")
            plindex += 1
mainSolution()