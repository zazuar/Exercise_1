#Functions will run as long as the parameters are met. Here we're setting the 


def produce_log(deliver_day, path):
#arguments to be (deliver_day, path)

    print("Day", deliver_day)
    produce_log = open(path)
#we are setting the produce_log to open the .txt files which are referenced below


    for line in produce_log:
        line = line.rstrip()
        words = line.split('|')


#since we split the text, now we're referencing the values by their index value 

        melon = words[0]
        count = words[1]
        amount = words[2]

        print("Delivered {} {}s for total of ${}".format(
            count, melon, amount))

    produce_log.close()


#These are the produce logs saved as .txt files. Since functiosn run
#top to bottom and it will only execute one file at a time.

produce_log(1, "um-deliveries-20140519.txt")
produce_log(2, "um-deliveries-20140520.txt")
produce_log(3, "um-deliveries-20140521.txt")


