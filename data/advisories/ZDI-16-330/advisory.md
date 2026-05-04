# ZDI-16-330: Panasonic FPWIN Pro OPNISAMX Heap Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-330
- **ZDI-CAN:** ZDI-CAN-3446
- **Date:** 2016-05-11
- **CVE:** CVE-2016-4499
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Panasonic
- **Affected Products:** FPWIN Pro
- **Credit:** Steven Seeley of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-330/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Panasonic FPWIN Pro. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within parsing of project files. A specially-crafted project file can cause a heap buffer overrun in a memcpy call. An attacker can leverage this vulnerability to execute arbitrary code in the context of the current process.

## Additional Details

Panasonic has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-16-131-01

## Disclosure Timeline

- 2016-01-19 - Vulnerability reported to vendor
- 2016-05-11 - Coordinated public release of advisory
