# ZDI-18-1004: (0Day) Hewlett Packard Enterprise Intelligent Management Center dbman Opcode 10013 Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1004
- **ZDI-CAN:** ZDI-CAN-6072
- **Date:** 2018-09-07
- **CVE:** N/A
- **CVSS:** 9.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** Intelligent Management Center
- **Credit:** sztivi
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1004/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Hewlett Packard Enterprise Intelligent Management Center. Authentication is not required to exploit this vulnerability. The specific flaw exists within the dbman service, which listens on TCP port 2810 by default. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute arbitrary code under the context of SYSTEM.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 04/25/18 to 05/09/18 - ZDI reported vulnerabilities to vendor 07/19/18 - Vendor replied indicating vendor did not consider these issues as vulnerabilities 07/23/18 - ZDI replied expressing the disagreement and provided reasons for the argument 09/03/18 - ZDI notified vendor these cases will 0-day on Friday September 7 -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the service to trusted machines. Only the clients and servers that have a legitimate procedural relationship with the service should be permitted to communicate with it. This could be accomplished in a number of ways, most notably with firewall rules/whitelisting.

## Disclosure Timeline

- 2018-04-25 - Vulnerability reported to vendor
- 2018-09-07 - Coordinated public release of advisory
- 2018-09-07 - Advisory Updated
