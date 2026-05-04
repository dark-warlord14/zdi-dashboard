# ZDI-15-091: MICROSYS PROMOTIC Stack Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-091
- **ZDI-CAN:** ZDI-CAN-2543
- **Date:** 2015-03-12
- **CVE:** CVE-2014-9205
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** MICROSYS
- **Affected Products:** PROMOTIC
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-091/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of MICROSYS PROMOTIC. Authentication is not required to exploit this vulnerability. The program blindly copies attacker-supplied data into a fixed-sized buffer without validating the length of this data resulting in a stack buffer overflow. The specific flaw exists within the PmBase64Decode function which ignores the passed-in length of the destination buffer. An attacker can exploit this condition to achieve code execution under the context of the process.

## Additional Details

MICROSYS has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-15-062-01

## Disclosure Timeline

- 2014-11-19 - Vulnerability reported to vendor
- 2015-03-12 - Coordinated public release of advisory
