# ZDI-15-518: Microsoft Windows JScript ArrayBuffer.slice Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-518
- **ZDI-CAN:** ZDI-CAN-3045
- **Date:** 2015-10-13
- **CVE:** CVE-2015-6053
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** CK
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-518/
## Vulnerability Details

This vulnerability allows remote attackers to disclose the contents of arbitrary memory locations on applications using the JScript scripting language on vulnerable installations of Microsoft Windows. Microsoft Internet Explorer is an affected application. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the implementation of the ArrayBuffer.slice method. By supplying specially crafted parameters, an attacker can read the contents of arbitrary memory locations. An attacker can use this information in conjunction with other vulnerabilities to execute code in the context of the process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/library/security/MS15-106

## Disclosure Timeline

- 2015-07-09 - Vulnerability reported to vendor
- 2015-10-13 - Coordinated public release of advisory
