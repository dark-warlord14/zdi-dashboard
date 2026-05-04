# ZDI-18-1418: Adobe Reader DC JavaScript ANSendForSharedReview JavaScript API Restrictions Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1418
- **ZDI-CAN:** ZDI-CAN-7272
- **Date:** 2018-12-17
- **CVE:** CVE-2018-16018
- **CVSS:** 2.7
- **CVSS Vector:** AV:L/AC:H/PR:N/UI:R/S:C/C:L/I:N/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Reader DC
- **Credit:** Abdul-Aziz Hariri of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1418/
## Vulnerability Details

This vulnerability allows remote attackers to bypass JavaScript API restrictions on vulnerable installations of Adobe Reader DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the ANSendForSharedReview method. By creating a specially crafted PDF with specific Javascript instructions, it is possible to bypass the Javascript API restrictions. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb18-41.html

## Disclosure Timeline

- 2018-09-24 - Vulnerability reported to vendor
- 2018-12-17 - Coordinated public release of advisory
