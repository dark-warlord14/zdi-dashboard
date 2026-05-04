# ZDI-26-029: (0Day) GPT Academic run_in_subprocess_wrapper_func Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-029
- **ZDI-CAN:** ZDI-CAN-27958
- **Date:** 2026-01-09
- **CVE:** CVE-2026-0763
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** GPT Academic
- **Affected Products:** GPT Academic
- **Credit:** Peter Girnus (@gothburz) of Trend Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-029/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of GPT Academic. Authentication is not required to exploit this vulnerability. The specific flaw exists within the run_in_subprocess_wrapper_func function. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

08/27/25 – ZDI submitted the report to the vendor 09/24/25 – ZDI asked for updates 10/22/25 – ZDI asked for updates 12/10/25 – ZDI notified the vendor of the intention to publish the case as a 0-day advisory -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product

## Disclosure Timeline

- 2025-08-26 - Vulnerability reported to vendor
- 2026-01-09 - Coordinated public release of advisory
- 2026-01-09 - Advisory Updated
