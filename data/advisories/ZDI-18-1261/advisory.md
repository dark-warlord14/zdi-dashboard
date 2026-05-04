# ZDI-18-1261: LAquis SCADA LQS File Parsing Patamar Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1261
- **ZDI-CAN:** ZDI-CAN-6602
- **Date:** 2018-10-16
- **CVE:** CVE-2018-17901
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** LAquis SCADA
- **Affected Products:** Software
- **Credit:** b0nd @garage4hackers
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1261/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of LAquis SCADA. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of LQS files. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

LAquis SCADA has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-18-289-01

## Disclosure Timeline

- 2018-07-10 - Vulnerability reported to vendor
- 2018-10-16 - Coordinated public release of advisory
- 2018-10-16 - Advisory Updated
