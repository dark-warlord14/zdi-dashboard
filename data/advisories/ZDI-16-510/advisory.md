# ZDI-16-510: Microsoft Internet Explorer Add-on Installer Enhanced Protected Mode Sandbox Escape Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-510
- **ZDI-CAN:** ZDI-CAN-3788
- **Date:** 2016-09-16
- **CVE:** CVE-2016-3292
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Thomas Vanhoutte
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-510/
## Vulnerability Details

This vulnerability allows attackers to escape from the Enhanced Protected Mode sandbox on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the usage of the Internet Explorer Add-on Installer component. An attacker who has gained code execution within the Internet Explorer Enhanced Protected Mode sandbox can leverage this component to place a malicious HTML file in a predictable location at medium integrity. An attacker can leverage this in conjunction with other vulnerabilities to execute code under the context of the user at medium integrity.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS16-104

## Disclosure Timeline

- 2016-05-24 - Vulnerability reported to vendor
- 2016-09-16 - Coordinated public release of advisory
