# ZDI-15-586: Microsoft Windows VBScript CreateObject Function Use-After-Free Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-586
- **ZDI-CAN:** ZDI-CAN-3318
- **Date:** 2015-12-08
- **CVE:** CVE-2015-6135
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Simon Zuckerbraun - HP Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-586/
## Vulnerability Details

This vulnerability allows remote attackers to disclose the contents of memory on applications using the VBScript scripting language on vulnerable installations of Microsoft Windows. Microsoft Internet Explorer is an affected application. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the implementation of the VBScript CreateObject function. By supplying specially crafted parameters, an attacker can disclose the contents of memory. An attacker can use this information in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/library/security/ms15-124.aspx

## Disclosure Timeline

- 2015-09-22 - Vulnerability reported to vendor
- 2015-12-08 - Coordinated public release of advisory
