# ZDI-16-366: Microsoft Internet Explorer PerformDoDragDrop Protected Mode Sandbox Escape Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-366
- **ZDI-CAN:** ZDI-CAN-3539
- **Date:** 2016-06-16
- **CVE:** CVE-2016-3211
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Ashutosh Mehra (https://twitter.com/ashutoshmehra)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-366/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the usage of the method IShdocvwBroker::PerformDoDragDrop. An attacker who has gained code execution within the Internet Explorer Protected Mode sandbox can leverage this method to place a malicious executable file in any location to which the user has write access. An attacker can leverage this vulnerability to execute code under the context of the user at medium integrity.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS16-063

## Disclosure Timeline

- 2016-02-01 - Vulnerability reported to vendor
- 2016-06-16 - Coordinated public release of advisory
