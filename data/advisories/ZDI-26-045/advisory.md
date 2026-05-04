# ZDI-26-045: Cisco Snort _bnfa_search_csparse_nfa Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-045
- **ZDI-CAN:** ZDI-CAN-27893
- **Date:** 2026-01-28
- **CVE:** CVE-2026-20027
- **CVSS:** 5.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N
- **Affected Vendors:** Cisco
- **Affected Products:** Snort
- **Credit:** Guy Lederfein of Trend Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-045/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Cisco Snort. Authentication is not required to exploit this vulnerability. The specific flaw exists within the _bnfa_search_csparse_nfa method. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the service account.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-snort3-dcerpc-vulns-J9HNF4tH

## Disclosure Timeline

- 2025-08-12 - Vulnerability reported to vendor
- 2026-01-28 - Coordinated public release of advisory
- 2026-01-28 - Advisory Updated
