# ZDI-20-1360: WECON PLC Editor WCP File Parsing Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1360
- **ZDI-CAN:** ZDI-CAN-11187
- **Date:** 2020-11-10
- **CVE:** CVE-2020-25181
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** WECON
- **Affected Products:** PLC Editor
- **Credit:** Natnael Samson (@NattiSamson)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1360/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of WECON PLC Editor. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of WCP files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of an administrator.

## Additional Details

WECON has issued an update to correct this vulnerability. More details can be found at: https://us-cert.cisa.gov/ics/advisories/icsa-20-310-01

## Disclosure Timeline

- 2020-07-15 - Vulnerability reported to vendor
- 2020-11-10 - Coordinated public release of advisory
