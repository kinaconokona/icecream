{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import json\n",
    "from linebot import LineBotApi\n",
    "from linebot.models import TextSendMessage\n",
    "\n",
    "\n",
    "file = open('info.json','r')\n",
    "info = json.load(file)\n",
    "\n",
    "CHANNEL_ACCESS_TOKEN = info['CHANNEL_ACCESS_TOKEN']\n",
    "line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)\n",
    "\n",
    "def main():\n",
    "    USER_ID = info['USER_ID']\n",
    "    messages = TextSendMessage(text = \"さいきん、アイス食べてる～❔\\nおいしーよー\")\n",
    "    line_bot_api.push_message(USER_ID, messages=messages)\n",
    "    \n",
    "if __name__ == \"__main__\":\n",
    "    main()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
