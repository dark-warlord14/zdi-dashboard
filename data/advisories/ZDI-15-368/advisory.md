# ZDI-15-368: (Pwn2Own) Adobe Reader makeMeasurement Stack Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-368
- **ZDI-CAN:** ZDI-CAN-2821
- **Date:** 2015-07-29
- **CVE:** CVE-2015-5110
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Reader
- **Credit:** Nicolas Joly
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-368/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of arguments passed to the makeMeasurement method. A specially crafted argument passed to makeMeasurement can overflow a buffer of size 0x64 bytes. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/reader/apsb15-15.html

## Disclosure Timeline

- 2015-03-18 - Vulnerability reported to vendor
- 2015-07-29 - Coordinated public release of advisory
