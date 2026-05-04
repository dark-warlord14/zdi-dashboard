# ZDI-18-1417: Adobe Reader DC JavaScript AnnotsString Object Arbitrary Overwrite Restrictions Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1417
- **ZDI-CAN:** ZDI-CAN-7230
- **Date:** 2018-12-17
- **CVE:** CVE-2018-16018
- **CVSS:** 7.7
- **CVSS Vector:** AV:L/AC:H/PR:N/UI:R/S:C/C:H/I:H/A:H
- **Affected Vendors:** Adobe
- **Affected Products:** Reader
- **Credit:** Abdul-Aziz Hariri of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1417/
## Vulnerability Details

This vulnerability allows remote attackers to bypass API restrictions on vulnerable installations of Adobe Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the AnnotsString object. By creating a specially crafted PDF with specific JavaScript instructions, it is possible to overwrite the object's properties and methods. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb18-41.html

## Disclosure Timeline

- 2018-09-10 - Vulnerability reported to vendor
- 2018-12-17 - Coordinated public release of advisory
