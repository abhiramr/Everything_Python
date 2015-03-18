# PEP-8 Compliant
# Program to validate parentheses


def bracket_checker(sentence):
    li = []
    left_indices = []
    right_indices = []
    k=0
    for i in sentence:
        if i == '(':
            k += 1
            left_indices.append(sentence.index(i))
        if i == ')':
            k -= 1
            right_indices.append(sentence.index(i))
    lsum = sum(left_indices)
    rsum = sum(right_indices)
    if k < 0 or k > 0 or (lsum > rsum):
        return 0
    if k == 0 and (lsum < rsum):
        return 1


def main():
    sen = input("Enter sentence to brackidate:")
    status = bracket_checker(sen)
    if status == 0:
        print("Invalid!")
    else:
        print("Valid!")

if __name__ == "__main__":
    main()
