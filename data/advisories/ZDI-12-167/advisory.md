# ZDI-12-167: (0Day) Novell File Reporter NFRAgent.exe VOL Tag Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-167
- **ZDI-CAN:** ZDI-CAN-1318
- **Date:** 2012-08-29
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Novell
- **Affected Products:** File Reporter
- **Credit:** Tenable Network Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-167/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell File Reporter Agent. Authentication is not required to exploit this vulnerability. The specific flaw exists within NFRAgent.exe which communicates with the Agent component over HTTPS on TCP port 3037. When parsing tags inside the VOL element, the process performs insufficient bounds checking on user-supplied data prior to copying it into a fixed-length buffer on the stack. This vulnerability can result in remote code execution under the context of the SYSTEM account.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 180 day deadline. -- Mitigation: Given the stated purpose of File Reporter, and the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the service to trusted machines. Only the clients and servers that have a legitimate procedural relationship with the Novell File Reporter Agent should be permitted to communicate with it. This could be accomplished in a number of ways, most notably with firewall rules/whitelisting. These features are available in the native Windows Firewall, as described in http://technet.microsoft.com/en-us/library/cc725770%28WS.10%29.aspx and numerous other Microsoft Knowledge Base articles.

## Disclosure Timeline

- 2011-10-21 - Vulnerability reported to vendor
- 2012-08-29 - Coordinated public release of advisory
