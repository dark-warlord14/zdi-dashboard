# ZDI-15-609: Adobe Flash MP3 ID3 COMM Tag Heap Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-609
- **ZDI-CAN:** ZDI-CAN-3262
- **Date:** 2015-12-08
- **CVE:** CVE-2015-8446
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Flash
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-609/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Flash. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of MP3 files. The issue lies in the failure to allocate enough space for COMM tags. An attacker could leverage this vulnerability to execute arbitrary code under the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/flash-player/apsb15-32.html

## Disclosure Timeline

- 2015-09-03 - Vulnerability reported to vendor
- 2015-12-08 - Coordinated public release of advisory
