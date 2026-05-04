# ZDI-26-032: (0Day) Open WebUI load_tool_module_by_id Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-032
- **ZDI-CAN:** ZDI-CAN-28257
- **Date:** 2026-01-09
- **CVE:** CVE-2026-0766
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Open WebUI
- **Affected Products:** Open WebUI
- **Credit:** Peter Girnus (@gothburz), Brandon Niemczyk of Trend Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-032/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Open WebUI. Authentication is required to exploit this vulnerability. The specific flaw exists within the load_tool_module_by_id function. The issue results from the lack of proper validation of a user-supplied string before using it to execute Python code. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

10/09/25 – ZDI submitted the report to the vendor’s GitHub account 10/10/25 – the vendor closed the report 10/15/25 – ZDI asked for the reason 11/10/25 – ZDI asked for the fix 12/10/25 – ZDI notified the vendor of the intention to publish the case as a 0-day advisory -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product

## Disclosure Timeline

- 2025-10-09 - Vulnerability reported to vendor
- 2026-01-09 - Coordinated public release of advisory
- 2026-01-09 - Advisory Updated
