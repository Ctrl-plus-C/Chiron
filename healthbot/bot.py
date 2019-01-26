import zulip
import pprint
import requests

pp = pprint.PrettyPrinter(indent=4)


class Bot():
    def __init__(self):
        self.client = zulip.Client(config_file="~/.zuliprc")
        self.subscribe()
        print("subscribed")

    def subscribe(self):
        stream_data = self.client.get_streams().get("streams")
        temp_dict = {}
        stream_list = []
        for data in stream_data:
            temp_dict["name"] = data.get("name")
            stream_list.append(temp_dict)

        result = self.client.add_subscriptions(stream_list)
        # pp.pprint(r)
        pp.pprint(stream_data)

    def process(self, msg):
        word = msg.get('content').lower().split(" ")
        print(word)
        # s = "Invalid command"
        words = ' '.join(word[1:])
        print(words)

        send_dict = {
            "type": "stream",
            "to": msg.get("display_recipient"),
            "subject": msg.get("subject"),
            "content": "Invalid command"
        }

        text_keys = ' '.join(word[3:])
        if word[1] == "diagnose" and word[2]=="disease":            
            re = requests.post(url = "127.0.0.1/8000/api/parse", data = text_keys)
            import pdb; pdb.set_trace()
            rezero = re["result"][0]
            ind = rezero["indications_and_doses"]
            dos = rezero["dosage_and_administration"]
            des = rezero["description"]
            inf = rezero["information_for_patients"]
            ove = rezero["overdosage"]
            
            result = 0#re.text
            send_dict["content"] = result
            result = self.client.send_message(send_dict)
            pp.pprint(result) 
        elif word[1] == "describe" and word[2]=="medicine":
            re = requests.post(url = "http://127.0.0.1:8000/api/prescription", data = text_keys)
            result = re.text
            send_dict["content"] = result
            result = self.client.send_message(send_dict)
            pp.pprint(result) 
        else:
            print("+++Err+++")
            result = self.client.send_message(send_dict)
        return


def main():
    bot = Bot()
    print("listening")
    bot.client.call_on_each_message(bot.process)

main()
