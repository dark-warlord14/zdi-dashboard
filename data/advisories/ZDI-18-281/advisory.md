# ZDI-18-281: OMRON CX-One CX-Motion sscanf Stack-based Buffer Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-281
- **ZDI-CAN:** ZDI-CAN-5402
- **Date:** 2018-04-11
- **CVE:** CVE-2018-7514
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** OMRON
- **Affected Products:** CX-One
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-281/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of OMRON CX-One. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of MCI files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a stack-based buffer. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

OMRON has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-18-100-02

## Disclosure Timeline

- 2017-12-01 - Vulnerability reported to vendor
- 2018-04-11 - Coordinated public release of advisory
- 2018-04-11 - Advisory Updated
