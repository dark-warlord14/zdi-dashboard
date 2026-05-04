# ZDI-26-035: (0Day) Langflow eval_custom_component_code Eval Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-035
- **ZDI-CAN:** ZDI-CAN-26972
- **Date:** 2026-01-09
- **CVE:** CVE-2026-0769
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Langflow
- **Affected Products:** Langflow
- **Credit:** Peter Girnus (@gothburz) of Trend Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-035/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Langflow. Authentication is not required to exploit this vulnerability. The specific flaw exists within the implementation of eval_custom_component_code function. The issue results from the lack of proper validation of a user-supplied string before using it to execute python code. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

07/18/25 – ZDI submitted the report to the vendor’s GitHub account 09/11/25 – ZDI asked for updates 10/10/25 – ZDI asked for the fix 12/10/25 – ZDI notified the vendor of the intention to publish the case as a 0-day advisory -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product

## Disclosure Timeline

- 2025-07-18 - Vulnerability reported to vendor
- 2026-01-09 - Coordinated public release of advisory
- 2026-01-09 - Advisory Updated
