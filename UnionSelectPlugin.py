import pandas as pd
import PyPluMA
import PyIO

class UnionSelectPlugin:
    def input(self, inputfile):
        parameters = PyIO.readParameters(inputfile)

        self.chow_df = pd.read_csv(PyPluMA.prefix()+"/"+parameters["GroupA"])
        self.wd_df = pd.read_csv(PyPluMA.prefix()+"/"+parameters["GroupB"])
        self.metadata_df = pd.read_csv(PyPluMA.prefix()+"/"+parameters["annotations"], sep="\t")

    def run(self):
        self.all_metabolites = set(self.chow_df['metabolite']).union(set(self.wd_df['metabolite']))
        print('Total number of metabolites: {}'.format(len(self.all_metabolites)))
        print(self.all_metabolites)

    def output(self, outputfile):
        df = pd.DataFrame({'CHEM_ID':list(self.all_metabolites)})
        df = df.merge(self.metadata_df, how='left', on='CHEM_ID')

        df.to_csv(outputfile+"/significant_annotated.csv", index=False)

        a = ["X{}".format(x) for x in self.chow_df['metabolite']]
        groupa = open(outputfile+"/groupA.txt", 'w')
        for x in a:
           groupa.write(x)
           groupa.write('\n')

        b = ["X{}".format(x) for x in self.wd_df['metabolite']]
        groupb = open(outputfile+"/groupB.txt", 'w')
        for x in b:
           groupb.write(x)
           groupb.write('\n')



