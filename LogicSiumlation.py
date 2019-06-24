
import time
# import gc


class MismatcheError(RuntimeError):
    def __init__(self, arg):
        self.args = arg
class LogicSimulator:
    dict_opt = {'and': 0, 'or': 1, 'xor': 2, 'nand': 3, 'nor': 4, 'xnor': 5, 'buf': 6, 'not': 7}
    def __init__(self,benchFile,ipFile,opFile):
        self.benchFile=benchFile
        self.ipFile=ipFile
        self.opFile=opFile
    def siumlation(self):
        gateValue = []
        gateDict = {}
        outPutStartIndex = 0
        middleGateStartIndex = 0
        gatelist = []
        # try:
        #将bench逻辑文件转化
        with open(self.benchFile, 'r') as f:
            count = 0
            meetMiddleFlag = False
            meetOutputFlag = False

            for aline in f:
                aline = aline.replace('\n', '')

                if (aline.startswith("#") or aline == None or len(aline) == 0):
                    continue
                elif aline.startswith("INPUT"):
                    tt = aline.split('(')
                    gName = str(tt[1].replace(')', ''))
                    gateDict[gName] = count
                    gateValue.append(None)
                    count += 1


                elif aline.startswith("OUTPUT"):
                    if meetOutputFlag == False:
                        meetOutputFlag = True
                        outPutStartIndex = count

                    tt = aline.split('(')
                    gName = str(tt[1].replace(')', ''))

                    gateDict[gName] = count
                    gateValue.append(None)
                    count += 1
                else:
                    if meetMiddleFlag == False:
                        meetMiddleFlag = True
                        middleGateStartIndex = count
                        # print("middlestart",count)
                    aline = aline.replace(' ', '')
                    aline = aline.replace('=', ',')
                    aline = aline.replace('(', ',')
                    aline = aline.replace(')', '')
                    tt = aline.split(',')
                    if (str(tt[0]) not in gateDict):
                        gateDict[str(tt[0])] = count
                        gateValue.append(None)
                        tt[0] = count
                        count += 1
                    else:
                        tt[0] = gateDict[str(tt[0])]
                    tt[1] = LogicSimulator.dict_opt[tt[1]]

                    for i in range(2, len(tt)):
                        tt[i] = int(gateDict[str(tt[i])])

                    gatelist.append(tt)
        # except IOError:
        #     print ("Error: 没有找到文件或读取文件失败")

        # else:
        # try:
        with open (self.ipFile,'r') as ip:
            with open(self.opFile, 'w') as fw:
                for ipvs in ip:
                    ipvs=ipvs.replace('\n','')

                    #fillInput
                    count = 0
                    for i in ipvs:
                        gateValue[count] = int(i)
                        count += 1

                    #doSim
                    for gateInfo in gatelist:
                        outGateIndex = gateInfo[0]
                        optType = gateInfo[1]
                        # optType=optType.lower()

                        if (optType == 4):
                            # NOR
                            tot = gateValue[gateInfo[2]]
                            for item in gateInfo[3:]:
                                tot |= gateValue[item]
                            v = ~tot
                        elif (optType < 4):
                            if (optType > 1):

                                if (optType == 2):
                                    # XOR
                                    v = gateValue[gateInfo[2]] ^ gateValue[gateInfo[3]]
                                else:  # 3
                                    # NAND
                                    tot = gateValue[gateInfo[2]]
                                    for item in gateInfo[3:]:
                                        tot &= gateValue[item]
                                    v = ~tot

                            elif (optType == 1):
                                # OR
                                tot = gateValue[gateInfo[2]]
                                for item in gateInfo[3:]:
                                    tot |= gateValue[item]
                                v = tot
                            else:
                                # AND
                                tot = gateValue[gateInfo[2]]
                                for item in gateInfo[3:]:
                                    tot &= gateValue[item]
                                v = tot

                        elif (optType > 4):
                            if (optType > 6):
                                v = ~ gateValue[gateInfo[2]]
                            elif (optType == 6):
                                v = gateValue[gateInfo[2]]
                            else:
                                tot = gateValue[gateInfo[2]]
                                for item in gateInfo[3:]:
                                    tot |= gateValue[item]
                                v = ~tot
                        else:
                            raise Exception("Unknown Gate OPT")

                        gateValue[outGateIndex] = v

                    #gatherOutput
                    opvs = ''
                    for item in gateValue[outPutStartIndex:middleGateStartIndex]:
                        opvs+=str(item)
                    fw.write(ipvs + ' ' + opvs + '\n')

        # except MismatcheError:
        #     print(MismatcheError,"Input Size Mismatch")
        # except Exception:
        #     print(Exception,"Unknown Gate OPT")
        # except IOError:
        #     print ("Error:InputFile 没有找到文件或读取文件失败")

    # def gatherOutput(self,ipvs,fw):
    #     opvs=''
    #     for item in self.gateValue[self.outPutStartIndex:self.middleGateStartIndex]:
    #         opvs.join(str(item))
    #
    #     fw.write(ipvs+' '+opvs+'\n')




    # def fillInput(self,ipvs):
    #     count=0
    #     for i in ipvs:
    #         self.gateValue[count]=int(i)
    #         count+=1




    # def parseBenchFile(self):
    #
    #     with open(self.benchFile, 'r') as f:
    #         count=0
    #         meetMiddleFlag= False
    #         meetOutputFlag = False
    #
    #         for aline in f:
    #
    #
    #             aline = aline.replace('\n', '')
    #
    #             if (aline.startswith("#") or aline == None or len(aline) == 0):
    #                 continue
    #             elif aline.startswith("INPUT"):
    #                 tt = aline.split('(')
    #                 gName = str(tt[1].replace(')', ''))
    #                 self.gateDict[gName]=count
    #                 self.gateValue.append(None)
    #                 count += 1
    #
    #
    #             elif aline.startswith("OUTPUT"):
    #                 if meetOutputFlag==False:
    #                     meetOutputFlag=True
    #                     self.outPutStartIndex=count
    #                     # print("outputstart",count)
    #
    #                 tt = aline.split('(')
    #                 gName = str(tt[1].replace(')', ''))
    #
    #                 self.gateDict[gName] = count
    #                 self.gateValue.append(None)
    #                 count += 1
    #             else:
    #                 if meetMiddleFlag==False:
    #                     meetMiddleFlag=True
    #                     self.middleGateStartIndex=count
    #                     # print("middlestart",count)
    #                 aline = aline.replace(' ', '')
    #                 aline = aline.replace('=', ',')
    #                 aline = aline.replace('(', ',')
    #                 aline = aline.replace(')', '')
    #                 tt = aline.split(',')
    #                 if (str(tt[0]) not in self.gateDict):
    #                     self.gateDict[str(tt[0])] = count
    #                     self.gateValue.append(None)
    #                     tt[0]=count
    #                     count += 1
    #                 else:
    #                     tt[0]=self.gateDict[str(tt[0])]
    #                 tt[1]=LogicSimulator.dict_opt[tt[1]]
    #
    #                 for i in range (2,len(tt)):
    #                     tt[i]=int(self.gateDict[str(tt[i])])
    #
    #                 self.gatelist.append(tt)
    #

    # def doSim(self,gateInfo):
    #     # print(gateInfo)
    #     outGateIndex=gateInfo[0]
    #     optType=gateInfo[1]
    #     # optType=optType.lower()
    #
    #     if (optType == 4):
    #         #NOR
    #         tot = gateInfo[2]
    #         for item in gateInfo[3:]:
    #             tot |= self.gateValue[item]
    #         v=~tot
    #     elif(optType<4):
    #         if(optType>1):
    #
    #             if (optType ==2):
    #                 #XOR
    #                 v = self.gateValue[gateInfo[2]] ^ self.gateValue[gateInfo[3]]
    #             else: #3
    #                 #NAND
    #                 tot = gateInfo[2]
    #                 for item in gateInfo[3:]:
    #                     tot &= self.gateValue[item]
    #                 v=~tot
    #
    #         elif (optType==1):
    #             #OR
    #             tot = gateInfo[2]
    #             for item in gateInfo[3:]:
    #                 tot |= self.gateValue[item]
    #             v=tot
    #         else:
    #             #AND
    #             tot = gateInfo[2]
    #             for item in gateInfo[3:]:
    #                 tot &= self.gateValue[item]
    #             v=tot
    #
    #     elif (optType > 4):
    #         if (optType > 6):
    #             v = ~ self.gateValue[gateInfo[2]]
    #         elif (optType == 6):
    #             v = self.gateValue[gateInfo[2]]
    #         else:
    #             tot = gateInfo[2]
    #             for item in gateInfo[3:]:
    #                 tot |= self.gateValue[item]
    #             v=~tot
    #     else:
    #         raise Exception("Unknown Gate OPT")
    #
    #     self.gateValue[outGateIndex] = v
    #     # print(self.gateValue)

    # def AND(self, gateInfo):
    #     tot=gateInfo[2]
    #     for item in gateInfo[3:]:
    #         tot &=self.gateValue[item]
    #     return tot
    #
    # def OR(self, gateInfo):
    #     tot = gateInfo[2]
    #     for item in gateInfo[3:]:
    #         tot |= self.gateValue[item]
    #     return tot
    #
    # def XOR(self, gateInfo):
    #     return self.gateValue[gateInfo[2]]^self.gateValue[gateInfo[3]]
    #
    # def NAND(self, gateInfo):
    #     return ~(self.AND(gateInfo))
    #
    # def NOR(self, gateInfo):
    #     return ~(self.OR(gateInfo))
    #
    # def XNOR(self, gateInfo):
    #     return ~(self.XOR(gateInfo))
    #
    # def BUF(self, gateInfo):
    #     return self.gateValue[gateInfo[2]]
    #
    # def NOT(self, gateInfo):
    #     return ~ self.gateValue[gateInfo[2]]

# gc.disable()
start = time.process_time()
benchFile = "/Users/liusunhe/testfile/bench/c17_UX.bench.txt"
ipFile = "/Users/liusunhe/testfile/input/c17_all_ip.txt"
opFile='/Users/liusunhe/testfile/outputPython/c17_all_op.txt'
test=LogicSimulator(benchFile,ipFile,opFile)

test.siumlation()

end = time.process_time()
print('Running time: %s Seconds' % (end - start))

# gc.enable()