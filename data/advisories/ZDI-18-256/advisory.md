# ZDI-18-256: OMRON CX-Supervisor SCS File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-256
- **ZDI-CAN:** ZDI-CAN-5305
- **Date:** 2018-03-23
- **CVE:** CVE-2018-7517
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** OMRON
- **Affected Products:** CX-Supervisor
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-256/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of OMRON CX-Supervisor. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of SCS project files. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

OMRON has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-18-072-01

## Disclosure Timeline

- 2017-10-24 - Vulnerability reported to vendor
- 2018-03-23 - Coordinated public release of advisory
- 2018-03-23 - Advisory Updated
