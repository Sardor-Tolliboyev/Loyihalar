{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5c6ae26d-c80c-468b-9ed7-8eee1bc66726",
   "metadata": {},
   "outputs": [],
   "source": [
    "# So'z topish o'yini\n",
    "\n",
    "import random\n",
    "from uzwords import words\n",
    "\n",
    "def get_word():\n",
    "    word = random.choice(words)\n",
    "    while \"-\" in word or ' ' in word:\n",
    "        word = random.choice(words)    \n",
    "    return word.upper()\n",
    "\n",
    "def display(user_letters,word):\n",
    "    display_letter=\"\"\n",
    "    for letter in word:\n",
    "        if letter in user_letters:\n",
    "            display_letter += letter\n",
    "        else:\n",
    "            display_letter += \"-\"\n",
    "    return display_letter\n",
    "\n",
    "def play():\n",
    "    word = get_word()\n",
    "    # So'zdagi harflar\n",
    "    word_letters = set(word)\n",
    "    # Foydalanuvchi kiritgan harflar\n",
    "    user_letters = ''\n",
    "    print(f\"Мен {len(word)} хонали сўз ўйладим. Топа оласизми?\")\n",
    "    # print(word)\n",
    "    while word_letters:\n",
    "        print(display(user_letters,word))\n",
    "        if user_letters:\n",
    "            print(f\"Шу вақтгача киритган ҳарфларингиз: {user_letters}\")\n",
    "        \n",
    "        letter = input(\"Ҳарф киритинг: \").upper()\n",
    "        if letter in user_letters:\n",
    "            print(\"Бу ҳарфни аввал киритгансиз. Бошқа ҳарф киритинг.\")\n",
    "            continue        \n",
    "        elif letter in word:\n",
    "            word_letters.remove(letter)\n",
    "            print(f\"{letter} ҳарфи тўғри.\")\n",
    "        else:\n",
    "            print(\"Бундай ҳарф йўқ.\")\n",
    "        user_letters += letter\n",
    "    print(f\"Табриклайман! {word} сўзини {len(user_letters)} та уринишда топдингиз.\")\n",
    "\n",
    "    play()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.12.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
