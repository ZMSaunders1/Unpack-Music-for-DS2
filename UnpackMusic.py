import fsb5
import os
import argparse

parser = argparse.ArgumentParser(description="Unpacks DS2:SotfS music")
parser.add_argument("-c", type=str, required=True, help="The location of the sound directory (C:\Program Files (x86)\Steam\steamapps\common\Dark Souls II: Scolar of the first Sin\sound)")

fileNames = ["frpg2_smain.fsb",
             "frpg2_sm1002.fsb",
             "frpg2_sm1004.fsb",
             "frpg2_sm1010.fsb",
             "frpg2_sm1014.fsb",
             "frpg2_sm1015.fsb",
             "frpg2_sm1015.fsb",
             "frpg2_sm1017.fsb",
             "frpg2_sm1018.fsb",
             "frpg2_sm1018.fsb",
             "frpg2_sm1023.fsb",
             "frpg2_sm1025.fsb",
             "frpg2_sm1027.fsb",
             "frpg2_sm1031.fsb",
             "frpg2_sm1032.fsb",
             "frpg2_sm1033.fsb",
             "frpg2_sm1034.fsb",
             "frpg2_sm2010.fsb",
             "frpg2_sm2011.fsb",
             "frpg2_sm2021.fsb",
             "frpg2_sm2024.fsb",
             "frpg2_sm4003.fsb",
             "frpg2_sm5035.fsb",
             "frpg2_sm5036.fsb",
             "frpg2_sm5037.fsb",
             "frpg2_sm7021.fsb"
             ]
numFiles = len(fileNames)

songNames = [["m000000002","m000000003","m000000010","m000000014"],
             ["m100200001"],
             ["m100400001"],
             ["m101000001","m101000002"],
             ["m101400001","m101400002"],
             ["m101500001"],
             ["m101600001","m101600002","m101600003"],
             ["m101700001","m101700002"],
             ["m101800001"],
             ["m101900001","m101900002"],
             ["m102300001","m102300002"],
             ["m102500001"],
             ["m102700001"],
             ["m103100001","m103100002"],
             ["m103200001","m103201040"],
             ["m103300001"],
             ["m103400001"],
             ["m201000001"],
             ["m201100001","m201100002"],
             ["m102800001","m102800002","m102100001","m102100002","m102100003","m760203000"],
             ["m202400001","m202400002"],
             ["m400300001"],
             ["Queen_sm_sing_a_song2",  "m503500001","m503500002","m503500003"],
             ["KOKUEN-KISHI-NEW2",      "m101900001","m101900002"],
             ["ARSHUNA-NEW2","FDP_b05_b1_test06","FDP_b13_b0_test03"],
             ["m202100004_andeal",      "m702100001","m702100002"]
             ]

realNames = [["Main_Menu_Screen","Longing","You_Died_Sound","Title_Screen_Appearing"],
             ["Things_Betwixt"],
             ["Majula"],
             ["Last_Giant","The_Pursuer"],
             ["Duke's_Dear_Freja","Prowling_Magus"],
             ["Guardian Dragon"],
             ["Lost_Sinner","Ruin_Sentinels","Bell_Gargoyles"],
             ["Mytha,_the_Baneful_Queen","Covetous_Demon"],
             ["Flexile_Sentry"],
             ["Old_Iron_King","Smelter_Demon"],
             ["Skeleton_Kings","Executioner's_Chariot"],
             ["The_Rotton"],
             ["Ancient_Dragon"],
             ["Dragonrider","Old_Dragonslayer"],
             ["Scorpioness_Najka","Ornifex_Sound_Effects"],
             ["Royal_Rat_Authority"],
             ["Royal_Rat_Vanguard"],
             ["Giant_Lord"],
             ["Demon_of_Song","Milfanito_Singing"],
             ["Nashandra","Throne_Watcher_&_Defender","Looking_Glass_Knight","Twin_Dragonriders","Milfanito_Song","Trapped_Milfanito_Singing"],
             ["Velstadt,_the_Royal_Aegis","Vendrick"],
             ["Darklurker"],
             ["Elana_Singing","Elana","Sihn,_the_Slumbering_Dragon","Graverobber,_Varg_&_Cerah"],
             ["Fume_Knight","Sir_Alonne","Blue_Smelter_Demon"],
             ["Burnt_Ivory_King","Aava,_King's_Pet","Lud_&_Zallen,_King's_Pets"],
             ["Aldia,_Scholar_of_the_First_Sin","Credits,_No_Link","Credits,_Link"]
             ]

args = parser.parse_args()
directory = args.c

for i in range (0,numFiles):
    file = os.path.join(directory,fileNames[i])

    with open(file, 'rb') as f:
        fsb = fsb5.FSB5(f.read())
#    print(fsb.header)
        ext = fsb.get_sample_extension()
    
    for j in range(0,len(songNames[i])):
        song = songNames[i][j]
        for sample in fsb.samples:
            if(song==sample.name):
                with open(f"./output/{realNames[i][j]}.{ext}","wb") as g:
                    rebuilt_sample = fsb.rebuild_sample(sample)
                    g.write(rebuilt_sample)

        

