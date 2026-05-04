# ZDI-17-441: Apple Safari Node Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-441
- **ZDI-CAN:** ZDI-CAN-4537
- **Date:** 2017-06-22
- **CVE:** CVE-2017-2454
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** Zheng Huang of the Baidu Security Lab
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-441/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Safari. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of Node objects. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT207617

## Disclosure Timeline

- 2017-03-09 - Vulnerability reported to vendor
- 2017-06-22 - Coordinated public release of advisory
