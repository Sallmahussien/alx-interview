#!/usr/bin/python3
"""Defines 0-orime_game module"""


def isWinner(x, nums):
    """Return the winner from prime game"""
    if x < 1 or not nums:
        return None

    max_num = max(nums)
    primes = getPrimes(max_num)

    ben_score, maria_score = 0, 0

    for i in range(x):
        if nums[i] == 1:
            ben_score += 1
            continue

        round_set = [True for _ in range(nums[i] + 1)]
        idx = 2
        round_set_len = len(round_set)
        is_score_set = False

        while(idx < round_set_len):
            while (idx < len(round_set) and not primes[idx]
                   and not round_set[idx]):
                idx += 1

            if idx == len(round_set):
                ben_score += 1
                is_score_set = True
                break

            mutiple_idx = idx
            while(mutiple_idx < round_set_len):
                last_one_to_remove = 'maria'
                round_set[mutiple_idx] = False
                mutiple_idx *= mutiple_idx

            idx += 1
            while (idx < len(round_set) and not primes[idx]
                   and not round_set[idx]):
                idx += 1

            if idx == len(round_set):
                maria_score += 1
                is_score_set = True
                break

            mutiple_idx = idx
            while(mutiple_idx < round_set_len):
                last_one_to_remove = 'ben'
                round_set[mutiple_idx] = False
                mutiple_idx *= mutiple_idx

            idx += 1

        if not is_score_set:
            if last_one_to_remove == 'ben':
                ben_score += 1
            elif last_one_to_remove == 'maria':
                maria_score += 1

    if ben_score == maria_score:
        return None

    return 'Ben' if ben_score > maria_score else 'Maria'


def getPrimes(num):
    primes = [True for i in range(num + 1)]

    p = 2
    while(p * p <= num):
        if primes[p]:
            for i in range(p*p, num+1, p):
                primes[i] = False

        p += 1

    return primes
