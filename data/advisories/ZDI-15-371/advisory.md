# ZDI-15-371: (Pwn2Own) Adobe Reader makeMeasurement Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-371
- **ZDI-CAN:** ZDI-CAN-3105
- **Date:** 2015-07-29
- **CVE:** CVE-2015-5107
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** Reader
- **Credit:** Nicolas Joly
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-371/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Adobe Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of arguments passed to the makeMeasurement method. A specially crafted argument to makeMeasurement will leave objects in an inconsistent state. This data can later be retrieved via a call to dumpMeasureData. An attacker can leverage this vulnerability to disclose sensitive information about the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/reader/apsb15-15.html

## Disclosure Timeline

- 2015-03-18 - Vulnerability reported to vendor
- 2015-07-29 - Coordinated public release of advisory
