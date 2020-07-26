from tkinter import *
from health_score_model import *

root = Tk()
root.title("Python Health Score")
label1 = Label(root, text="Feature data", font=("Helvetica", 16))
labelServer = Label(root, text="Server     ", font=("Helvetica", 16))
labelChild = Label(root, text="Child's App", font=("Helvetica", 16))
labelParent = Label(root, text="Parents' App", font=("Helvetica", 16))

e = Entry(root, width = 50)
e.grid(row = 1, column = 0)
label1.grid(row = 0, column = 0)
labelChild.grid(row = 2, column = 0)
labelServer.grid(row = 2, column = 1)
labelParent.grid(row = 2, column = 2)

def myClick():
    i = 3
    inputs = list(map(int,e.get().split(",")))
    # print(inputs)
    ct, t_encode, t_encrypt = child_app(inputs)
    str_inputs = [str(j)+' ' for j in inputs]
    label2 = Label(root, text='[Input]:'+ ''.join(str_inputs), font=("Helvetica", 16))
    label2.grid(row = i, column = 0)
    i += 1
    label2 = Label(root, text="Encrypt:CKKS.Ciphertext", font=("Helvetica", 16))
    label2.grid(row = i, column = 0)
    i += 1

    enc_result, t_predic = server(ct)
    label2 = Label(root, text="[Child]:CKKS.Ciphertext", font=("Helvetica", 16))
    label2.grid(row = i, column = 1)
    i += 1
    label2 = Label(root, text="Predict:CKKS.Ciphertext", font=("Helvetica", 16))
    label2.grid(row = i, column = 1)
    i += 1

    result, t_decrypt, t_decode = parents_app(enc_result)
    label2 = Label(root, text="[Server]:CKKS.Ciphertext", font=("Helvetica", 16))
    label2.grid(row = i, column = 2)
    i += 1
    label2 = Label(root, text="Decrypt: "+str(result), font=("Helvetica", 16))
    label2.grid(row = i, column = 2)
    i += 1

    result_nonHE_temp, time_nonHE_temp = test(inputs, result)
    

myButton= Button(root, text="Send", command = myClick)
myButton.grid(row = 1, column = 2)
root.mainloop()