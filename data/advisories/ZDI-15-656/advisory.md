# ZDI-15-656: Adobe Flash MPEG-4 Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-656
- **ZDI-CAN:** ZDI-CAN-3416
- **Date:** 2016-03-02
- **CVE:** CVE-2015-8652
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Flash
- **Credit:** AbdulAziz Hariri - HPE Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-656/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Flash. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within MPEG-4 parsing. A specially crafted MP4 file can force Adobe Flash to read memory past the end of an allocated object. An attacker could leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/flash-player/apsb15-32.html

## Disclosure Timeline

- 2015-11-17 - Vulnerability reported to vendor
- 2016-03-02 - Coordinated public release of advisory
