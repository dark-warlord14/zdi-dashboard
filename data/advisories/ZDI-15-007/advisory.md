# ZDI-15-007: Adobe Flash Player AVSegmentedSource::getABRProfileInfoAtIndex Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-007
- **ZDI-CAN:** ZDI-CAN-2601
- **Date:** 2015-01-21
- **CVE:** CVE-2015-0307
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Flash Player
- **Credit:** bilou
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-007/
## Vulnerability Details

This vulnerability allows remote attackers to disclose arbitrary memory on vulnerable installations of Adobe Flash. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the AVSegmentedSource::getABRProfileInfoAtIndex function. Once the AVSegmentedSource class is initialized with a valid m3u8 file, it is possible for an attacker to force out-of-bounds reads. An attacker can leverage this vulnerability to disclose arbitrary memory.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://helpx.adobe.com/security/products/flash-player/apsb15-01.html

## Disclosure Timeline

- 2014-11-04 - Vulnerability reported to vendor
- 2015-01-21 - Coordinated public release of advisory
