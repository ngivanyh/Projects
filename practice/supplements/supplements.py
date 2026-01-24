params = [int(param) for param in input().split(" ")]

EYE_SUPPLEMENT_TYPES = params[0]
STOMACH_SUPPLEMENT_TYPES = params[1]

# generate indentifiers
EYE_SUPPLEMENT_CODES = [chr(i) for i in range(0, EYE_SUPPLEMENT_TYPES * 2, 2)] # gets the even-numbered UTF+16 chars
STOMACH_SUPPLEMENT_CODES = [chr(j) for j in range(1, STOMACH_SUPPLEMENT_TYPES * 2, 2)] # gets the odd-numbered UTF+16 chars
COMBINED_CODES = EYE_SUPPLEMENT_CODES + STOMACH_SUPPLEMENT_CODES

disallowed_mixtures = [input().split(" ") for _ in range(params[2])]
disallowed_mixtures = [(EYE_SUPPLEMENT_CODES[int(a) - 1], STOMACH_SUPPLEMENT_CODES[int(b) - 1]) for a, b in disallowed_mixtures]

# print(EYE_SUPPLEMENT_CODES, STOMACH_SUPPLEMENT_CODES)

# print(disallowed_mixtures)

mixtures_list = [[med] for med in COMBINED_CODES]

def avail_mixtures(cur_mix):
    global disallowed_mixtures, COMBINED_CODES
    
    propsed_mix = cur_mix
    
    returned = []
    for medicine in COMBINED_CODES:
        if not medicine in propsed_mix:
            propsed_mix.append(medicine)
            # print(f"proposed: {propsed_mix}\nvalid: {returned}")
            
            for a, b in disallowed_mixtures:
                # print(f"disallowed mix: {(a, b)}", end="\n\n")
                if (a not in propsed_mix) and (b not in propsed_mix) and (propsed_mix not in returned):
                    # print(f"valid! {propsed_mix}")
                    returned.append(propsed_mix)
                    # print(f"returned as of validity {returned}")
                    yield propsed_mix
                # print(f"out of if and yielded{returned}")
            # print(f"out of FOR{returned}")
                
            propsed_mix = propsed_mix[:len(propsed_mix) - 1]
        # print(f"out of del{returned}")

def gen_mix(mix):
    global mixtures_list, mixture_amounts
    
    for extended_mix in avail_mixtures(mix):
        if not sorted(extended_mix) in mixtures_list:
            mixtures_list.append(sorted(extended_mix))
            gen_mix(extended_mix)

for mix in mixtures_list:
    gen_mix(mix)
    
print(max([len(mix) for mix in mixtures_list]))