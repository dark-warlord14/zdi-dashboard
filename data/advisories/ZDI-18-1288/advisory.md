# ZDI-18-1288: OMRON CX-Supervisor SCS File Parsing Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1288
- **ZDI-CAN:** ZDI-CAN-6404
- **Date:** 2018-10-17
- **CVE:** CVE-2018-17907
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** OMRON
- **Affected Products:** CX-Supervisor
- **Credit:** b0nd @garage4hackers
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1288/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of OMRON CX-Supervisor. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of SCS files. By manipulating a document's elements, an attacker can trigger a read past the end of an allocated array. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

OMRON has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-18-290-01

## Disclosure Timeline

- 2018-06-22 - Vulnerability reported to vendor
- 2018-10-17 - Coordinated public release of advisory
- 2018-10-17 - Advisory Updated
