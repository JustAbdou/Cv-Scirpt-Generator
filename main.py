import docx
from docx2pdf import convert

def CvScript():
    fileName = input("File Name  (The file should be in the Desktop) : ")
    companyName = input("Company Name to be Changed : ")
    newName = input("The new name : ")
    doc = docx.Document("PATH" + fileName +".docx")

    #This is the Paragraph location of my keyword (The company name)
    single_para = doc.paragraphs[4]

    for runs in single_para.runs:
        if(runs.text == companyName):
            runs.text = newName
            doc.save("PATH" + newName + ".docx")
            convert("PATH"+ newName + ".docx", "outputPATH" + newName + ".pdf")
            print("\n FILE HAS BEEN CREATED Successfully")

if __name__ == "__main__":
    CvScript()