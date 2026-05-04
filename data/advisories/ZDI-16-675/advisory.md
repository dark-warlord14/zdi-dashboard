# ZDI-16-675: Microsoft Windows ADO Recordset GetRows Use-After-Free Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-675
- **ZDI-CAN:** ZDI-CAN-3956
- **Date:** 2017-01-10
- **CVE:** CVE-2016-3375
- **CVSS:** 2.6
- **CVSS Vector:** AV:N/AC:H/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-675/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the GetRows method of the Recordset object implemented by Microsoft ActiveX Data Objects (ADO). By performing actions in script an attacker can cause a pointer to be reused after it has been freed. An attacker could leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/library/security/ms16-104.aspx

## Disclosure Timeline

- 2016-09-06 - Vulnerability reported to vendor
- 2017-01-10 - Coordinated public release of advisory
