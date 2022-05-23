from graphics import *
from time import *

def main ():
    win = GraphWin("mf_folio", 686,900)

    #Colors set 1
    Red    = color_rgb(255,0,0)
    Blue   = color_rgb(51,103,153)
    Black  = color_rgb(0,0,0)
    Skin   = color_rgb(246,208,185)
    White  = color_rgb(255,255,255)
    Gold   = color_rgb(241,196,15)

    #color Set 2
    Backclr = color_rgb(165,137,87)
    Fblue   = color_rgb(119,136,144)
    FFblue  = color_rgb(143,161,171)
    Fgreen  = color_rgb(141,157,92)
    Fmud    = color_rgb(121,103,91)
    FDMud   = color_rgb(69,43,26)
    MoniC   = color_rgb(93,62,34)
    Mskin   = color_rgb(252,198,162)

    #BACKGROUND
    rect1 = Rectangle(Point(0,0),Point(686,900))
    rect1.setFill(Black)

    #BODY

    X1 = Point(321,316)
    X1.draw(win)
    X2 = Point(304,329)
    X2.draw(win)
    X3 = Point(324,489)
    X3.draw(win)
    X4 = Point(334,490)
    X4.draw(win)
    X5 = Point(352,486)
    X5.draw(win)
    X6 = Point(355,478)
    X6.draw(win)
    X7 = Point(367,480)
    X7.draw(win)
    X8 = Point(382,480)
    X8.draw(win)
    X9 = Point(396,476)
    X9.draw(win)
    X10 = Point(399,488)
    X10.draw(win)
    X11 = Point(422,490)
    X11.draw(win)
    X12 = Point(446,486)
    X12.draw(win)
    X13 = Point(462,477)
    X13.draw(win)
    X14 = Point(454,450)
    X14.draw(win)
    X15 = Point(445,431)
    X15.draw(win)
    X16 = Point(448,418)
    X16.draw(win)
    X17 = Point(448,399)
    X17.draw(win)
    X18 = Point(431,352)
    X18.draw(win)
    X19 = Point(430,333)
    X19.draw(win)
    X20 = Point(424,316)
    X20.draw(win)

    BodyB = Polygon(X1,X2,X3,X4,X5,X6,X7,X8,X9,X10,X11,X12,X13,X14,X15,X16,X17,X18,X19,X20)
    BodyB.setFill(Blue)

    # FACEEEE

        #EARS
            #EAR1
    ptEarCircleC = Point(246,190)
    EarCL = Circle(ptEarCircleC, 30)
        
    ptEarCircleC1 = Point(246,190)
    EarCL1 = Circle(ptEarCircleC1, 28)
    EarCL1.setFill(Blue)
    
            #EAR2
    ptEar1CircleC = Point(510,190)
    Ear1CL1 = Circle(ptEar1CircleC, 30)
    Ear1CL1.setFill(Black)

    ptEar1CircleC1 = Point(510,190)
    Ear1CL1 = Circle(ptEar1CircleC1, 28)
    Ear1CL1.setFill(Blue)
    
     #FaceOutline
    ptfaceCircleC = Point(378,180)
    FaceCL = Circle(ptfaceCircleC,139)
    FaceCL.setFill(Black)
            
    ptfaceCircleC1 = Point(378,180)
    FaceCL1 = Circle(ptfaceCircleC1,134)
    FaceCL1.setFill(Blue)

    #SHIELD
    ptShieldC = Point(203,424)
    Shield = Circle(ptShieldC,142)
    Shield.setFill(Black)

    ptShieldC1 = Point(203,424)
    Shield1 = Circle(ptShieldC1,137)
    Shield1.setFill(Red)
    
    Shield2 = Circle(ptShieldC,112)
    Shield2.setFill(White)
    

    Shield3 = Circle(ptShieldC,97)
    Shield3.setFill(Red)
    

    Shield4 = Circle(ptShieldC,81)
    Shield4.setFill(Blue)

    
        #EYEB1

    p1 = Point(396,174)
    p1.draw(win)
    p2 = Point(446,144)
    p2.draw(win)
    p3 = Point(455,145)
    p3.draw(win)
    p4 = Point(466,180)
    p4.draw(win)
    p5 = Point(458,204)
    p5.draw(win)
    p6 = Point(436,209)
    p6.draw(win)
    p7 = Point(412,198)
    p7.draw(win)

    EyeB1 = Polygon(p1,p2,p3,p4,p5,p6,p7)
    EyeB1.setFill(Skin)
    

        #EYEB2
    T1 = Point(358,171)
    T1.draw(win)
    T2 = Point(339,198)
    T2.draw(win)
    T3 = Point(313,209)
    T3.draw(win)
    T4 = Point(288,205)
    T4.draw(win)
    T5 = Point(279,180)
    T5.draw(win)
    T6 = Point(292,147)
    T6.draw(win)
    T7 = Point(302,144)
    T7.draw(win)

    EyeB2 = Polygon(T1,T2,T3,T4,T5,T6,T7)
    EyeB2.setFill(Skin)
    

        #EYES
            #EYE1
    ptEyeCircleC = Point(310,177)
    EyeCL = Circle(ptEyeCircleC,22)
    EyeCL.setFill(Black)
    

    ptEye1CircleC = Point(310,174)
    Eye1CL = Circle(ptEye1CircleC,6)
    Eye1CL.setFill(White)
    

            #EYE2
    ptEyeCircleC1 = Point(435,177)
    EyeCL1 = Circle(ptEyeCircleC1,22)
    EyeCL1.setFill(Black)
    

    ptEye1CircleC1 = Point(435,174)
    Eye1CL1 = Circle(ptEye1CircleC1,6)
    Eye1CL1.setFill(White)
    

    #A ON HEAD
        #Part1
    A1 = Point(337,141)
    A1.draw(win)
    A2 = Point(357,69)
    A2.draw(win)
    A3 = Point(391,69)
    A3.draw(win)
    A4 = Point(412,138)
    A4.draw(win)
    A5 = Point(383,139)
    A5.draw(win)
    A6 = Point(378,126)
    A6.draw(win)
    A7 = Point(366,126)
    A7.draw(win)
    A8 = Point(360,142)
    A8.draw(win)

    LetterA = Polygon(A1,A2,A3,A4,A5,A6,A7,A8)
    LetterA.setFill(White)
    
        #Part2
    AA1 = Point(374,90)
    AA1.draw(win)
    AA2 = Point(378,108)
    AA2.draw(win)
    AA3 = Point(368,108)
    AA3.draw(win)

    TriA = Polygon(AA1,AA2,AA3)
    TriA.setFill(Blue)
    

    #Mouth
        #Mouth Skin

    M1 = Point(374,207) 
    M1.draw(win)
    M2 = Point(450,234)
    M2.draw(win)
    M3 = Point(462,274)
    M3.draw(win)
    M4 = Point(427,299)
    M4.draw(win)
    M5 = Point(388,309)
    M5.draw(win)
    M6 = Point(349,306)
    M6.draw(win)
    M7 = Point(328,301)
    M7.draw(win)
    M8 = Point(281,270)
    M8.draw(win)
    M9 = Point(288,240)
    M9.draw(win)

    MSkin = Polygon(M1,M2,M3,M4,M5,M6,M7,M8,M9)
    MSkin.setFill(Skin)
    

        #Mouth
    B1 = Point(342,259)
    B1.draw(win)
    B2 = Point(367,279)
    B2.draw(win)
    B3 = Point(381,278)
    B3.draw(win)
    B4 = Point(403,252)
    B4.draw(win)
    B5 = Point(388,260)
    B5.draw(win)

    MBlack = Polygon(B1,B2,B3,B4,B5)
    MBlack.setFill(Black)
    
          
        #Star
    S1 = Point(198,357)
    S1.draw(win)
    S2 = Point(180,396)
    S2.draw(win)
    S3 = Point(131,406)
    S3.draw(win)
    S4 = Point(167,439)
    S4.draw(win)
    S5 = Point(158,486)
    S5.draw(win)
    S6 = Point(201,462)
    S6.draw(win)
    S7 = Point(244,486)
    S7.draw(win)
    S8 = Point(234,439)
    S8.draw(win)
    S9 = Point(269,406)
    S9.draw(win)
    S10 = Point(220,399)
    S10.draw(win)

    SStar = Polygon(S1,S2,S3,S4,S5,S6,S7,S8,S9,S10)
    SStar.setFill(White)

    #Shirt Strips

        # First Strip
    S11 = Point(337,358)
    S11.draw(win)
    S12 = Point(333,365)
    S12.draw(win)
    S13 = Point(344,404)
    S13.draw(win)
    S14 = Point(351,364)
    S14.draw(win)

    Strip1 = Polygon(S11,S12,S13,S14)
    Strip1.setFill(Red)
    

        # Second Strip
    S21 = Point(353,363)
    S21.draw(win)
    S22 = Point(345,414)
    S22.draw(win)
    S23 = Point(359,416)
    S23.draw(win)
    S24 = Point(364,365)
    S24.draw(win)

    Strip2 = Polygon(S21,S22,S23,S24)
    Strip2.setFill(White)

        # Third Strip
    S31 = Point(366,365)
    S31.draw(win)
    S32 = Point(362,417)
    S32.draw(win)
    S33 = Point(392,414)
    S33.draw(win)
    S34 = Point(384,366)
    S34.draw(win)

    Strip3 = Polygon(S31,S32,S33,S34)
    Strip3.setFill(Red)
    

        #forth Strip
    S41 = Point(386,365)
    S41.draw(win)
    S42 = Point(394,414)
    S42.draw(win)
    S43 = Point(406,413)
    S43.draw(win)
    S44 = Point(399,364)
    S44.draw(win)

    Strip4 = Polygon(S41,S42,S43,S44)
    Strip4.setFill(White)

        #Fifth Strip
    S51 = Point(401,363)
    S51.draw(win)
    S52 = Point(408,411)
    S52.draw(win)
    S53 = Point(431,403)
    S53.draw(win)
    S54 = Point(416,360)
    S54.draw(win)

    Strip5 = Polygon(S51,S52,S53,S54)
    Strip5.setFill(Red)

        # Sixth Strip
    S61 = Point(417,359)
    S61.draw(win)
    S62 = Point(435,402)
    S62.draw(win)
    S63 = Point(443,395)
    S63.draw(win)
    S64 = Point(426,357)
    S64.draw(win)

    Strip6 = Polygon(S61,S62,S63,S64)
    Strip6.setFill(White)

    #ARM

    H1 = Point(430,315)
    H1.draw(win)
    H2 = Point(432,324)
    H2.draw(win)
    H3 = Point(434,348)
    H3.draw(win)
    H4 = Point(464,369)
    H4.draw(win)
    H5 = Point(488,371)
    H5.draw(win)
    H6 = Point(452,375)
    H6.draw(win)
    H7 = Point(448,378)
    H7.draw(win)
    H8 = Point(451,391)
    H8.draw(win)
    H9 = Point(453,405)
    H9.draw(win)
    H10 = Point(453,418)
    H10.draw(win)
    H11 = Point(450,427)
    H11.draw(win)
    H12 = Point(457,438)
    H12.draw(win)
    H13 = Point (468,432)
    H13.draw(win)
    H14 = Point(486,418)
    H14.draw(win)
    H15 = Point(504,396)
    H15.draw(win)
    H16 = Point(514,377)
    H16.draw(win)
    H17 = Point(510,368)
    H17.draw(win)
    H18 = Point(492,349)
    H18.draw(win)
    H19 = Point(457,326)
    H19.draw(win)

    Arm1 = Polygon(H1,H2,H3,H4,H5,H6,H7,H8,H9,H10,H11,H12,H13,H14,H15,H16,H17,H18,H19)
    Arm1.setFill(Blue)

    #Boots
        #Boot1 TOP
    BT1 = Point(321,495)
    BT1.draw(win)
    BT2 = Point(304,516)
    BT2.draw(win)
    BT3 = Point(314,518)
    BT3.draw(win)
    BT4 = Point(332,519)
    BT4.draw(win)
    BT5 = Point(350,516)
    BT5.draw(win)
    BT6 = Point(353,515)
    BT6.draw(win)
    BT7 = Point(355,511)
    BT7.draw(win)
    BT8 = Point(355,491)
    BT8.draw(win)

    Boot1Top = Polygon(BT1,BT2,BT3,BT4,BT4,BT5,BT6,BT7,BT8)
    Boot1Top.setFill(Red)
    
        #Boot1 BOT

    BY1 = Point(301,520)
    BY1.draw(win)
    BY2 = Point(283,537)
    BY2.draw(win)
    BY3 = Point(292,550)
    BY3.draw(win)
    BY4 = Point(306,555)
    BY4.draw(win)
    BY5 = Point(328,556)
    BY5.draw(win)
    BY6 = Point(342,555)
    BY6.draw(win)
    BY7 = Point(351,549)
    BY7.draw(win)
    BY8 = Point(354,539)
    BY8.draw(win)
    BY9 = Point(351,521)
    BY9.draw(win)
    BY10 = Point(332,523)
    BY10.draw(win)
    BY11 = Point(310,522)
    BY11.draw(win)
    BY12 = Point(301,519)
    BY12.draw(win)

    Boot1Bot = Polygon(BY1,BY2,BY3,BY4,BY5,BY6,BY7,BY8,BY9,BY10,BY11,BY12)
    Boot1Bot.setFill(Red)
    

        #Boot2 Top

    CT1 = Point(468,482)
    CT1.draw(win)
    CT2 = Point(471,488)
    CT2.draw(win)
    CT3 = Point(471,506)
    CT3.draw(win)
    CT5 = Point(452,515)
    CT5.draw(win)
    CT6 = Point(471,504)
    CT6.draw(win)
    CT7 = Point(452,515)
    CT7.draw(win)
    CT8 = Point(427,519)
    CT8.draw(win)
    CT9 = Point(401,516)
    CT9.draw(win)
    CT10 = Point(393,511)
    CT10.draw(win)
    CT11 = Point(396,492)
    CT11.draw(win)
    CT12 = Point(446,491)
    CT12.draw(win)
    CT13 = Point(461,483)
    CT13.draw(win)

    Boot2Top = Polygon(CT1,CT2,CT3,CT5,CT6,CT7,CT8,CT8,CT9,CT10,CT11,CT12,CT13)
    Boot2Top.setFill(Red)

        #Boot2 Bot

    CY1 = Point(398,522)
    CY1.draw(win)
    CY2 = Point(396,546)
    CY2.draw(win)
    CY3 = Point(403,554)
    CY3.draw(win)
    CY4 = Point(418,557)
    CY4.draw(win)
    CY5 = Point(444,556)
    CY5.draw(win)
    CY6 = Point(456,551)
    CY6.draw(win)
    CY7 = Point(466,544)
    CY7.draw(win)
    CY8 = Point(467,515)
    CY8.draw(win)
    CY9 = Point(460,515)
    CY9.draw(win)
    CY10 = Point(438,522)
    CY10.draw(win)
    CY11 = Point(414,522)
    CY11.draw(win)

    Boot2Bot = Polygon( CY1,CY2,CY3,CY4,CY5,CY6,CY7,CY8,CY9,CY10,CY11)
    Boot2Bot.setFill(Red)
    

    #Belt
        #Belt1
    BL1 = Point(344,423)
    BL1.draw(win)
    BL2 = Point(342,443)
    BL2.draw(win)
    BL3 = Point(349,445)
    BL3.draw(win)
    BL4 = Point(349,422)
    BL4.draw(win)

    Belt1 = Polygon(BL1,BL2,BL3,BL4)
    Belt1.setFill(Black)

        #Belt2

    BK1 = Point(352,419)
    BK1.draw(win)
    BK2 = Point(352,452)
    BK2.draw(win)
    BK3 = Point(393,452)
    BK3.draw(win)
    BK4 = Point(393,419)
    BK4.draw(win)

    Belt2 = Polygon(BK1,BK2,BK3,BK4)
    Belt2.setFill(Gold)
    

        #Belt3

    BJ1 = Point(396,423)
    BJ1.draw(win)
    BJ2 = Point(396,445)
    BJ2.draw(win)
    BJ3 = Point(411,442)
    BJ3.draw(win)
    BJ4 = Point(411,418)
    BJ4.draw(win)


    Belt3 = Polygon(BJ1,BJ2,BJ3,BJ4)
    Belt3.setFill(Black)


        #Belt4

    BH1 = Point(422,416)
    BH1.draw(win)
    BH2 = Point(424,438)
    BH2.draw(win)
    BH3 = Point(441,429) 
    BH3.draw(win)
    BH4 = Point(443,406)
    BH4.draw(win)

    Belt4 = Polygon(BH1,BH2,BH3,BH4)
    Belt4.setFill(Black)
                
        #Belt Fix

    BF1 = Point(360,425)
    BF1.draw(win)
    BF2 = Point(359,446)
    BF2.draw(win)
    BF3 = Point(374,446)
    BF3.draw(win)
    BF4 = Point(374,425)
    BF4.draw(win)

    BLTFX = Polygon(BF1,BF2,BF3,BF4)
    BLTFX.setFill(Blue)
    

    BFF1 = Point(378,425)
    BFF1.draw(win)
    BFF2 = Point(385,425)
    BFF2.draw(win)
    BFF3 = Point(385,446)
    BFF3.draw(win)
    BFF4 = Point(378,446)
    BFF4.draw(win)

    BLTFX1 = Polygon(BFF1,BFF2,BFF3,BFF4)
    BLTFX1.setFill(Blue)

################################################################################################################################################################################
#Transition

    
    rect3 = Rectangle(Point(0,0),Point(686,900))
    rect3.setFill(Black)

    #Letter T
    T1 = Point(250,205)
    T1.draw(win)
    T2 = Point(249,238)
    T2.draw(win)
    T3 = Point(272,237)
    T3.draw(win)
    T4 = Point(272,344)
    T4.draw(win)
    T5 = Point(304,344)
    T5.draw(win)
    T6 = Point(304,237)
    T6.draw(win)
    T7 = Point(325,238)
    T7.draw(win)
    T8 = Point(326,205)
    T8.draw(win)

    LetterT = Polygon(T1,T2,T3,T4,T5,T6,T7,T8)
    LetterT.setFill(White)
    
    #Letter O

    O1 = Point(329,238)
    O1.draw(win)
    O2 = Point(329,344)
    O2.draw(win)
    O3 = Point(436,344)
    O3.draw(win)
    O4 = Point(436,237)
    O4.draw(win)

    LetterO1 = Polygon(O1,O2,O3,O4)
    LetterO1.setFill(White)


    O5 = Point(356,265)
    O5.draw(win)
    O6 = Point(356,317)
    O6.draw(win)
    O7 = Point(409,317)
    O7.draw(win)
    O8 = Point(409,264)
    O8.draw(win)

    LetterO2 = Polygon(O5,O6,O7,O8)
    LetterO2.setFill(Black)
########
    
    LetterO11 = Polygon(O1,O2,O3,O4)
    LetterO11.setFill(White)
    LetterO11.move(120,0)
    LetterO22 = Polygon(O5,O6,O7,O8)
    LetterO22.setFill(Black)
    LetterO22.move(120,0)

    #Letter  E
    E1 = Point(112,402)
    E1.draw(win)
    E2 = Point(113,505)
    E2.draw(win)
    E3 = Point(161,504)
    E3.draw(win)
    E4 = Point(161,482)
    E4.draw(win)
    E5 = Point(137,482)
    E5.draw(win)
    E55 = Point(137,465)
    E55.draw(win)
    E6 = Point(158,464)
    E6.draw(win)
    E7 = Point(158,442)
    E7.draw(win)
    E8 = Point(137,442)
    E8.draw(win)
    E9 = Point(137,424)
    E9.draw(win)
    E10 = Point(160,424)
    E10.draw(win)
    E11 = Point(161,402)
    E11.draw(win)

    LetterE = Polygon (E1,E2,E3,E4,E5,E55,E6,E7,E8,E9,E10,E11)
    LetterE.setFill(White)

    #AAA1 = Point(169,505)
    #AAA1.draw(win)
    #AAA2 = Point(197,402)
    #AAA2.draw(win)
    #AAA3 = Point(223,402)
    #AAA3.draw(win)
    #AAA4 = Point(249,504)
    #AAA4.draw(win)
    #AAA5 = Point(225,504)
    #AAA5.draw(win)
    #AAA6 = Point(222,490)
    #AAA6.draw(win)
    #AAA7 = Point(197,490)
    #AAA7.draw(win)
    #AAA8 = Point(193,504)
    #AAA8.draw(win)
    
    
    #LetterAA = Polygon(AAA1,AAA2,AAA3,AAA4,AAA5,AAA6,AAA7,AAA8)
    #LetterAA.setFill(White)

    #AAT1 = Point(201,470)
    #AAT1.draw(win)
    #AAT2 = Point(216,470)
    #AAT2.draw(win)
    #AAT3 = Point(209,420)
    #AAT3.draw(win)

    #LetterTA = Polygon(AAT1,AAT2,AAT3)
    #LetterTA.setFill(Black)


    EZ1 = Point(174,403)
    EZ1.draw(win)
    EZ2 = Point(174,425)
    EZ2.draw(win)
    EZ3 = Point(204,425)
    EZ3.draw(win)
    EZ4 = Point(168,504)
    EZ4.draw(win)
    EZ5 = Point(237,505)
    EZ5.draw(win)
    EZ6 = Point(237,482)
    EZ6.draw(win)
    EZ7 = Point(205,482)
    EZ7.draw(win)
    EZ8 = Point(240,402)
    EZ8.draw(win)

    LetterZ = Polygon(EZ1,EZ2,EZ3,EZ4,EZ5,EZ6,EZ7,EZ8)
    LetterZ.setFill(White)



    Q1 = Point(347,397)
    Q1.draw(win)
    Q2 = Point(347,429)
    Q2.draw(win)
    Q3 = Point(419,428)
    Q3.draw(win)
    Q4 = Point(419,441)
    Q4.draw(win)
    Q5 = Point(383,441)
    Q5.draw(win)
    Q6 = Point(382,472)
    Q6.draw(win)
    Q7 = Point(444,472)
    Q7.draw(win)
    Q8 = Point(444,396)

    QuestionMark = Polygon(Q1,Q2,Q3,Q4,Q5,Q6,Q7,Q8)
    QuestionMark.setFill(White)

    QuestionMark1 = Polygon(Q1,Q2,Q3,Q4,Q5,Q6,Q7,Q8)
    QuestionMark1.setFill(White)
    QuestionMark1.move(110,0)

    
    QDot1 = Point(382,487)
    QDot1.draw(win)
    QDot2 = Point(382,517)
    QDot2.draw(win)
    QDot3 = Point(407,517)
    QDot3.draw(win)
    QDot4 = Point(407,486)
    QDot4.draw(win)

    QuestionDot = Polygon(QDot1,QDot2,QDot3,QDot4)
    QuestionDot.setFill(White)

    QuestionDot1 = Polygon(QDot1,QDot2,QDot3,QDot4)
    QuestionDot1.setFill(White)
    QuestionDot1.move(110,0)

    

    
    

    
    



#####################################################################################
    #2nd picture



        #TEXT
    

    rect2 = Rectangle(Point(0,0),Point(686,900))
    rect2.setFill(Backclr)
    

    #Frame
    FR1 = Point(75,61)
    FR1.draw(win)
    FR2 = Point(75,841)
    FR2.draw(win)
    FR3 = Point(619,841)
    FR3.draw(win)
    FR4 = Point(619,61)

    Frame = Polygon(FR1,FR2,FR3,FR4)
    Frame.setFill(FFblue)

    #Top Frame

    FRR1 = Point(619,272)
    FRR1.draw(win)
    FRR2 = Point(75,272)
    FRR2.draw(win)
    FRR3 = Point(75,61)
    FRR3.draw(win)
    FRR4 = Point(619,61)
    FRR4.draw(win)

    FrameTop = Polygon(FRR1,FRR2,FRR3,FRR4)
    FrameTop.setFill(Fblue)
    
    
    
    #Bushes

    B41 = Point(75,214)
    B41.draw(win)
    B42 = Point(94,214)
    B42.draw(win)
    B43 = Point(106,219)
    B43.draw(win)
    B44 = Point(122,225)
    B44.draw(win)
    B45 = Point(132,228)
    B45.draw(win)
    B46 = Point(142,225)
    B46.draw(win)
    B47 = Point(153,217)
    B47.draw(win)
    B48 = Point(163,215)
    B48.draw(win)
    B49 = Point(172,223)
    B49.draw(win)
    B410 = Point(186,219)
    B410.draw(win)
    B411 = Point(193,223)
    B411.draw(win)
    B412 = Point(196,229)
    B412.draw(win)
    B413 = Point(196,242)
    B413.draw(win)
    B414 = Point(199,245)
    B414.draw(win)
    B415 = Point(211,244)
    B415.draw(win)
    B416 = Point(213,255)
    B416.draw(win)
    B417 = Point(217,258)
    B417.draw(win)
    B418 = Point(225,256)
    B418.draw(win)
    B419 = Point(231,256)
    B419.draw(win)
    B420 = Point(240,269)
    B420.draw(win)        #TOP part
    B421 = Point(240,344)
    B421.draw(win)
    B422 = Point(206,350)
    B422.draw(win)
    B423 = Point(150,365)
    B423.draw(win)
    B424 = Point(114,373)
    B424.draw(win)
    B425 = Point(75,373)
    B425.draw(win)

    Bush1 = Polygon(B41,B42,B43,B44,B45,B46,B47,B48,B49,B410,B411,B412,B413,B414,B415,B416,B417,B418,B419,B420,B421,B422,B423,B424,B425)
    Bush1.setFill(Fgreen)
    
    #Bush 2

    B11 = Point(448,305)
    B11.draw(win)
    B12 = Point(456,297)
    B12.draw(win)
    B13 = Point(461,289)
    B13.draw(win)
    B14 = Point(465,280)
    B14.draw(win)
    B15 = Point(470,273)
    B15.draw(win)
    B16 = Point(472,272)
    B16.draw(win)
    B17 = Point(489,277)
    B17.draw(win)
    B18 = Point(497,284)
    B18.draw(win)
    B19 = Point(502,287)
    B19.draw(win)
    B110 = Point(522,286)
    B110.draw(win)
    B111 = Point(540,286)
    B111.draw(win)
    B112 = Point(564,284)
    B112.draw(win)
    B113 = Point(560,276)
    B113.draw(win)
    B114 = Point(555,269)
    B114.draw(win)
    B115 = Point(539,268)
    B115.draw(win)
    B116 = Point(529,269)
    B116.draw(win)
    B117 = Point(525,264)
    B117.draw(win)
    B118 = Point(529,255)
    B118.draw(win)
    B119 = Point(528,247)
    B119.draw(win)
    B120 = Point(522,242)
    B120.draw(win)
    B121 = Point(513,235)
    B121.draw(win)
    B122 = Point(510,225)
    B122.draw(win)
    B123 = Point(514,215)
    B123.draw(win)
    B124 = Point(510,208)
    B124.draw(win)
    B125 = Point(501,206)
    B125.draw(win)
    B126 = Point(486,210)
    B126.draw(win)
    B127 = Point(465,221)
    B127.draw(win)
    B128 = Point(435,219)
    B128.draw(win)
    B129 = Point(440,245)
    B129.draw(win)
    B130 = Point(446,275)
    B130.draw(win)

    Bush2 = Polygon(B11,B12,B13,B14,B15,B16,B17,B18,B19,B110,B111,B112,B113,B114,B115,B116,B117,B118,B119,B120,B121,B122,B123,B124,B125,B126,B127,B128,B129,B130)
    Bush2.setFill(Fgreen)
    
    #Bush 3

    C1 = Point(619,354)
    C1.draw(win)
    C2 = Point(600,358)
    C2.draw(win)
    C3 = Point(584,366)
    C3.draw(win)
    C4 = Point(565,365)
    C4.draw(win)
    C5 = Point(551,360)
    C5.draw(win)
    C6 = Point(525,371)
    C6.draw(win)
    C7 = Point(511,361)
    C7.draw(win)
    C8 = Point(494,358)
    C8.draw(win)
    C9 = Point(483,366)
    C9.draw(win)
    C10 = Point(498,375)
    C10.draw(win)
    C11 = Point(513,381)
    C11.draw(win)
    C12 = Point(514,386)
    C12.draw(win)
    C13 = Point(508,429)
    C13.draw(win)
    C14 = Point(613,504)
    C14.draw(win)
    C15 = Point(619,495)
    C15.draw(win)

    Bush3 = Polygon(C1,C2,C3,C4,C5,C6,C7,C8,C9,C10,C11,C12,C13,C14,C15)
    Bush3.setFill(Fgreen)
    
     #MUD

    X1 = Point(75,411)
    X1.draw(win)
    X2 = Point(109,402)
    X2.draw(win)
    X3 = Point(131,401)
    X3.draw(win)
    X4 = Point(144,393)
    X4.draw(win)
    X5 = Point(167,389)
    X5.draw(win)
    X6 = Point(150,405)
    X6.draw(win)
    X7 = Point(145,421)
    X7.draw(win)
    X8 = Point(153,435)
    X8.draw(win)
    X9 = Point(169,445)
    X9.draw(win)
    X10 = Point(177,450)
    X10.draw(win)
    X11 = Point(178,457)
    X11.draw(win)
    X12 = Point(169,467)
    X12.draw(win)
    X13 = Point(153,476)
    X13.draw(win)
    X14 = Point(130,485)
    X14.draw(win)
    X15 = Point(118,492)
    X15.draw(win)
    X16 = Point(116,504)
    X16.draw(win)
    X17 = Point(127,517)
    X17.draw(win)
    X18 = Point(136,529)
    X18.draw(win)
    X19 = Point(135,546)
    X19.draw(win)
    X20 = Point(119,571)
    X20.draw(win)
    X21 = Point(75,570)
    X21.draw(win)

    Mud1 = Polygon(X1,X2,X3,X4,X5,X6,X7,X8,X9,X10,X11,X12,X13,X14,X15,X16,X17,X18,X19,X20,X21)
    Mud1.setFill(Fmud)
    

    XX1 = Point(180,387)
    XX1.draw(win)
    XX2 = Point(168,399)
    XX2.draw(win)
    XX3 = Point(161,413)
    XX3.draw(win)
    XX4 = Point(166,425)
    XX4.draw(win)
    XX5 = Point(179,436)
    XX5.draw(win)
    XX6 = Point(188,448)
    XX6.draw(win)
    XX7 = Point(189,463)
    XX7.draw(win)
    XX8 = Point(180,470)
    XX8.draw(win)
    XX9 = Point(162,485)
    XX9.draw(win)
    XX10 = Point(157,497)
    XX10.draw(win)
    XX11 = Point(160,507)
    XX11.draw(win)
    XX12 = Point(165,517)
    XX12.draw(win)
    XX13 = Point(243,413)
    XX13.draw(win)
    XX14 = Point(251,385)
    XX14.draw(win)
    XX15 = Point(216,383)
    XX15.draw(win)

    Mud2 = Polygon(XX1,XX2,XX3,XX4,XX5,XX6,XX7,XX8,XX9,XX10,XX11,XX12,XX13,XX14,XX15)
    Mud2.setFill(Fmud)
    


        #Mud Right
    
    D1 = Point(619,494)
    D1.draw(win)
    D2 = Point(594,482)
    D2.draw(win)
    D3 = Point(563,465)
    D3.draw(win)
    D4 = Point(553,455)
    D4.draw(win)
    D5 = Point(539,454)
    D5.draw(win)
    D6 = Point(515,421)
    D6.draw(win)
    D7 = Point(516,401)
    D7.draw(win)
    D8 = Point(524,389)
    D8.draw(win)
    D9 = Point(522,384)
    D9.draw(win)
    D10 = Point(502,392)
    D10.draw(win)
    D11 = Point(484,387)
    D11.draw(win)
    D12 = Point(467,391)
    D12.draw(win)
    D13 = Point(541,565)
    D13.draw(win)
    D14 = Point(619,564)
    D14.draw(win)

    Mud3 = Polygon(D1,D2,D3,D4,D5,D6,D7,D8,D9,D10,D11,D12,D13,D14)
    Mud3.setFill(Fmud)
    
        #Flor
    YX1 = Point(75,571)
    YX1.draw(win)
    YX2 = Point(619,564)
    YX2.draw(win)
    YX3 = Point(619,841)
    YX4 = Point(75,841)
    YX4.draw(win)

    DMud = Polygon(YX1,YX2,YX3,YX4)
    DMud.setFill(FDMud)

    #Moni chest
    CH1 = Point(220,624)
    CH2 = Point(256,638)
    CH3 = Point(271,613)
    CH4 = Point(286,582)
    CH5 = Point(286,582)
    CH6 = Point(312,538)
    CH7 = Point(351,492)
    CH8 = Point(306,489)
    CH9 = Point(270,474)
    CH10 = Point(257,460)
    CH11 = Point(267,434)
    CH12 = Point(244,461)
    CH13 = Point(225,495)
    CH14 = Point(220,525)
    CH15 = Point(218,570)

    MChest = Polygon(CH1,CH2,CH3,CH4,CH5,CH6,CH7,CH8,CH9,CH10,CH11,CH12,CH13,CH14,CH15)
    MChest.setFill(MoniC)


    R1 = Point(259,641)
    R2 = Point(275,646)
    R3 = Point(317,566)
    R4 = Point(346,525)
    R5 = Point(385,490)
    R6 = Point(427,467)
    R7 = Point(471,455)
    R8 = Point(516,450)
    R9 = Point(509,440)
    R10 = Point(473,443)
    R11 = Point(414,465)
    R12 = Point(357,491)
    R13 = Point(324,525)
    R14 = Point(296,566)
    R15 = Point(266,627)

    M1chest = Polygon(R1,R2,R3,R4,R5,R6,R7,R8,R9,R10,R11,R12,R13,R14,R15)
    M1chest.setFill(MoniC)

    #Bie

    Y1 = Point(137,595)
    Y2 = Point(150,561)
    Y3 = Point(168,512)
    Y4 = Point(206,455)
    Y5 = Point(232,421)
    Y6 = Point(241,412)
    Y7 = Point(240,447)
    Y8 = Point(258,427)
    Y9 = Point(264,431)
    Y10 = Point(244,456)
    Y11 = Point(225,486)
    Y12 = Point(218,508)
    Y13 = Point(213,554)
    Y14 = Point(216,622)
    Y15 = Point(206,604)
    Y16 = Point(187,594)
    Y17 = Point(180,587)
    Y18 = Point(150,589)

    MBie = Polygon(Y1, Y2, Y3, Y4, Y5, Y6, Y7, Y8, Y9, Y10, Y11, Y12, Y13, Y14, Y15, Y16, Y17, Y18)
    MBie.setFill(MoniC)

    #Hair
    U1 = Point(239,446)
    U2 = Point(245,375)
    U3 = Point(235,313)
    U4 = Point(247,241)
    U5 = Point(275,178)
    U6 = Point(295,160)
    U7 = Point(304,155)
    U8 = Point(321,150)
    U9 = Point(359,147)
    U10 = Point(375,150)
    U11 = Point(396,164)
    U12 = Point(419,185)
    U13 = Point(435,221)
    U14 = Point(446,272)
    U15 = Point(450,337)
    U16 = Point(456,362)
    U17 = Point(464,383)
    U18 = Point(474,400)
    U19 = Point(505,435)
    U20 = Point(387,476)
    U21 = Point(269,437)
    U22 = Point(258,429)

    HairM = Polygon(U1,U2,U3,U4,U5,U6,U7,U8,U9,U10,U11,U12,U13,U14,U15,U16,U17,U18,U19,U20,U21,U22)
    HairM.setFill(Black)

    #moni Neck

    I1 = Point(315,386)
    I2 = Point(300,399)
    I3 = Point(280,421)
    I4 = Point(268,441)
    I5 = Point(261,460)
    I6 = Point(266,472)
    I7 = Point(287,481)
    I8 = Point(313,487)
    I9 = Point(338,490)
    I10 = Point(352,489)
    I11 = Point(387,475)
    I12 = Point(387,433)
    I13 = Point(391,372)
    I14 = Point(393,315)
    I15 = Point(375,332)
    I16 = Point(351,348)
    I17 = Point(326,357)
    I18 = Point(316,358)
    I19 = Point(321,397)
    I20 = Point(315,397)

    Neck1 = Polygon(I1,I2,I3,I4,I5,I6,I7,I8,I9,I10,I11,I12,I13,I14,I15,I16,I17,I18,I19,I20)
    Neck1.setFill(Mskin)

    #Moni face

    F1 = Point(391,308)
    F2 = Point(391,291)
    F3 = Point(389,272)
    F4 = Point(386,253)
    F5 = Point(378,230)
    F6 = Point(369,211)
    F7 = Point(352,193)
    F8 = Point(332,185)
    F9 = Point(313,181)
    F10 = Point(294,184)
    F11 = Point(279,200)
    F12 = Point(272,216)
    F13 = Point(267,243)
    F14 = Point(267,273)
    F15 = Point(271,299)
    F16 = Point(280,320)
    F17 = Point(292,337)
    F18 = Point(302,346)
    F19 = Point(315,353)
    F20 = Point(323,353)
    F21 = Point(341,346)
    F22 = Point(360,336)
    F23 = Point(376,324)
    F24 = Point(387,313)

    MFace = Polygon(F1,F2,F3,F4,F5,F6,F7,F8,F9,F10,F11,F12,F13,F14,F15,F16,F17,F18,F19,F20,F21,F22,F23,F24)
    MFace.setFill(Mskin)

    #Eye

    G1 = Point(332,253)
    G2 = Point(339,253)
    G3 = Point(339,256)
    G4 = Point(343,258)
    G5 = Point(347,256)
    G6 = Point(347,253)
    G7 = Point(356,254)
    G8 = Point(350,250)
    G9 = Point(343,249)
    G10 = Point(338,249)

    MEye1 = Polygon(G1,G2,G3,G4,G5,G6,G7,G8,G9,G10)
    MEye1.setFill(Black)

    MEye2 = Polygon(G1,G2,G3,G4,G5,G6,G7,G8,G9,G10)
    MEye2.setFill(Black)
    MEye2.move(-55,0)

#EyeB1
    H1 = Point(322,239)
    H2 = Point(328,236)
    H3 = Point(333,235)
    H4 = Point(342,238)
    H5 = Point(352,242)
    H6 = Point(359,244)

    MeyeB1 = Line(H1,H2)
    MeyeB2 = Line(H2,H3)
    MeyeB3 = Line(H3,H4)
    MeyeB4 = Line(H4,H5)
    MeyeB5 = Line(H5,H6)
#
    MeyeB11 = Line(H1,H2)
    MeyeB11.move(0,1)
    MeyeB21 = Line(H2,H3)
    MeyeB21.move(0,1)
    MeyeB31 = Line(H3,H4)
    MeyeB31.move(0,1)
    MeyeB41 = Line(H4,H5)
    MeyeB41.move(0,1)
    MeyeB51 = Line(H5,H6)
    MeyeB51.move(0,1)
#
    MeyeB12 = Line(H1,H2)
    MeyeB12.move(0,-1)
    MeyeB22 = Line(H2,H3)
    MeyeB22.move(0,-1)
    MeyeB32 = Line(H3,H4)
    MeyeB32.move(0,-1)
    MeyeB42 = Line(H4,H5)
    MeyeB42.move(0,-1)
    MeyeB52 = Line(H5,H6)
    MeyeB52.move(0,-1)

#EyeB2
    K1 = Point(272,245)
    K2 = Point(279,243)
    K3 = Point(287,240)
    K4 = Point(294,239)
    K5 = Point(301,243)

    M1eye1 = Line(K1,K2)
    M1eye2 = Line(K2,K3)
    M1eye3 = Line(K3,K4)
    M1eye4 = Line(K4,K5)

    M1eye12 = Line(K1,K2)
    M1eye12.move(0,1)
    M1eye22 = Line(K2,K3)
    M1eye22.move(0,1)
    M1eye32 = Line(K3,K4)
    M1eye32.move(0,1)
    M1eye42 = Line(K4,K5)
    M1eye42.move(0,1)

    M1eye13 = Line(K1,K2)
    M1eye13.move(0,-1)
    M1eye23 = Line(K2,K3)
    M1eye23.move(0,-1)
    M1eye33 = Line(K3,K4)
    M1eye33.move(0,-1)
    M1eye43 = Line(K4,K5)
    M1eye43.move(0,-1)
    
    #DRESSS
    
    L1 = Point(134,598)
    L2 = Point(122,634)
    L3 = Point(119,655)
    L4 = Point(124,670)
    L5 = Point(134,687)
    L6 = Point(152,699)
    L7 = Point(172,703)
    L8 = Point(192,702)
    L9 = Point(221,695)
    L10 = Point(218,687)
    L11 = Point(216,677)
    L12 = Point(218,666)
    L13 = Point(224,655)
    L14 = Point(235,647)
    L15 = Point(248,643)
    L16 = Point(254,640)
    L17 = Point(238,633)
    L18 = Point(222,628)
    L19 = Point(211,623)
    L20 = Point(211,617)
    L21 = Point(206,609)
    L22 = Point(195,599)
    L23 = Point(183,594)
    L24 = Point(176,588)
    L25 = Point(163,588)
    L26 = Point(150,589)

    MArm1 = Polygon(L1,L2,L3,L4,L5,L6,L7,L8,L9,L10,L11,L12,L13,L14,L15,L16,L17,L18,L19,L20,L21,L22,L23,L24,L25,L26)
    MArm1.setFill(MoniC)
    #nose

    N1 = Point(327,293)
    N2 = Point(327,299)
    N3 = Point(321,300)

    MNose = Line(N1,N2)
    MNose1 = Line(N2,N3)

    M1Nose = Line(N1,N2)
    M1Nose.move(1,1)
    M1Nose1 = Line(N2,N3)
    M1Nose1.move(1,1)

    M2Nose = Line(N1,N2)
    M2Nose.move(-1,-1)
    M2Nose1 = Line(N2,N3)
    M2Nose1.move(-1,-1)

    N4 = Point(313,298)
    N5 = Point(307,301)
    N6 = Point(302,300)
    N7 = Point(300,296)
    N8 = Point(301,289)
    N9 = Point(304,276)

    LNose = Line(N4,N5)
    LNose1 = Line(N5,N6)
    LNose2 = Line(N6,N7)
    LNose3 = Line(N7,N8)
    LNose4 = Line(N8,N9)

    L1Nose = Line(N4,N5)
    L1Nose.move(1,1)
    L1Nose1 = Line(N5,N6)
    L1Nose1.move(1,1)
    L1Nose2 = Line(N6,N7)
    L1Nose2.move(1,1)
    L1Nose3 = Line(N7,N8)
    L1Nose3.move(1,1)
    L1Nose4 = Line(N8,N9)
    L1Nose4.move(1,1)

    L2Nose = Line(N4,N5)
    L2Nose.move(1,1)
    L2Nose1 = Line(N5,N6)
    L2Nose1.move(1,1)
    L2Nose2 = Line(N6,N7)
    L2Nose2.move(1,1)
    L2Nose3 = Line(N7,N8)
    L2Nose3.move(1,1)
    L2Nose4 = Line(N8,N9)
    L2Nose4.move(1,1)

    WE1 = Point(318,270)
    WE2 = Point(319,258)

    MNOSE = Line(WE1,WE2)
    M1NOSE = Line(WE1,WE2)
    M1NOSE.move(1,1)
    
    M2NOSE = Line(WE1,WE2)
    M2NOSE.move(-1,-1)
    
    
    
        
    #mouth

    J1 = Point(291,310)
    J2 = Point(295,313)
    J3 = Point(295,313)
    J4 = Point(328,313)
    J5 = Point(328,313)
    J6 = Point(336,308)

    Mmouth1 = Line(J1,J2)
    Mmouth2 = Line(J3,J4)
    Mmouth3 = Line(J5,J6)

    Mmouth11 = Line(J1,J2)
    Mmouth11.move(0,1)
    Mmouth21 = Line(J3,J4)
    Mmouth21.move(0,1)
    Mmouth31 = Line(J5,J6)
    Mmouth31.move(0,1)

    Mmouth12 = Line(J1,J2)
    Mmouth12.move(0,-1)
    Mmouth22 = Line(J3,J4)
    Mmouth22.move(0,-1)
    Mmouth32 = Line(J5,J6)
    Mmouth32.move(0,-1)

    J7 = Point(304,323)
    J8 = Point(319,323)

    Mmouth4 = Line(J7,J8)
    
    Mmouth41 = Line(J7,J8)
    Mmouth41.move(0,1)
    Mmouth42 = Line(J7,J8)
    Mmouth42.move(0,-1)

    #HandSkin
    
    Z1 = Point(221,694)
    Z2 = Point(242,693)
    Z3 = Point(275,728)
    Z4 = Point(299,746)
    Z5 = Point(321,754)
    Z6 = Point(325,752)
    Z7 = Point(335,756)
    Z8 = Point(345,758)
    Z9 = Point(356,752)
    Z10 = Point(365,752)
    Z11 = Point(366,749)
    Z12 = Point(358,733)
    Z13 = Point(327,704)
    Z14 = Point(319,697)
    Z15 = Point(321,696)
    Z16 = Point(370,722)
    Z17 = Point(381,722)
    Z18 = Point(381,719)
    Z19 = Point(357,694)
    Z20 = Point(335,678)
    Z21 = Point(316,666)
    Z22 = Point(296,656)
    Z23 = Point(255,640)
    Z24 = Point(234,647)
    Z25 = Point(221,659)
    Z26 = Point(217,668)
    Z27 = Point(216,680)
    Z28 = Point(218,691)

    MHand1 = Polygon (Z1,Z2,Z3,Z4,Z5,Z6,Z7,Z8,Z9,Z10,Z11,Z12,Z13,Z14,Z15,Z16,Z17,Z18,Z19,Z20,Z21,Z22,Z23,Z24,Z25,Z26,Z27,Z28)
    MHand1.setFill(Mskin)


    V1 = Point(292,724)
    V2 = Point(324,751)
    
    MFinger = Line(V1,V2)
    MFinger1 = Line(V1,V2)
    MFinger1.move(1,1)
    MFinger2 = Line(V1,V2)
    MFinger2.move(-1,-1)
    
    V3 = Point(311,713)
    V4 = Point(356,753)

    M1Finger = Line(V3,V4)
    M1Finger1 = Line(V3,V4)
    M1Finger1.move(1,1)
    M1Finger2 = Line(V3,V4)
    M1Finger2.move(-1,-1)
    
    #Hand 2

    QW1 = Point(300,750)
    QW2 = Point(284,752)
    QW3 = Point(274,751)
    QW4 = Point(264,747)
    QW5 = Point(243,759)
    QW6 = Point(235,769)
    QW7 = Point(229,768)
    QW8 = Point(226,763)
    QW9 = Point(217,762)
    QW10 = Point(215,759)
    QW11 = Point(209,758)
    QW12 = Point(205,754)
    QW13 = Point(197,750)
    QW14 = Point(194,741)
    QW15 = Point(197,724)
    QW16 = Point(213,706)
    QW17 = Point(229,696)
    QW18 = Point(241,694)
    QW19 = Point(276,729)

    MHand2 = Polygon(QW1,QW2,QW3,QW4,QW5,QW6,QW7,QW8,QW9,QW10,QW11,QW12,QW13,QW14,QW15,QW16,QW17,QW18,QW19)
    MHand2.setFill(Mskin)
    #FingerFix
    QE1 = Point(226,764)
    QE2 = Point(247,737)

    LFinger = Line(QE1,QE2)
    LF1inger = Line(QE1,QE2)
    LF1inger.move(1,1)
    LF1inger1 = Line(QE1,QE2)
    LF1inger1.move(-1,-1)

    QE3 = Point(215,759)
    QE4 = Point(216,750)
    QE5 = Point(235,725)

    LFinger1 = Line(QE3,QE4)
    LFinger2 = Line(QE4,QE5)

    LFinger1x = Line(QE3,QE4)
    LFinger1x.move(1,1)
    
    LFinger2x = Line(QE4,QE5)
    LFinger2x.move(1,1)
    
    LFinger11 = Line(QE3,QE4)
    LFinger11.move(-1,-1)
    
    LFinger21 = Line(QE4,QE5)
    LFinger21.move(-1,-1)

    QE6 = Point(203,753)
    QE7 = Point(207,733)
    QE8 = Point(225,715)

    L1Finger1 = Line(QE6,QE7)
    L1Finger2 = Line(QE7,QE8)

    L1Finger11 = Line(QE6,QE7)
    L1Finger11.move(1,1)
    L1Finger21 = Line(QE7,QE8)
    L1Finger21.move(1,1)

    L1Finger12 = Line(QE6,QE7)
    L1Finger12.move(-1,-1)
    L1Finger22 = Line(QE7,QE8)
    L1Finger22.move(-1,-1)

    #Thumb Finger

    RT1 = Point(333,673)
    RT2 = Point(343,677)
    RT3 = Point(357,679)
    RT4 = Point(357,681)
    RT5 = Point(355,685)
    RT6 = Point(346,686)
    RT7 = Point(333,687)

    MThumb = Polygon(RT1,RT2,RT3,RT4,RT5,RT6,RT7)
    MThumb.setFill(Mskin)
    
    #Clothes

    ER1 = Point(137,580)
    ER2 = Point(131,579)
    ER3 = Point(124,580)
    ER4 = Point(112,588)
    ER5 = Point(104,597)
    ER6 = Point(95,611)
    ER7 = Point(80,624)
    ER8 = Point(75,627)
    ER9 = Point(75,841)
    ER10 = Point(619,841)
    ER11 = Point(619,784)
    ER12 = Point(600,760)
    ER13 = Point(589,740)
    ER14 = Point(580,715)
    
    ERClo = Polygon(ER1,ER2,ER3,ER4,ER5,ER5,ER6,ER7,ER8,ER9,ER10,ER11,ER12,ER13,ER14)
    ERClo.setFill(MoniC)

    TY1 = Point(526,468)
    TY2 = Point(474,519)
    TY3 = Point(466,538)
    TY4 = Point(464,559)
    TY5 = Point(464,582)
    TY6 = Point(467,600)
    TY7 = Point(470,618)
    TY8 = Point(471,649)
    TY9 = Point(468,670)
    TY10 = Point(451,676)
    TY11 = Point(422,680)
    TY12 = Point(384,687)
    TY13 = Point(362,690)
    TY14 = Point(356,693)
    TY15 = Point(314,692)
    TY16 = Point(298,721)
    TY17 = Point(368,749)
    TY18 = Point(408,752)
    TY19 = Point(440,759)
    TY20 = Point(493,761)
    TY21 = Point(523,758)
    TY22 = Point(547,748)
    TY23 = Point(567,732)
    TY24 = Point(579,713)
    TY25 = Point(580,682)
    TY26 = Point(577,651)
    TY27 = Point(569,623)
    TY28 = Point(567,607)
    TY29 = Point(565,575)
    TY30 = Point(559,542)
    TY31 = Point(553,520)
    TY32 = Point(541,494)
    TY33 = Point(538,488)

    MRightH = Polygon(TY1,TY2,TY3,TY4,TY5,TY6,TY7,TY8,TY9,TY10,TY11,TY12,TY13,TY14,TY15,TY16,TY17,TY18,TY19,TY20,TY21,TY22,TY23,TY24,TY25,TY26,TY27,TY28,TY29,TY30,TY31,TY32,TY33)
    MRightH.setFill(MoniC)


    YU1 = Point(526,468)
    YU2 = Point(521,458)
    YU3 = Point(515,452)
    YU4 = Point(486,452)
    YU5 = Point(465,455)
    YU6 = Point(441,461)
    YU7 = Point(417,470)
    YU8 = Point(387,487)
    YU9 = Point(367,502)
    YU10 = Point(345,524)
    YU11 = Point(326,550)
    YU12 = Point(309,579)
    YU13 = Point(301,594)
    YU14 = Point(285,625)
    YU15 = Point(262,660)
    YU16 = Point(355,692)
    YU17 = Point(495,697)
    YU18 = Point(498,553)
    YU19 = Point(472,522)
    YU20 = Point(538,488)

    MRightC = Polygon(YU1,YU2,YU3,YU4,YU5,YU6,YU7,YU8,YU9,YU10,YU11,YU12,YU13,YU14,YU15,YU16,YU17,YU18,YU19,YU20)
    MRightC.setFill(MoniC)

    #Shoulder FIX
    UI1 = Point(482,535)
    UI2 = Point(450,499)
    UI3 = Point(522,464)
    UI4 = Point(532,482)

    MFIX1 = Polygon(UI1,UI2,UI3,UI4)
    MFIX1.setFill(MoniC)
    MFIX1.setOutline(MoniC)
    # DETAILS
    OP1 = Point(468,666)
    OP2 = Point(509,593)
    CFIX1 = Line(OP1,OP2)

    OP3 = Point(468,670)
    OP4 = Point(519,657)
    CFIX2 = Line(OP3,OP4)

    OP5 = Point(457,675)
    OP6 = Point(513,674)
    OP7 = Point(534,681)
    CFIX3 = Line(OP5,OP6)
    CFIX3a = Line(OP6,OP7)

###############################################################
   #Picture 1 Draw
    Object = [rect1,BodyB,EarCL,EarCL1,Ear1CL1,FaceCL,FaceCL1,Shield,Shield1,Shield2,Shield3,Shield4,EyeB1,EyeB2,EyeCL,Eye1CL,EyeCL1,Eye1CL1,LetterA,TriA,MSkin,MBlack,SStar,Strip1,Strip2,Strip3,Strip4,Strip5,Strip6,Arm1,Boot1Top,Boot1Bot,Boot2Top,Boot2Bot,Belt1,Belt2,Belt3,Belt4,BLTFX,BLTFX1,rect3,]
    for i in Object:
        i.draw(win)
        sleep(.25)

    # Transition draw

    LetterT.draw(win)
    LetterO1.draw(win)
    LetterO2.draw(win)
    LetterO11.draw(win)
    LetterO22.draw(win)
    LetterE.draw(win)
    #LetterAA.draw(win)
    #LetterTA.draw(win)
    LetterZ.draw(win)
    QuestionMark.draw(win)
    QuestionMark1.draw(win)
    QuestionDot.draw(win)
    QuestionDot1.draw(win)
    
    
    sleep(1.25)
    
    
    #Picture2 Draw
        #Part1
    Object2 = [rect2,Frame,FrameTop,Bush1,Bush2,Bush3,Mud1,Mud2,Mud3,DMud,ERClo,HairM,MChest,M1chest,MBie,Neck1,MFace,MEye1,MEye2,Mmouth1,Mmouth2,Mmouth3,Mmouth4,Mmouth11,Mmouth21,Mmouth31,Mmouth12,Mmouth22,Mmouth32,Mmouth41,Mmouth42,MeyeB1,MeyeB2,MeyeB3,MeyeB4,MeyeB5,MeyeB11,MeyeB21,MeyeB31,MeyeB41,MeyeB51,MeyeB12,MeyeB22,MeyeB32,MeyeB42,MeyeB52,M1eye1,M1eye2,M1eye3,M1eye4,M1eye12,M1eye22,M1eye32,M1eye42,M1eye13,M1eye23,M1eye33,M1eye43,MArm1]
    for j in Object2:
        j.draw(win)
        sleep(.25)

        #Part2 
    Object3 = [MRightC,MRightH,MThumb,MHand1,MFinger,MFinger1,MFinger2,M1Finger,M1Finger1,M1Finger2,MNose,MNose1,M1Nose,M1Nose1,M2Nose,M2Nose1,LNose,LNose1,LNose2,LNose3,LNose4,L1Nose,L1Nose1,L1Nose2,L1Nose3,L1Nose4,L2Nose,L2Nose1,L2Nose2,L2Nose3,L2Nose4,MHand2,LFinger,LF1inger,LF1inger1,LFinger1,LFinger2, LFinger1x, LFinger2x, LFinger11, LFinger21, L1Finger1, L1Finger2, L1Finger11, L1Finger21, L1Finger12, L1Finger22,MNOSE,M1NOSE,M2NOSE]
    for k in Object3:
        k.draw(win)
        sleep(.25)
        
        #Part3
    Object4 = [MFIX1,CFIX1,CFIX2,CFIX3,CFIX3a]
    for l in Object4:
        l.draw(win)
        sleep(.25)
        
    

main()




       
