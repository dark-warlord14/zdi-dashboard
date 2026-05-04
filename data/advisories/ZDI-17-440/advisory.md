# ZDI-17-440: (0Day) Lepide LepideAuditor Suite Malicious Server Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-440
- **ZDI-CAN:** ZDI-CAN-3833
- **Date:** 2017-06-21
- **CVE:** N/A
- **CVSS:** 9.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Lepide
- **Affected Products:** LepideAuditor Suite
- **Credit:** Steven Seeley of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-440/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Lepide LepideAuditor Suite. Authentication is not required to exploit this vulnerability. The specific flaw exists within genratereports.php. The issue lies in the failure to properly validate a user-supplied command prior to using it in system calls. The more general flaw is that the software trusts responses from a server that is specified by a user and can be induced to execute commands from that server. An attacker can leverage this vulnerability to execute arbitrary code under the context of SYSTEM.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 07/01/2016 - ZDI reported the vulnerability to a previous known contact with this vendor 05/12/2017 - ZDI sent follow-up to the vendor 06/02/2017 - ZDI sent follow-up to the vendor -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the service to trusted machines. Only the clients and servers that have a legitimate procedural relationship with the service should be permitted to communicate with it. This could be accomplished in a number of ways, most notably with firewall rules/whitelisting. These features are available in the native Windows Firewall, as described in http://technet.microsoft.com/en-us/library/cc725770%28WS.10%29.aspx and numerous other Microsoft Knowledge Base articles.

## Disclosure Timeline

- 2016-07-01 - Vulnerability reported to vendor
- 2017-06-21 - Coordinated public release of advisory
