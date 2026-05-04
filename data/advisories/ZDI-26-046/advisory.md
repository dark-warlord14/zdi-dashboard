# ZDI-26-046: Cisco Snort _bnfa_search_csparse_nfa Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-046
- **ZDI-CAN:** ZDI-CAN-27892
- **Date:** 2026-01-28
- **CVE:** CVE-2026-20026
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Cisco
- **Affected Products:** Snort
- **Credit:** Guy Lederfein of Trend Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-046/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Cisco Snort. Authentication is not required to exploit this vulnerability. The specific flaw exists within the _bnfa_search_csparse_nfa method. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-snort3-dcerpc-vulns-J9HNF4tH

## Disclosure Timeline

- 2025-08-12 - Vulnerability reported to vendor
- 2026-01-28 - Coordinated public release of advisory
- 2026-01-28 - Advisory Updated
