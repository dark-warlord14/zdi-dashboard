# ZDI-22-1430: Adobe Acrobat Reader DC JP2 File Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1430
- **ZDI-CAN:** ZDI-CAN-18538
- **Date:** 2022-10-14
- **CVE:** CVE-2022-38449
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Reader DC
- **Credit:** soiax
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1430/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Adobe Acrobat Reader DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of JP2 images. Crafted data in a JP2 image can trigger a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb22-46.html

## Disclosure Timeline

- 2022-09-06 - Vulnerability reported to vendor
- 2022-10-14 - Coordinated public release of advisory
