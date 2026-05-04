# ZDI-19-907: Adobe Media Encoder CC MP4 File Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-907
- **ZDI-CAN:** ZDI-CAN-8804
- **Date:** 2019-10-21
- **CVE:** CVE-2019-8243
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** Media Encoder
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-907/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Adobe Media Encoder CC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of MP4 files. Crafted data in an MP4 file can trigger a read outside the bounds of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/media-encoder/apsb19-52.html

## Disclosure Timeline

- 2019-08-08 - Vulnerability reported to vendor
- 2019-10-21 - Coordinated public release of advisory
- 2019-11-14 - Advisory Updated
