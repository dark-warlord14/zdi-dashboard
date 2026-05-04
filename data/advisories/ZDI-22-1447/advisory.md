# ZDI-22-1447: Adobe Illustrator PCX File Parsing Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1447
- **ZDI-CAN:** ZDI-CAN-17671
- **Date:** 2022-10-21
- **CVE:** CVE-2022-38435
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Adobe
- **Affected Products:** Illustrator
- **Credit:** Tran Van Khang - khangkito (VinCSS)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1447/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Adobe Illustrator. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of PCX files. The issue results from the lack of proper validation of user-supplied data, which can result in a memory corruption condition. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/si/security/products/illustrator/apsb22-56.html

## Disclosure Timeline

- 2022-06-24 - Vulnerability reported to vendor
- 2022-10-21 - Coordinated public release of advisory
