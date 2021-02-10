import getopt
import sys
def main(argv):
    user_uuid = ''
    doc_uuid = ''
    task_id = 0
    try:
        opts, args = getopt.getopt(argv, "u:d:t:", ["user_uuid=", "doc_uuid=", "task_id="])
    except getopt.GetoptError:
        print('cw2 -u <user_uuid> -d <doc_uuid> -t <task_id>')
        opts=[]
    for opt, arg in opts:
        if opt == '-h':
            print('cw2.py -u <user_uuid> -d <doc_uuid> -t <task_id>')
            sys.exit()
        elif opt in ("-u", "--user_uuid"):
            user_uuid = arg
        elif opt in ("-d", "--doc_uuid"):
            doc_uuid = arg
        elif opt in ("-t", "--task_id"):
            task_id = arg
    if int(task_id) == 1:
        with open("../requirements.txt", 'r') as fin:
            print("Requirments.txt file content")
            print(fin.read())
    if int(task_id) == 2:
        if doc_uuid == '':
            print(" No doc_uuid supplied")
        else:
            task_2(doc_uuid)
            print("Histograms for per country been saved in : Graphs/countries_to_book_UUID.png")
            print("Histograms for per continent been saved in : Graphs/continent_to_book_UUI.png")
    elif int(task_id) == 3:
        task_3()
        print("Histograms of browser usage has been saved in 'Graphs/simple_browser_usage.png' ")
        print("Histograms of generalised browser usage has been saved in 'Graphs/general_browser_usage.png")
    elif int(task_id) == 4:
        print("10 most active readers")
        task_4(10)
    elif int(task_id) == 5:
        if (user_uuid == '') | (doc_uuid == ''):
            print("Provide user_uuid or/and doc_uuid")
            # 938601f24509a9f1 , 110727005030-000000009cca70787e5fba1fda005c85
        else:
            task_5(user_uuid, doc_uuid)
    elif int(task_id) == 6:
        if (user_uuid == '') | (doc_uuid == ''):
            print("Provide user_uuid or/and doc_uuid")
            # 938601f24509a9f1 , 110727005030-000000009cca70787e5fba1fda005c85
        else:
            task_6(user_uuid, doc_uuid)


if __name__ == "__main__":
    main(sys.argv[1:])
