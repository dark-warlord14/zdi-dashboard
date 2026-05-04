# ZDI-16-684: Adobe Digital Editions PDF FlateDecode Parsing Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-684
- **ZDI-CAN:** ZDI-CAN-3664
- **Date:** 2017-06-13
- **CVE:** CVE-2016-4263
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Digital Editions
- **Credit:** Mario Gomes(@NetFuzzer)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-684/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Digital Editions. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within FlateDecode. A specially crafted PDF with a specific FlateDecode stream can force a dangling pointer to be reused after it has been freed. An attacker could leverage this vulnerability to execute arbitrary code under the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/Digital-Editions/apsb16-28.html

## Disclosure Timeline

- 2016-04-07 - Vulnerability reported to vendor
- 2017-06-13 - Coordinated public release of advisory
