{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "257f2ddf-aebe-4b4d-aa41-28082edeb672",
   "metadata": {},
   "outputs": [],
   "source": [
    "# so'z topish o'yini \n",
    "\n",
    "import random\n",
    "from suzlar_ruyxati import suzlar\n",
    "\n",
    "def tasodifiy_suz():\n",
    "    suz = random.choice(suzlar)\n",
    "    while \"-\" in suz or ' ' in suz:\n",
    "        suz = random.choice(suzlar)    \n",
    "    return suz.upper()\n",
    "\n",
    "def natijasi(foyd_harflar, suz):\n",
    "    natija = \"\"\n",
    "    for harf in suz:\n",
    "        if harf in foyd_harflar:\n",
    "            natija += harf\n",
    "        else:\n",
    "            natija += \"-\"\n",
    "    return natija\n",
    "\n",
    "def play():\n",
    "    suz = tasodifiy_suz()\n",
    "    # So'zdagi harflar\n",
    "    suzdagi_harflar = set(suz)\n",
    "    # Foydalanuvchi kiritgan harflar\n",
    "    foyd_harflar = ''\n",
    "    print(f\"Мен {len(suz)} хонали сўз ўйладим. Топа оласизми?\")\n",
    "    # print(word)\n",
    "    while suzdagi_harflar:\n",
    "        print(natijasi(foyd_harflar, suz))\n",
    "        if foyd_harflar:\n",
    "            print(f\"Шу вақтгача киритган ҳарфларингиз: {foyd_harflar}\")\n",
    "        \n",
    "        harf = input(\"Ҳарф киритинг: \").upper()\n",
    "        if harf in foyd_harflar:\n",
    "            print(\"Бу ҳарфни аввал киритгансиз. Бошқа ҳарф киритинг.\")\n",
    "            continue        \n",
    "        elif harf in suz:\n",
    "            suzdagi_harflar.remove(harf)\n",
    "            print(f\"{harf} ҳарфи тўғри.\")\n",
    "        else:\n",
    "            print(\"Бундай ҳарф йўқ.\")\n",
    "        foyd_harflar += harf\n",
    "    print(f\"Табриклайман! {suz} сўзини {len(foyd_harflar)} та уринишда топдингиз.\")"
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
