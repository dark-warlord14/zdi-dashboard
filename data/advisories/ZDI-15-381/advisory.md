# ZDI-15-381: Microsoft MSXML generate-id Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-381
- **ZDI-CAN:** ZDI-CAN-2760
- **Date:** 2015-08-11
- **CVE:** CVE-2015-2440
- **CVSS:** 5.4
- **CVSS Vector:** AV:N/AC:H/Au:N/C:C/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Ucha Gobejishvili
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-381/
## Vulnerability Details

This vulnerability allows remote attackers to gain information about the layout of memory on vulnerable installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the implementation of the XSLT function generate-id. The unique ID string it returns can be used to infer the address at which an XML Node object is stored in memory. An attacker can use this information in conjunction with other vulnerabilities to execute code in the context of the process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/ms15-084

## Disclosure Timeline

- 2015-02-17 - Vulnerability reported to vendor
- 2015-08-11 - Coordinated public release of advisory
