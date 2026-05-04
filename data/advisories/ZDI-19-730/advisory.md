# ZDI-19-730: Adobe Photoshop PostScript put Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-730
- **ZDI-CAN:** ZDI-CAN-8481
- **Date:** 2019-08-19
- **CVE:** CVE-2019-7984
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Adobe
- **Affected Products:** Photoshop
- **Credit:** Steven Seeley (mr_me) of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-730/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Adobe Photoshop. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of the put command in PostScript. The issue results from the lack of proper validation of user-supplied data, which can result in read and write operations past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/photoshop/apsb19-44.html

## Disclosure Timeline

- 2019-05-08 - Vulnerability reported to vendor
- 2019-08-19 - Coordinated public release of advisory
