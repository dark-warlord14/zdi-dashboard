# ZDI-18-569: Adobe Flash RTMP Parsing Integer Overflow Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-569
- **ZDI-CAN:** ZDI-CAN-5614
- **Date:** 2018-06-07
- **CVE:** CVE-2018-5000
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** Flash
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-569/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Adobe Flash. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists in the handling of RTMP data. The issue results from the lack of proper validation of user-supplied data, which can result in an integer overflow before reading from memory. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/flash-player/apsb18-19.html

## Disclosure Timeline

- 2018-04-25 - Vulnerability reported to vendor
- 2018-06-07 - Coordinated public release of advisory
- 2018-06-07 - Advisory Updated
