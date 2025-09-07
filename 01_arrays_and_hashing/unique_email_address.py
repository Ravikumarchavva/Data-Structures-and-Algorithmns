from typing import List
class Solution:

    def process_local_name(self, local_name: str) -> str:
        filtered_name = local_name.split('+')[0]
        return filtered_name.replace('.', '')
        
    def numUniqueEmails(self, emails: List[str]) -> int:

        filtered_emails = set()

        for email in emails:
            local_name = email.split('@')[0]
            domain_name = email.split('@')[1]
            filtered_emails.add(self.process_local_name(local_name) + '@' + domain_name)

        return len(filtered_emails)

if __name__ == "__main__":
    s = Solution()
    print(s.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob@leetcode.com","testemail+david@lee.tcode.com"]))