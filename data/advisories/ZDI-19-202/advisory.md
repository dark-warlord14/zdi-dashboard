# ZDI-19-202: Adobe Reader DC Name Squatting JavaScript Restrictions Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-202
- **ZDI-CAN:** ZDI-CAN-7334
- **Date:** 2019-02-12
- **CVE:** CVE-2019-7041
- **CVSS:** 2.7
- **CVSS Vector:** AV:L/AC:H/PR:N/UI:R/S:C/C:L/I:N/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Reader DC
- **Credit:** Abdul-Aziz Hariri and Jasiel Spelman of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-202/
## Vulnerability Details

This vulnerability allows remote attackers to bypass JavaScript API restrictions on vulnerable installations of Adobe Reader DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists due to a mispelled API in the built-in encoded JavaScript scripts. By creating a specially crafted PDF with specific JavaScript instructions, it is possible to bypass the Javascript API restrictions. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb19-07.html

## Disclosure Timeline

- 2018-10-04 - Vulnerability reported to vendor
- 2019-02-12 - Coordinated public release of advisory
