# ZDI-15-183: Microsoft Windows VBScript Regular Expression Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-183
- **ZDI-CAN:** ZDI-CAN-2791
- **Date:** 2015-05-12
- **CVE:** CVE-2015-1684
- **CVSS:** 5.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** SkyLined
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-183/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The vulnerability relates to how VBScript processes capturing groups in regular expressions. By performing a search using a regular expression that has an unusual form, an attacker can reveal data stored in the memory of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS15-043

## Disclosure Timeline

- 2015-03-03 - Vulnerability reported to vendor
- 2015-05-12 - Coordinated public release of advisory
