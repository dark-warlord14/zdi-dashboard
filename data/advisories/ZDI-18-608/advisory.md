# ZDI-18-608: Eaton 9000XDrive TLF File Parsing Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-608
- **ZDI-CAN:** ZDI-CAN-5669
- **Date:** 2018-07-12
- **CVE:** CVE-2018-8847
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Eaton
- **Affected Products:** 9000XDrive
- **Credit:** Ghirmay Desta
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-608/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Eaton 9000XDrive. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of a TLF file. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a stack-based buffer. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Eaton has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-18-193-01

## Disclosure Timeline

- 2018-02-23 - Vulnerability reported to vendor
- 2018-07-12 - Coordinated public release of advisory
- 2018-07-12 - Advisory Updated
