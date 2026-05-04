# ZDI-19-002: Adobe Acrobat Reader DC JavaScript Read-Only Variables Arbitrary Overwrite Restrictions Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-002
- **ZDI-CAN:** ZDI-CAN-7229
- **Date:** 2019-01-04
- **CVE:** CVE-2018-16018
- **CVSS:** 7.7
- **CVSS Vector:** AV:L/AC:H/PR:N/UI:R/S:C/C:H/I:H/A:H
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Reader DC
- **Credit:** Abdul-Aziz Hariri of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-002/
## Vulnerability Details

This vulnerability allows remote attackers to bypass API restrictions on vulnerable installations of Adobe Acrobat Reader DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of read-only properties and objects. By creating a specially crafted PDF with specific JavaScript instructions, it is possible to bypass the Javascript API restrictions. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb19-02.html

## Disclosure Timeline

- 2018-09-12 - Vulnerability reported to vendor
- 2019-01-04 - Coordinated public release of advisory
- 2020-08-18 - Advisory Updated
