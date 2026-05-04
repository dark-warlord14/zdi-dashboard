# ZDI-21-1074: Siemens Simcenter STAR-CCM+ SCE File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1074
- **ZDI-CAN:** ZDI-CAN-13700
- **Date:** 2021-09-15
- **CVE:** CVE-2021-25665
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Siemens
- **Affected Products:** Simcenter STAR-CCM+
- **Credit:** Francis Provencher {PRL}
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1074/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Siemens Simcenter STAR-CCM+. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of SCE files. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated data structure. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Siemens has issued an update to correct this vulnerability. More details can be found at: https://us-cert.cisa.gov/ics/advisories/icsa-21-257-05

## Disclosure Timeline

- 2021-06-04 - Vulnerability reported to vendor
- 2021-09-15 - Coordinated public release of advisory
