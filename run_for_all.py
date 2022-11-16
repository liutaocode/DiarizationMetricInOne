#!/usr/bin/env python
import os
from argparse import ArgumentParser
from tabulate import tabulate

def print_table(collar, MS, FA, SC, OVL, DER, JER, CDER, SER, BER, ref_part, fa_dur, fa_seg, fa_mean, n_digits=2, table_format='simple'):
    floatfmt = '.%df' % n_digits
    rows = []
    col_names = ['collar', 'MS', 'FA', 'SC', 'OVL', 'DER', 'JER', 'CDER', 'SER', 'BER', 'ref_part', 'fa_dur', 'fa_seg', 'fa_mean']
    rows.append((collar, MS, FA, SC, OVL, DER, JER, CDER, SER, BER, ref_part, fa_dur, fa_seg, fa_mean))
    tbl = tabulate(
        rows, headers=col_names, floatfmt=floatfmt, tablefmt=table_format)
    print(tbl)

def main():
    ref_rttm_file = args.ref_rttm_fns
    ref_total_seg_num = len(open(ref_rttm_file).readlines())

    hyp_rttm_file = args.sys_rttm_fns
    hyp_total_seg_num = len(open(hyp_rttm_file).readlines())

if __name__ == "__main__":
    parser = ArgumentParser(
        description='SD diarization from RTTM files.', add_help=True,
        usage='%(prog)s [options]')
    parser.add_argument('-s', dest='sys_rttm_fns', help='system RTTM files (default: %(default)s)')
    parser.add_argument('-r', dest='ref_rttm_fns', help='reference RTTM files (default: %(default)s)')
    args = parser.parse_args()

    ref_rttm_file = args.ref_rttm_fns
    hyp_rttm_file = args.sys_rttm_fns

    # dscore
    cmd = "python ./dscore-ovl/score.py -s %s -r %s"%(hyp_rttm_file, ref_rttm_file)
    total_result = os.popen(cmd).readlines()[-1]
    items = total_result.replace("\n","").split()
    collar, MS, FA, SC, OVL, DER, JER = float(items[0]),float(items[1])*0.01,float(items[2])*0.01,float(items[3])*0.01,float(items[4])*0.01,float(items[5])*0.01,float(items[6])*0.01

    # CDER
    cmd = "python ./CDER_Metric/score.py -s %s -r %s"%(hyp_rttm_file, ref_rttm_file)
    total_result = os.popen(cmd).readlines()[-1]
    CDER = float(total_result.replace("\n","").split(":")[-1])

    #BER
    cmd = "python ./BER/score.py -s %s -r %s"%(hyp_rttm_file, ref_rttm_file)
    result = os.popen(cmd).readlines()[-1]
    items = result.replace("\n","").split()

    SER, BER, ref_part, fa_dur, fa_seg, fa_mean = float(items[0]),float(items[1]),float(items[2]),float(items[3]),float(items[4]),float(items[5])

    print_table(collar, MS, FA, SC, OVL, DER, JER, CDER, SER, BER, ref_part, fa_dur, fa_seg, fa_mean)
