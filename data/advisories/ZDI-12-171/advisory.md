# ZDI-12-171: (0Day) HP Intelligent Management Center UAM sprintf Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-171
- **ZDI-CAN:** ZDI-CAN-1348
- **Date:** 2012-08-29
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** Intelligent Management Center
- **Credit:** e6af8de8b1d4b2b6d5ba2610cbf9cd38
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-171/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Hewlett-Packard Intelligent Management Center. Authentication is not required to exploit this vulnerability. The flaw exists within the uam.exe component which listens by default on UDP port 1811. When logging received actions to a log file, sprintf is used to build the log message. The process does not properly verify the destination buffer on the stack is of sufficient size to handle the newly created string. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the SYSTEM user.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 180 day deadline. -- Mitigation: The overall design of the Intelligent Management Center assumes it runs as an application on a Windows server. Given the stated purpose of Intelligent Management Center, and the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the service to trusted machines. Only the clients and servers that have a legitimate procedural relationship with the HP Intelligent Management Center should be permitted to communicate with it. This could be accomplished in a number of ways, most notably with firewall rules/whitelisting. These features are available in the native Windows Firewall, as described in http://technet.microsoft.com/en-us/library/cc725770%28WS.10%29.aspx and numerous other Microsoft Knowledge Base articles.

## Disclosure Timeline

- 2011-10-21 - Vulnerability reported to vendor
- 2012-08-29 - Coordinated public release of advisory
