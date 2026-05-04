# ZDI-25-1152: (0Day) NSF Unidata NetCDF-C Variable Name Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1152
- **ZDI-CAN:** ZDI-CAN-27267
- **Date:** 2025-12-18
- **CVE:** CVE-2025-14934
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** NSF Unidata
- **Affected Products:** NetCDF-C
- **Credit:** Fady Osman
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1152/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of NSF Unidata NetCDF-C. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of variable names. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

06/03/25 - ZDI reported the vulnerability to the vendor 06/08/25 – the vendor acknowledged the receipt of the report 06/25/25 - ZDI asked for updates 11/06/25 – ZDI asked for updates 12/05/25 – ZDI notified the vendor of the intention to publish the case as a 0-day advisory on 12/18/25 -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product

## Disclosure Timeline

- 2025-06-03 - Vulnerability reported to vendor
- 2025-12-18 - Coordinated public release of advisory
- 2025-12-18 - Advisory Updated
