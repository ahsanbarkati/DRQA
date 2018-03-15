#!/usr/bin/env python3
# Copyright 2017-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
"""Interactive interface to full DrQA pipeline."""

import torch
import argparse
import code
import prettytable
import logging
import os

from termcolor import colored
from drqa import pipeline
from drqa.retriever import utils

print("import done!")
os.system("export CLASSPATH=$CLASSPATH:/home/shellphish/DrQA/data/corenlp/*")
#logger.info('Initializing pipeline...')
DrQA = pipeline.DrQA(
    cuda=None,
    fixed_candidates=None,
    reader_model=None,
    ranker_config={'options': {'tfidf_path': None}},
    db_config={'options': {'db_path': None}},
    tokenizer=None
)

print("Pipeline ready")

# ------------------------------------------------------------------------------
# Drop in to interactive mode
# ------------------------------------------------------------------------------

def process(question, candidates=None, top_n=1, n_docs=10):
    print("Processing")
    predictions = DrQA.process(
        question, candidates, top_n, n_docs, return_context=True
    )
    answer=""
    longans=""
    for p in predictions:
        text = p['context']['text']
        start = p['context']['start']
        end = p['context']['end']
        answer=text[start:end]
        longans=text
    ans=[answer,longans]
    return ans

