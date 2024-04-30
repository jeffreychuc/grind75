import collections
from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = collections.defaultdict(set)
        # graph is going to be a dict with an empty set as a default value
        email_to_name = {}
        # email to name will keep a mapping of each email to the actual name of the person the email belongs to
        for account in accounts:
            name = account[0]

            # [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
            # the name is the first element, the emails are the rest of the list
            # using the example input above you would get a graph like so

            # {
            #   "johnsmith@mail.com": [
            #     "john00@mail.com",
            #     "john_newyork@mail.com",
            #     "johnsmith@mail.com"
            #   ],
            #   "john_newyork@mail.com": [
            #     "johnsmith@mail.com"
            #   ],
            #   "john00@mail.com": [
            #     "johnsmith@mail.com"
            #   ],
            #   "mary@mail.com": [
            #     "mary@mail.com"
            #   ],
            #   "johnnybravo@mail.com": [
            #     "johnnybravo@mail.com"
            #   ]
            # }

            # we're using the first email in the list as the primary node
            for email in account[1:]:
                # add emails to the graphs based on the first email in the list
                graph[email].add(account[1])
                graph[account[1]].add(email)
                # do the reverse as well

                email_to_name[email] = name
                # this email to name hashmap is to keep a mapping of what name is going to what email

        res = []
        visited = set()

        # this will iterate over each key in the "graph" default dict
        for email in graph:
            # checks to see if we've already visited that email
            if email not in visited:
                # we want to visit each email
                stack = [email]
                # add the email to visited
                visited.add(email)

                local_res = []
                # while there are emails in the stack
                while stack:
                    # remove that node from the stack
                    node = stack.pop()
                    # add that node to the local_result
                    local_res.append(node)
                    # get each email from the graph that has that initial email
                    # so the initial loop would add
                    #     "john00@mail.com",
                    #     "john_newyork@mail.com",
                    #     "johnsmith@mail.com"
                    # to the stack then it would go back and
                    # go through each of the emails in the set for each of those emails until there
                    # were no more emails to check.  It would also skip all emails that it has seen already
                    for edge in graph[node]:
                        if edge not in visited:
                            stack.append(edge)
                            visited.add(edge)
                res.append([email_to_name[email]] + sorted(local_res))

        return res

# Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
# Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
