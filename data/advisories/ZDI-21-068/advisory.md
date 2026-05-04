# ZDI-21-068: Panasonic Control FPWIN Pro Project File Parsing Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-068
- **ZDI-CAN:** ZDI-CAN-11579
- **Date:** 2021-01-14
- **CVE:** CVE-2020-16236
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Panasonic
- **Affected Products:** Control FPWIN Pro
- **Credit:** Francis Provencher {PRL}
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-068/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Panasonic Control FPWIN Pro. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of PRO files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated data structure. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Panasonic has issued an update to correct this vulnerability. More details can be found at: https://us-cert.cisa.gov/ics/advisories/icsa-21-005-02

## Disclosure Timeline

- 2020-08-05 - Vulnerability reported to vendor
- 2021-01-14 - Coordinated public release of advisory
