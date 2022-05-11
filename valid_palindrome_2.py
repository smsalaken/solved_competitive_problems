

# def rev(x):
#     t = len(x)
#     rev_x = ""
#     while t>0 :
#         rev_x = rev_x + x[t-1]
#         t = t - 1
#     return(rev_x)


# def validPalindrome(s):
#     for i in range(len(s)):
#         if (i == 0):
#             x = s[1:len(s)]
#             if ( x== rev(x)):
#                 return(True)
#         elif (i < len(s)):
#             x = s[0:i]+s[i+1:len(s)]
#             if (x == rev(x)):
#                 return(True)
#         else: 
#             x = s[0:len(s)]
#             if( x == rev(x)):
#                 return(True)
#     return(False)

def validPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    # Time: O(n)
    # Space: O(n)
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            one, two = s[left:right], s[left + 1:right + 1]
            return one == one[::-1] or two == two[::-1]
        left, right = left + 1, right - 1
    return True

# rev('abc')
# rev('ab c')
# validPalindrome('abca')
# validPalindrome('aba')
# validPalindrome('abc')

# x = "ihdssfebdreoidovhazbgqrzxwojobhuklacmdjjtwglxrvibhxlfqqftgcgcqvbajcjuccptjraegcjvgoegqqmyzzainbliroelyznsnmdkrybdblwzakcyyhgyutolqoamhitkrnzwsngssuysupvaurmuqvnyjcaxtvypvyalqaguwbyvcotrmqprkhmtdrxeaguejzyftgxueionhbsngaysucjihmvhabfydztkhdxfqjmfocqhsakimvobjazvzkwringqaqvswbyfzoqnrrixktdollxhuqlwmzmenwcevbcmawztlipofbqovsvlgmufehndenritjgfwybzntpakdpgstzdsizwvxzirdoqgzdpidtnhsietpedlilmlotytiigqibstsolqotaibdproaivfdasxntqusskyzwsyculbwspcfncbztnthktnjrikkzjcxvdksutsicowwdgsfyystrqlaypikwtvifvwueupdbiqpeujedyucjyjxeykcizmzrlctmooxzqdzdjktbrlhqjufwnkfzuovdlkdpygfjupxrcnmzzyrqgddoyfgayuyziklschezajqalztxthzedscyphcuevggvwbrkhznratnfrggzqmazyskzdzleeqmwlkzsjvmtclzxogzuidoyumiyvqpjwyzxvjfkjbesadfvlydesqdeihnuxkdjfzcgrmsmipvjhfhqvvsixllhgzeminbciadnutagkjatkldnlaxxsikldsmqmyoetrsvcsomqewobgopfmcjyticzzeredeuihmmsdlthtwxdjvrrphmymhnoenafivahkigfbuesyprcfkpiagmgwkadzmdsbcjsyapmgkdruogbvewrzzskzhptbfdditiomhaphajpvnwwbywgohmyixoacsfyhptzeakhwxycihtxhkswwssgevzhhdnvsyauvhahzgbvwoiaeryzkgpiezlf"
x = 'abcdefg'
validPalindrome(x)