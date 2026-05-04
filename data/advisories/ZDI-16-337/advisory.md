# ZDI-16-337: Panasonic FPWIN Pro SCTASK Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-337
- **ZDI-CAN:** ZDI-CAN-3538
- **Date:** 2016-05-11
- **CVE:** CVE-2016-4496
- **CVSS:** 4.4
- **CVSS Vector:** AV:L/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Panasonic
- **Affected Products:** FPWIN Pro
- **Credit:** Steven Seeley of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-337/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Panasonic FPWIN Pro. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of a project file. A specially-crafted project file will lead to the construction of an SCTASK object followed by writes to the object that are outside its bounds. An attacker can leverage this vulnerability to attain code execution under the context of the current process.

## Additional Details

Panasonic has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-16-131-01

## Disclosure Timeline

- 2016-02-01 - Vulnerability reported to vendor
- 2016-05-11 - Coordinated public release of advisory
