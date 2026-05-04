# ZDI-20-653: Adobe Acrobat Reader DC JPEG2000 File Parsing Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-653
- **ZDI-CAN:** ZDI-CAN-10822
- **Date:** 2020-05-12
- **CVE:** CVE-2020-9612
- **CVSS:** 7.0
- **CVSS Vector:** AV:L/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Reader DC
- **Credit:** L4N
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-653/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Adobe Acrobat Reader DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of JPEG2000 images. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb20-24.html

## Disclosure Timeline

- 2020-03-31 - Vulnerability reported to vendor
- 2020-05-12 - Coordinated public release of advisory
