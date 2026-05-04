# ZDI-20-1355: Adobe Acrobat Pro DC PDF Export Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1355
- **ZDI-CAN:** ZDI-CAN-11957
- **Date:** 2020-11-10
- **CVE:** CVE-2020-24436
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Pro DC
- **Credit:** kimiya
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1355/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Adobe Acrobat Pro DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the exporting of PDF files. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated structure. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb20-67.html

## Disclosure Timeline

- 2020-09-30 - Vulnerability reported to vendor
- 2020-11-10 - Coordinated public release of advisory
