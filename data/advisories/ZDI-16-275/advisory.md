# ZDI-16-275: Microsoft Internet Explorer Add-on Installer Enhanced Protected Mode Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-275
- **ZDI-CAN:** ZDI-CAN-3506
- **Date:** 2016-05-10
- **CVE:** CVE-2016-0194
- **CVSS:** 4.7
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Thomas Vanhoutte
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-275/
## Vulnerability Details

This vulnerability allows remote attackers to bypass the Enhanced Protected Mode sandbox of vulnerable installations of Microsoft Internet Explorer and disclose file contents. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the Internet Explorer Add-on Installer component. An attacker can use this component to read the contents of any file that the current user has access to.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/library/security/ms16-051.aspx

## Disclosure Timeline

- 2016-01-19 - Vulnerability reported to vendor
- 2016-05-10 - Coordinated public release of advisory
