{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# !wget \"https://archive.ics.uci.edu/ml/machine-learning-databases/00240/UCI HAR Dataset.zip\"\n",
    "# !wget \"https://archive.ics.uci.edu/ml/machine-learning-databases/00240/UCI HAR Dataset.names\"\n",
    "# import copy\n",
    "import os\n",
    "from subprocess import call\n",
    "\n",
    "print(\"\")\n",
    "\n",
    "print(\"Downloading...\")\n",
    "if not os.path.exists(\"UCI HAR Dataset.zip\"):\n",
    "    call(\n",
    "        'wget \"https://archive.ics.uci.edu/ml/machine-learning-databases/00240/UCI HAR Dataset.zip\"',\n",
    "        shell=True\n",
    "    )\n",
    "    print(\"Downloading done.\\n\")\n",
    "else:\n",
    "    print(\"Dataset already downloaded. Did not download twice.\\n\")\n",
    "\n",
    "\n",
    "print(\"Extracting...\")\n",
    "extract_directory = os.path.abspath(\"UCI HAR Dataset\")\n",
    "if not os.path.exists(extract_directory):\n",
    "    call(\n",
    "        'unzip -nq \"UCI HAR Dataset.zip\"',\n",
    "        shell=True\n",
    "    )\n",
    "    print(\"Extracting successfully done to {}.\".format(extract_directory))\n",
    "else:\n",
    "    print(\"Dataset already extracted. Did not extract twice.\\n\")\n"
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
   "version": "3.5.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
