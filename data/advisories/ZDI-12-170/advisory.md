# ZDI-12-170: (0Day) HP Application Lifecycle Management XGO.ocx ActiveX Control Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-170
- **ZDI-CAN:** ZDI-CAN-1327
- **Date:** 2012-08-29
- **CVE:** N/A
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** Application Lifecycle Management
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-170/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Hewlett-Packard Application Lifecycle Management. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the XGO.ocx ActiveX control. The control exposed two vulnerable functions: 'SetShapeNodeType', which is vulnerable to a type confusion allowing user specified memory to be used as an object; and 'CopyToFile' which allows an attacker to create and overwrite files on the system of the user invoking the control. The attacker can utilize these vulnerabilities to execute remote code under the context of the process.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 180 day deadline. -- Mitigation: Given the stated purpose of Application Lifecycle Management, and the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the service to trusted machines. Only the clients and servers that have a legitimate procedural relationship with the HP Application Lifecycle Management service should be permitted to communicate with it. This could be accomplished in a number of ways, most notably with firewall rules/whitelisting. These features are available in the native Windows Firewall, as described in http://technet.microsoft.com/en-us/library/cc725770%28WS.10%29.aspx and numerous other Microsoft Knowledge Base articles.

## Disclosure Timeline

- 2011-08-12 - Vulnerability reported to vendor
- 2012-08-29 - Coordinated public release of advisory
