# ZDI-17-973: (0Day) Linksys WVBR0 User-Agent Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-973
- **ZDI-CAN:** ZDI-CAN-4892
- **Date:** 2017-12-18
- **CVE:** CVE-2017-17411
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Linksys
- **Affected Products:** WVBR0
- **Credit:** Ricky "HeadlessZeke" Lawshae
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-973/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Linksys WVBR0. Authentication is not required to exploit this vulnerability. The specific flaw exists within the web management portal. The issue lies in the lack of proper validation of user data before executing a system call. An attacker could leverage this vulnerability to execute code with root privileges.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 06/14/17 - ZDI disclosed the report to the vendor 09/14/17 - ZDI sent a follow-up to the vendor requesting a status update 10/10/17 - ZDI sent a follow-up to the vendor requesting a status update 11/20/17 - ZDI notified the vendor of the intent to release the 0-day report on 12/12 12/18/17 - The vendor confirmed that WVB Firmware version number is 1.0.41, that the firmware is rolling out to customers now and they expect the firmware rollout to be completed by 12/20 -- Mitigation: Fixed in firmware version number 1.0.41 Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the service to trusted machines. Only the clients and servers that have a legitimate procedural relationship with the service should be permitted to communicate with it. This could be accomplished in a number of ways, most notably with firewall rules/whitelisting.

## Disclosure Timeline

- 2017-06-14 - Vulnerability reported to vendor
- 2017-12-18 - Coordinated public release of advisory
