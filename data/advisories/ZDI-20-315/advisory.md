# ZDI-20-315: Adobe Photoshop PCX File Parsing Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-315
- **ZDI-CAN:** ZDI-CAN-9926
- **Date:** 2020-03-19
- **CVE:** CVE-2020-3770
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Adobe
- **Affected Products:** Photoshop
- **Credit:** Yu Zhou(@yuzhou6666)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-315/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Adobe Photoshop. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of PCX files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/photoshop/apsb20-14.html

## Disclosure Timeline

- 2019-12-17 - Vulnerability reported to vendor
- 2020-03-19 - Coordinated public release of advisory
