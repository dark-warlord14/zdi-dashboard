# ZDI-20-331: Adobe Media Encoder 3GP File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-331
- **ZDI-CAN:** ZDI-CAN-10070
- **Date:** 2020-03-24
- **CVE:** CVE-2020-3764
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Adobe
- **Affected Products:** Media Encoder
- **Credit:** Francis Provencher {PRL}
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-331/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Adobe Media Encoder CC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of 3GP files. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated structure. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/media-encoder/apsb20-10.html

## Disclosure Timeline

- 2020-01-10 - Vulnerability reported to vendor
- 2020-03-24 - Coordinated public release of advisory
