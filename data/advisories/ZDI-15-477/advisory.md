# ZDI-15-477: Adobe Reader DC addForegroundSprite Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-477
- **ZDI-CAN:** ZDI-CAN-3046
- **Date:** 2015-10-13
- **CVE:** CVE-2015-6699
- **CVSS:** 5.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Reader DC
- **Credit:** AbdulAziz Hariri and Jasiel Spelman of HP Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-477/
## Vulnerability Details

This vulnerability allows remote attackers to gain information about the layout of memory on vulnerable installations of Adobe Reader DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the addForegroundSprite function. The issue lies in excess values being returned in the error message when improper arguments are given. An attacker can use this information in conjunction with other vulnerabilities to execute arbitrary code under the context of the process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb15-24.html

## Disclosure Timeline

- 2015-07-28 - Vulnerability reported to vendor
- 2015-10-13 - Coordinated public release of advisory
