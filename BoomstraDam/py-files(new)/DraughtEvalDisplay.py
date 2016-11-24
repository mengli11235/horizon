#
#  This file is Copyright (C) 2010 Feike Boomstra.
#  Distributed under the Boost Software License, Version 1.0.
#  (See accompanying file LICENSE_1_0.txt or copy at
#  http://www.boost.org/LICENSE_1_0.txt)
#


from Tkinter import *
import tkFont
from DraughtDataStructures import *
from DraughtConstants import *
dc = DraughtConstants()

class EvalParameters:
    def __init__(self):
        self.man_value=StringVar()
        self.king_value=StringVar()
        self.man_position=StringVar()
        self.king_position=StringVar()
        self.tempi_score=StringVar()
        self.fit_score =StringVar()
        self.row_score=StringVar()
        self.freedom=StringVar()
        self.maze_penalty=StringVar()
        self.man_locked=StringVar()
        self.avoid_4641=StringVar()
        self.avoid_2324=StringVar()
        self.avoid_2335=StringVar()
        self.leg_2_8_13=StringVar()
        self.tri_253035=StringVar()
        self.klassiek=StringVar()
        self.ketting_stelling=StringVar()
        self.halve_hek=StringVar()
        self.active_15=StringVar()
        self.slechte_binding=StringVar()
        self.free_path=StringVar()
        self.edge_35=StringVar()
        self.edge_36=StringVar()
        self.t11_16_17=StringVar()
        self.voorpost=StringVar()
        self.locked=StringVar()
        self.vleugel_opsluiting=StringVar()
        self.tandem=StringVar()
        self.canon=StringVar()
        self.endgame =StringVar()
        self.score = StringVar()
        return

class DraughtEval:
    def __init__(self, eval_frame):
        self.white = EvalParameters()
        self.black = EvalParameters()
        self.diff    = EvalParameters()
        #bold font
        self.myFont = tkFont.Font(family="helvetica", weight="bold", size=10)
        # header
        Label(eval_frame, text="param",anchor=W, bd=3,relief=RIDGE, width=17,font=self.myFont).grid(column=0,row=0)
        Label(eval_frame, text="white",anchor=E, bd=3,relief=RIDGE, width=5,bg="#fff",font=self.myFont).grid(column=1,row=0)
        Label(eval_frame, text="black",anchor=E, bd=3,relief=RIDGE, width=6,bg="#eee",font=self.myFont).grid(column=2,row=0)
        Label(eval_frame, text="diff",anchor=E, bd=3,relief=RIDGE, width=6,bg="#fff",font=self.myFont).grid(column=3,row=0)
        
        Label(eval_frame, text="man_value",anchor=W).grid(column=0,row=1,sticky=W)
        Label(eval_frame, text="king_value",anchor=W).grid(column=0,row=2,sticky=W)
        Label(eval_frame, text="man_position",anchor=W).grid(column=0,row=3,sticky=W)
        Label(eval_frame, text="king_position",anchor=W).grid(column=0,row=4,sticky=W)
        Label(eval_frame, text="tempi_score",anchor=W).grid(column=0,row=5,sticky=W)
        Label(eval_frame, text="fit_score ",anchor=W).grid(column=0,row=6,sticky=W)
        Label(eval_frame, text="row_score",anchor=W).grid(column=0,row=7,sticky=W)
        Label(eval_frame, text="freedom",anchor=W).grid(column=0,row=8,sticky=W)
        Label(eval_frame, text="maze_penalty",anchor=W).grid(column=0,row=9,sticky=W)
        Label(eval_frame, text="man_locked",anchor=W).grid(column=0,row=10,sticky=W)
        Label(eval_frame, text="avoid_4641",anchor=W).grid(column=0,row=11,sticky=W)
        Label(eval_frame, text="avoid_2324",anchor=W).grid(column=0,row=12,sticky=W)
        Label(eval_frame, text="avoid_2335",anchor=W).grid(column=0,row=13,sticky=W)
        Label(eval_frame, text="leg_2_8_13",anchor=W).grid(column=0,row=14,sticky=W)
        Label(eval_frame, text="tri_253035",anchor=W).grid(column=0,row=15,sticky=W)
        Label(eval_frame, text="klassiek",anchor=W).grid(column=0,row=16,sticky=W)
        Label(eval_frame, text="ketting_stelling",anchor=W).grid(column=0,row=17,sticky=W)
        Label(eval_frame, text="halve_hek",anchor=W).grid(column=0,row=18,sticky=W)
        Label(eval_frame, text="active_15",anchor=W).grid(column=0,row=19,sticky=W)
        Label(eval_frame, text="slechte_binding",anchor=W).grid(column=0,row=20,sticky=W)
        Label(eval_frame, text="free_path",anchor=W).grid(column=0,row=21,sticky=W)
        Label(eval_frame, text="edge_35",anchor=W).grid(column=0,row=22,sticky=W)
        Label(eval_frame, text="edge_36",anchor=W).grid(column=0,row=23,sticky=W)
        Label(eval_frame, text="t11_16_17",anchor=W).grid(column=0,row=24,sticky=W)
        Label(eval_frame, text="voorpost",anchor=W).grid(column=0,row=25,sticky=W)
        Label(eval_frame, text="locked",anchor=W).grid(column=0,row=26,sticky=W)
        Label(eval_frame, text="vleugel_opsluiting",anchor=W).grid(column=0,row=27,sticky=W)
        Label(eval_frame, text="tandem",anchor=W).grid(column=0,row=28,sticky=W)
        Label(eval_frame, text="canon",anchor=W).grid(column=0,row=29,sticky=W)
        Label(eval_frame, text="endgame",anchor=W).grid(column=0,row=30,sticky=W)
        Label(eval_frame, text="score",anchor=W).grid(column=0,row=31,sticky=W)

        Label(eval_frame, textvariable=self.white.man_value,anchor=E,bg="#fff").grid(column=1,row=1,sticky=E)
        Label(eval_frame, textvariable=self.white.king_value,anchor=E,bg="#fff").grid(column=1,row=2,sticky=E)
        Label(eval_frame, textvariable=self.white.man_position,anchor=E,bg="#fff").grid(column=1,row=3,sticky=E)
        Label(eval_frame, textvariable=self.white.king_position,anchor=E,bg="#fff").grid(column=1,row=4,sticky=E)
        Label(eval_frame, textvariable=self.white.tempi_score,anchor=E,bg="#fff").grid(column=1,row=5,sticky=E)
        Label(eval_frame, textvariable=self.white.fit_score ,anchor=E,bg="#fff").grid(column=1,row=6,sticky=E)
        Label(eval_frame, textvariable=self.white.row_score,anchor=E,bg="#fff").grid(column=1,row=7,sticky=E)
        Label(eval_frame, textvariable=self.white.freedom,anchor=E,bg="#fff").grid(column=1,row=8,sticky=E)
        Label(eval_frame, textvariable=self.white.maze_penalty,anchor=E,bg="#fff").grid(column=1,row=9,sticky=E)
        Label(eval_frame, textvariable=self.white.man_locked,anchor=E,bg="#fff").grid(column=1,row=10,sticky=E)
        Label(eval_frame, textvariable=self.white.avoid_4641,anchor=E,bg="#fff").grid(column=1,row=11,sticky=E)
        Label(eval_frame, textvariable=self.white.avoid_2324,anchor=E,bg="#fff").grid(column=1,row=12,sticky=E)
        Label(eval_frame, textvariable=self.white.avoid_2335,anchor=E,bg="#fff").grid(column=1,row=13,sticky=E)
        Label(eval_frame, textvariable=self.white.leg_2_8_13,anchor=E,bg="#fff").grid(column=1,row=14,sticky=E)
        Label(eval_frame, textvariable=self.white.tri_253035,anchor=E,bg="#fff").grid(column=1,row=15,sticky=E)
        Label(eval_frame, textvariable=self.white.klassiek,anchor=E,bg="#fff").grid(column=1,row=16,sticky=E)
        Label(eval_frame, textvariable=self.white.ketting_stelling,anchor=E,bg="#fff").grid(column=1,row=17,sticky=E)
        Label(eval_frame, textvariable=self.white.halve_hek,anchor=E,bg="#fff").grid(column=1,row=18,sticky=E)
        Label(eval_frame, textvariable=self.white.active_15,anchor=E,bg="#fff").grid(column=1,row=19,sticky=E)
        Label(eval_frame, textvariable=self.white.slechte_binding,anchor=E,bg="#fff").grid(column=1,row=20,sticky=E)
        Label(eval_frame, textvariable=self.white.free_path,anchor=E,bg="#fff").grid(column=1,row=21,sticky=E)
        Label(eval_frame, textvariable=self.white.edge_35,anchor=E,bg="#fff").grid(column=1,row=22,sticky=E)
        Label(eval_frame, textvariable=self.white.edge_36,anchor=E,bg="#fff").grid(column=1,row=23,sticky=E)
        Label(eval_frame, textvariable=self.white.t11_16_17,anchor=E,bg="#fff").grid(column=1,row=24,sticky=E)
        Label(eval_frame, textvariable=self.white.voorpost,anchor=E,bg="#fff").grid(column=1,row=25,sticky=E)
        Label(eval_frame, textvariable=self.white.locked,anchor=E,bg="#fff").grid(column=1,row=26,sticky=E)
        Label(eval_frame, textvariable=self.white.vleugel_opsluiting,anchor=E,bg="#fff").grid(column=1,row=27,sticky=E)
        Label(eval_frame, textvariable=self.white.tandem,anchor=E,bg="#fff").grid(column=1,row=28,sticky=E)
        Label(eval_frame, textvariable=self.white.canon,anchor=E,bg="#fff").grid(column=1,row=29,sticky=E)
        Label(eval_frame, textvariable=self.white.endgame,anchor=E,bg="#fff").grid(column=1,row=30,sticky=E)

        Label(eval_frame, textvariable=self.black.man_value,anchor=E,bg="#eee").grid(column=2,row=1,sticky=E)
        Label(eval_frame, textvariable=self.black.king_value,anchor=E,bg="#eee").grid(column=2,row=2,sticky=E)
        Label(eval_frame, textvariable=self.black.man_position,anchor=E,bg="#eee").grid(column=2,row=3,sticky=E)
        Label(eval_frame, textvariable=self.black.king_position,anchor=E,bg="#eee").grid(column=2,row=4,sticky=E)
        Label(eval_frame, textvariable=self.black.tempi_score,anchor=E,bg="#eee").grid(column=2,row=5,sticky=E)
        Label(eval_frame, textvariable=self.black.fit_score ,anchor=E,bg="#eee").grid(column=2,row=6,sticky=E)
        Label(eval_frame, textvariable=self.black.row_score,anchor=E,bg="#eee").grid(column=2,row=7,sticky=E)
        Label(eval_frame, textvariable=self.black.freedom,anchor=E,bg="#eee").grid(column=2,row=8,sticky=E)
        Label(eval_frame, textvariable=self.black.maze_penalty,anchor=E,bg="#eee").grid(column=2,row=9,sticky=E)
        Label(eval_frame, textvariable=self.black.man_locked,anchor=E,bg="#eee").grid(column=2,row=10,sticky=E)
        Label(eval_frame, textvariable=self.black.avoid_4641,anchor=E,bg="#eee").grid(column=2,row=11,sticky=E)
        Label(eval_frame, textvariable=self.black.avoid_2324,anchor=E,bg="#eee").grid(column=2,row=12,sticky=E)
        Label(eval_frame, textvariable=self.black.avoid_2335,anchor=E,bg="#eee").grid(column=2,row=13,sticky=E)
        Label(eval_frame, textvariable=self.black.leg_2_8_13,anchor=E,bg="#eee").grid(column=2,row=14,sticky=E)
        Label(eval_frame, textvariable=self.black.tri_253035,anchor=E,bg="#eee").grid(column=2,row=15,sticky=E)
        Label(eval_frame, textvariable=self.black.klassiek,anchor=E,bg="#eee").grid(column=2,row=16,sticky=E)
        Label(eval_frame, textvariable=self.black.ketting_stelling,anchor=E,bg="#eee").grid(column=2,row=17,sticky=E)
        Label(eval_frame, textvariable=self.black.halve_hek,anchor=E,bg="#eee").grid(column=2,row=18,sticky=E)
        Label(eval_frame, textvariable=self.black.active_15,anchor=E,bg="#eee").grid(column=2,row=19,sticky=E)
        Label(eval_frame, textvariable=self.black.slechte_binding,anchor=E,bg="#eee").grid(column=2,row=20,sticky=E)
        Label(eval_frame, textvariable=self.black.free_path,anchor=E,bg="#eee").grid(column=2,row=21,sticky=E)
        Label(eval_frame, textvariable=self.black.edge_35,anchor=E,bg="#eee").grid(column=2,row=22,sticky=E)
        Label(eval_frame, textvariable=self.black.edge_36,anchor=E,bg="#eee").grid(column=2,row=23,sticky=E)
        Label(eval_frame, textvariable=self.black.t11_16_17,anchor=E,bg="#eee").grid(column=2,row=24,sticky=E)
        Label(eval_frame, textvariable=self.black.voorpost,anchor=E,bg="#eee").grid(column=2,row=25,sticky=E)
        Label(eval_frame, textvariable=self.black.locked,anchor=E,bg="#eee").grid(column=2,row=26,sticky=E)
        Label(eval_frame, textvariable=self.black.vleugel_opsluiting,anchor=E,bg="#eee").grid(column=2,row=27,sticky=E)
        Label(eval_frame, textvariable=self.black.tandem,anchor=E,bg="#eee").grid(column=2,row=28,sticky=E)
        Label(eval_frame, textvariable=self.black.canon,anchor=E,bg="#eee").grid(column=2,row=29,sticky=E)
        Label(eval_frame, textvariable=self.black.endgame,anchor=E,bg="#eee").grid(column=2,row=30,sticky=E)

        Label(eval_frame, textvariable=self.diff.man_value,anchor=E,bg="#fff").grid(column=3,row=1,sticky=E)
        Label(eval_frame, textvariable=self.diff.king_value,anchor=E,bg="#fff").grid(column=3,row=2,sticky=E)
        Label(eval_frame, textvariable=self.diff.man_position,anchor=E,bg="#fff").grid(column=3,row=3,sticky=E)
        Label(eval_frame, textvariable=self.diff.king_position,anchor=E,bg="#fff").grid(column=3,row=4,sticky=E)
        Label(eval_frame, textvariable=self.diff.tempi_score,anchor=E,bg="#fff").grid(column=3,row=5,sticky=E)
        Label(eval_frame, textvariable=self.diff.fit_score ,anchor=E,bg="#fff").grid(column=3,row=6,sticky=E)
        Label(eval_frame, textvariable=self.diff.row_score,anchor=E,bg="#fff").grid(column=3,row=7,sticky=E)
        Label(eval_frame, textvariable=self.diff.freedom,anchor=E,bg="#fff").grid(column=3,row=8,sticky=E)
        Label(eval_frame, textvariable=self.diff.maze_penalty,anchor=E,bg="#fff").grid(column=3,row=9,sticky=E)
        Label(eval_frame, textvariable=self.diff.man_locked,anchor=E,bg="#fff").grid(column=3,row=10,sticky=E)
        Label(eval_frame, textvariable=self.diff.avoid_4641,anchor=E,bg="#fff").grid(column=3,row=11,sticky=E)
        Label(eval_frame, textvariable=self.diff.avoid_2324,anchor=E,bg="#fff").grid(column=3,row=12,sticky=E)
        Label(eval_frame, textvariable=self.diff.avoid_2335,anchor=E,bg="#fff").grid(column=3,row=13,sticky=E)
        Label(eval_frame, textvariable=self.diff.leg_2_8_13,anchor=E,bg="#fff").grid(column=3,row=14,sticky=E)
        Label(eval_frame, textvariable=self.diff.tri_253035,anchor=E,bg="#fff").grid(column=3,row=15,sticky=E)
        Label(eval_frame, textvariable=self.diff.klassiek,anchor=E,bg="#fff").grid(column=3,row=16,sticky=E)
        Label(eval_frame, textvariable=self.diff.ketting_stelling,anchor=E,bg="#fff").grid(column=3,row=17,sticky=E)
        Label(eval_frame, textvariable=self.diff.halve_hek,anchor=E,bg="#fff").grid(column=3,row=18,sticky=E)
        Label(eval_frame, textvariable=self.diff.active_15,anchor=E,bg="#fff").grid(column=3,row=19,sticky=E)
        Label(eval_frame, textvariable=self.diff.slechte_binding,anchor=E,bg="#fff").grid(column=3,row=20,sticky=E)
        Label(eval_frame, textvariable=self.diff.free_path,anchor=E,bg="#fff").grid(column=3,row=21,sticky=E)
        Label(eval_frame, textvariable=self.diff.edge_35,anchor=E,bg="#fff").grid(column=3,row=22,sticky=E)
        Label(eval_frame, textvariable=self.diff.edge_36,anchor=E,bg="#fff").grid(column=3,row=23,sticky=E)
        Label(eval_frame, textvariable=self.diff.t11_16_17,anchor=E,bg="#fff").grid(column=3,row=24,sticky=E)
        Label(eval_frame, textvariable=self.diff.voorpost,anchor=E,bg="#fff").grid(column=3,row=25,sticky=E)
        Label(eval_frame, textvariable=self.diff.locked,anchor=E,bg="#fff").grid(column=3,row=26,sticky=E)
        Label(eval_frame, textvariable=self.diff.vleugel_opsluiting,anchor=E,bg="#fff").grid(column=3,row=27,sticky=E)
        Label(eval_frame, textvariable=self.diff.tandem,anchor=E,bg="#fff").grid(column=3,row=28,sticky=E)
        Label(eval_frame, textvariable=self.diff.canon,anchor=E,bg="#fff").grid(column=3,row=29,sticky=E)
        Label(eval_frame, textvariable=self.diff.endgame,anchor=E,bg="#fff").grid(column=3,row=30,sticky=E)
        Label(eval_frame, textvariable=self.diff.score,anchor=E,bg="#fff").grid(column=3,row=31,sticky=E)
        
        return
        
    def display(self, eval):
        self.white.man_value.set(self.scrap_zero(eval[1:6]))
        self.white.king_value.set(self.scrap_zero(eval[6:11]))
        self.white.man_position.set(self.scrap_zero(eval[11:16]))
        self.white.king_position.set(self.scrap_zero(eval[16:21]))
        self.white.tempi_score.set(self.scrap_zero(eval[21:26]))
        self.white.fit_score .set(self.scrap_zero(eval[26:31]))
        self.white.row_score.set(self.scrap_zero(eval[31:36]))
        self.white.freedom.set(self.scrap_zero(eval[36:41]))
        self.white.maze_penalty.set(self.scrap_zero(eval[41:46]))
        self.white.man_locked.set(self.scrap_zero(eval[46:51]))
        self.white.avoid_4641.set(self.scrap_zero(eval[51:56]))
        self.white.avoid_2324.set(self.scrap_zero(eval[56:61]))
        self.white.avoid_2335.set(self.scrap_zero(eval[61:66]))
        self.white.leg_2_8_13.set(self.scrap_zero(eval[66:71]))
        self.white.tri_253035.set(self.scrap_zero(eval[71:76]))
        self.white.klassiek.set(self.scrap_zero(eval[76:81]))
        self.white.ketting_stelling.set(self.scrap_zero(eval[81:86]))
        self.white.halve_hek.set(self.scrap_zero(eval[86:91]))
        self.white.active_15.set(self.scrap_zero(eval[91:96]))
        self.white.slechte_binding.set(self.scrap_zero(eval[96:101]))
        self.white.free_path.set(self.scrap_zero(eval[101:106]))
        self.white.edge_35.set(self.scrap_zero(eval[106:111]))
        self.white.edge_36.set(self.scrap_zero(eval[111:116]))
        self.white.t11_16_17.set(self.scrap_zero(eval[116:121]))
        self.white.voorpost.set(self.scrap_zero(eval[121:126]))
        self.white.locked.set(self.scrap_zero(eval[126:131]))
        self.white.vleugel_opsluiting.set(self.scrap_zero(eval[131:136]))
        self.white.tandem.set(self.scrap_zero(eval[136:141]))
        self.white.canon.set(self.scrap_zero(eval[141:146]))
        self.white.endgame.set(self.scrap_zero(eval[146:151]))

        self.black.man_value.set(self.scrap_zero(eval[151:156]))
        self.black.king_value.set(self.scrap_zero(eval[156:161]))
        self.black.man_position.set(self.scrap_zero(eval[161:166]))
        self.black.king_position.set(self.scrap_zero(eval[166:171]))
        self.black.tempi_score.set(self.scrap_zero(eval[171:176]))
        self.black.fit_score .set(self.scrap_zero(eval[176:181]))
        self.black.row_score.set(self.scrap_zero(eval[181:186]))
        self.black.freedom.set(self.scrap_zero(eval[186:191]))
        self.black.maze_penalty.set(self.scrap_zero(eval[191:196]))
        self.black.man_locked.set(self.scrap_zero(eval[196:201]))
        self.black.avoid_4641.set(self.scrap_zero(eval[201:206]))
        self.black.avoid_2324.set(self.scrap_zero(eval[206:211]))
        self.black.avoid_2335.set(self.scrap_zero(eval[211:216]))
        self.black.leg_2_8_13.set(self.scrap_zero(eval[216:221]))
        self.black.tri_253035.set(self.scrap_zero(eval[221:226]))
        self.black.klassiek.set(self.scrap_zero(eval[226:231]))
        self.black.ketting_stelling.set(self.scrap_zero(eval[231:236]))
        self.black.halve_hek.set(self.scrap_zero(eval[236:241]))
        self.black.active_15.set(self.scrap_zero(eval[241:246]))
        self.black.slechte_binding.set(self.scrap_zero(eval[246:251]))
        self.black.free_path.set(self.scrap_zero(eval[251:256]))
        self.black.edge_35.set(self.scrap_zero(eval[256:261]))
        self.black.edge_36.set(self.scrap_zero(eval[261:266]))
        self.black.t11_16_17.set(self.scrap_zero(eval[266:271]))
        self.black.voorpost.set(self.scrap_zero(eval[271:276]))
        self.black.locked.set(self.scrap_zero(eval[276:281]))
        self.black.vleugel_opsluiting.set(self.scrap_zero(eval[281:286]))
        self.black.tandem.set(self.scrap_zero(eval[286:291]))
        self.black.canon.set(self.scrap_zero(eval[291:296]))
        self.black.endgame.set(self.scrap_zero(eval[296:301]))
        self.diff.score.set(eval[301:307])

        self.set_diff(self.white.man_value,self.black.man_value,self.diff.man_value)
        self.set_diff(self.white.king_value,self.black.king_value,self.diff.king_value)
        self.set_diff(self.white.man_position,self.black.man_position,self.diff.man_position)
        self.set_diff(self.white.king_position,self.black.king_position,self.diff.king_position)
        self.set_diff(self.white.tempi_score,self.black.tempi_score,self.diff.tempi_score)
        self.set_diff(self.white.fit_score ,self.black.fit_score ,self.diff.fit_score )
        self.set_diff(self.white.row_score,self.black.row_score,self.diff.row_score)
        self.set_diff(self.white.freedom,self.black.freedom,self.diff.freedom)
        self.set_diff(self.white.maze_penalty,self.black.maze_penalty,self.diff.maze_penalty)
        self.set_diff(self.white.man_locked,self.black.man_locked,self.diff.man_locked)
        self.set_diff(self.white.avoid_4641,self.black.avoid_4641,self.diff.avoid_4641)
        self.set_diff(self.white.avoid_2324,self.black.avoid_2324,self.diff.avoid_2324)
        self.set_diff(self.white.avoid_2335,self.black.avoid_2335,self.diff.avoid_2335)
        self.set_diff(self.white.leg_2_8_13,self.black.leg_2_8_13,self.diff.leg_2_8_13)
        self.set_diff(self.white.tri_253035,self.black.tri_253035,self.diff.tri_253035)
        self.set_diff(self.white.klassiek,self.black.klassiek,self.diff.klassiek)
        self.set_diff(self.white.ketting_stelling,self.black.ketting_stelling,self.diff.ketting_stelling)
        self.set_diff(self.white.halve_hek,self.black.halve_hek,self.diff.halve_hek)
        self.set_diff(self.white.active_15,self.black.active_15,self.diff.active_15)
        self.set_diff(self.white.slechte_binding,self.black.slechte_binding,self.diff.slechte_binding)
        self.set_diff(self.white.free_path,self.black.free_path,self.diff.free_path)
        self.set_diff(self.white.edge_35,self.black.edge_35,self.diff.edge_35)
        self.set_diff(self.white.edge_36,self.black.edge_36,self.diff.edge_36)
        self.set_diff(self.white.t11_16_17,self.black.t11_16_17,self.diff.t11_16_17)
        self.set_diff(self.white.voorpost,self.black.voorpost,self.diff.voorpost)
        self.set_diff(self.white.locked,self.black.locked,self.diff.locked)
        self.set_diff(self.white.vleugel_opsluiting,self.black.vleugel_opsluiting,self.diff.vleugel_opsluiting)
        self.set_diff(self.white.tandem,self.black.tandem,self.diff.tandem)
        self.set_diff(self.white.canon,self.black.canon,self.diff.canon)
        self.set_diff(self.white.endgame,self.black.endgame,self.diff.endgame)

        return

    def set_diff(self, w_param, b_param, d_param):
        w = w_param.get()
        b = b_param.get()
        if w=='     ': w = '    0'
        if b=='     ': b  = '    0'
        d = str(int(w) - int(b)).rjust(5)
        if d == '    0': d = '     '
        d_param.set(d)
        return
        
    def scrap_zero(self, param):
        if param == '    0': return '     '
        return param
    
        
        
