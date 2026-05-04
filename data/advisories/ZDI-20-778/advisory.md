# ZDI-20-778: (Pwn2Own) ICONICS Genesis64 VariantClear Out-Of-Bounds Access Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-778
- **ZDI-CAN:** ZDI-CAN-10274
- **Date:** 2020-06-30
- **CVE:** CVE-2020-12011
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** ICONICS
- **Affected Products:** Genesis64
- **Credit:** Tobias Scharnowski, Niklas Breitfeld, and Ali Abbasi
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-778/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of ICONICS Genesis64. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of indexes. The issue results from the lack of proper validation of user-supplied data, which can result in a memory access past the end of an allocated structure. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

ICONICS has issued an update to correct this vulnerability. More details can be found at: https://www.us-cert.gov/ics/advisories/icsa-20-170-03

## Disclosure Timeline

- 2020-01-30 - Vulnerability reported to vendor
- 2020-06-30 - Coordinated public release of advisory
