# ZDI-21-1322: WECON PLC Editor WCP File Parsing Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1322
- **ZDI-CAN:** ZDI-CAN-13917
- **Date:** 2021-11-18
- **CVE:** CVE-2021-42707
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** WECON
- **Affected Products:** PLC Editor
- **Credit:** Natnael Samson (@NattiSamson)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1322/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of WECON PLC Editor. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of WCP files. The issue results from the lack of proper validation of user-supplied data, which can result in a memory corruption condition. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

WECON has issued an update to correct this vulnerability. More details can be found at: https://us-cert.cisa.gov/ics/advisories/icsa-21-315-01

## Disclosure Timeline

- 2021-06-24 - Vulnerability reported to vendor
- 2021-11-18 - Coordinated public release of advisory
