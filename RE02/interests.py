#!/usr/bin/env python3

principal_amount = int(input("Principal amount:"))
interest_rate = int(input("Interest rate:"))
payout_freq = int(input("Payout frequency:"))
total = principal_amount * ((1 + interest_rate / payout_freq) ** 2 * payout_freq)
print(total)