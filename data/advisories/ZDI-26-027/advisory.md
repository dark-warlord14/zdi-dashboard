# ZDI-26-027: (0Day) Foundation Agents MetaGPT actionoutput_str_to_mapping Code Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-027
- **ZDI-CAN:** ZDI-CAN-28124
- **Date:** 2026-01-09
- **CVE:** CVE-2026-0761
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Foundation Agents
- **Affected Products:** MetaGPT
- **Credit:** Peter Girnus (@gothburz) and Brandon Niemczyk of Trend Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-027/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Foundation Agents MetaGPT. Authentication is not required to exploit this vulnerability. The specific flaw exists within the actionoutput_str_to_mapping function. The issue results from the lack of proper validation of a user-supplied string before using it to execute Python code. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

09/19/25 – ZDI submitted the report to the vendor 10/14/25 – ZDI asked for updates 11/10/25 – ZDI asked for updates 12/09/25 – ZDI notified the vendor of the intention to publish the case as a 0-day advisory -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product

## Disclosure Timeline

- 2025-09-19 - Vulnerability reported to vendor
- 2026-01-09 - Coordinated public release of advisory
- 2026-01-09 - Advisory Updated
