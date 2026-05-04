# ZDI-15-377: Microsoft Internet Explorer add-on Installer Sandbox Escape Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-377
- **ZDI-CAN:** ZDI-CAN-2874
- **Date:** 2015-08-10
- **CVE:** CVE-2015-1743
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Thomas Vanhoutte
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-377/
## Vulnerability Details

This vulnerability allows remote attackers to escape Enhanced Protected Mode on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the usage of the add-on installer. An attacker can bypass checks within the add-on installer with special paths and junction points to achieve medium-integrity code execution under the context of the user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS15-056

## Disclosure Timeline

- 2015-04-23 - Vulnerability reported to vendor
- 2015-08-10 - Coordinated public release of advisory
