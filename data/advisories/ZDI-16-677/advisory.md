# ZDI-16-677: Microsoft Windows JavaScript Array.concat Type Confusion Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-677
- **ZDI-CAN:** ZDI-CAN-4331
- **Date:** 2017-01-20
- **CVE:** CVE-2016-7297
- **CVSS:** 5.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-677/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the JavaScript Array.concat method. By performing actions in JavaScript an attacker can trigger a type confusion condition. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/library/security/ms16-145.aspx

## Disclosure Timeline

- 2016-12-12 - Vulnerability reported to vendor
- 2017-01-20 - Coordinated public release of advisory
