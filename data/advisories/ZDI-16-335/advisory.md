# ZDI-16-335: Panasonic FPWIN Pro ReleaseBuffer Integer Overflow Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-335
- **ZDI-CAN:** ZDI-CAN-3503
- **Date:** 2016-05-11
- **CVE:** CVE-2016-4496
- **CVSS:** 4.4
- **CVSS Vector:** AV:L/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Panasonic
- **Affected Products:** FPWIN Pro
- **Credit:** Steven Seeley of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-335/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Panasonic FPWIN Pro. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within processing of a project file. A specially-crafted project file will lead to a write beyond the end of a heap buffer in the ReleaseBuffer method of the CString object due to a confusion between signed and unsigned integers in the GetBlockFromStream method of the CSCString object. An attacker can leverage this vulnerability to attain code execution under the context of the current process.

## Additional Details

Panasonic has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-16-131-01

## Disclosure Timeline

- 2016-01-19 - Vulnerability reported to vendor
- 2016-05-11 - Coordinated public release of advisory
